from datetime import datetime, timezone
import json
import os
from pathlib import Path

from scholarly import scholarly


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT / "_data" / "google_scholar_publications.json"
SCHOLAR_ID = os.environ.get("GOOGLE_SCHOLAR_ID") or "8F7li3AAAAAJ"
SCHOLAR_PROFILE = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=zh-CN"


def bold_self(author_text):
    return (
        author_text.replace("Y Wang", "**Y Wang**")
        .replace("Yuxi Wang", "**Yuxi Wang**")
        .replace("王愉茜", "**王愉茜**")
    )


def existing_overrides():
    if not OUTPUT_PATH.exists():
        return {}
    data = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    return {item["title"]: item for item in data.get("publications", [])}


def citation_url(author_pub_id):
    return (
        "https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN"
        f"&user={SCHOLAR_ID}&citation_for_view={author_pub_id}"
    )


def publication_year(pub):
    bib = pub.get("bib", {})
    raw_year = bib.get("pub_year") or bib.get("year") or ""
    try:
        return int(raw_year)
    except (TypeError, ValueError):
        return 0


def normalize_publication(pub, source_index, overrides):
    bib = pub.get("bib", {})
    title = bib.get("title", "").strip()
    authors = bold_self(bib.get("author", "").strip())
    venue = bib.get("citation", "").strip()
    year = publication_year(pub)
    author_pub_id = pub.get("author_pub_id", "")
    link = citation_url(author_pub_id) if author_pub_id else pub.get("pub_url", "")

    item = {
        "title": title,
        "authors": authors,
        "venue": venue,
        "year": year,
        "link": link,
        "cite": link,
        "source_index": source_index,
    }

    existing = overrides.get(title, {})
    for key in ("pdf", "doi"):
        if existing.get(key):
            item[key] = existing[key]
    if existing.get("link") and not item["link"]:
        item["link"] = existing["link"]
    if existing.get("cite") and not item["cite"]:
        item["cite"] = existing["cite"]

    return item


def main():
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=["publications"])

    overrides = existing_overrides()
    publications = [
        normalize_publication(pub, index, overrides)
        for index, pub in enumerate(author.get("publications", []), start=1)
        if pub.get("bib", {}).get("title")
    ]
    publications.sort(key=lambda item: (-item["year"], item["source_index"]))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "source": SCHOLAR_PROFILE,
        "publications": publications,
    }
    OUTPUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

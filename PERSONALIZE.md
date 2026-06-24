# Personalization Guide

This site is based on `RayeRen/acad-homepage.github.io`.

## Files to edit first

- `_config.yml`: site title, repository, avatar, email, Google Scholar, GitHub, LinkedIn, ORCID, and other profile links.
- `_pages/about.md`: biography, news, publications, research interests, education, awards, experience, talks, and services.
- `_data/navigation.yml`: top navigation labels and anchor links.
- `images/`: replace the avatar and paper thumbnails.

## Local preview

Install Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`.

## GitHub Pages

1. Create a repository named `YOUR_GITHUB_USERNAME.github.io`.
2. Replace `YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME.github.io` in `_config.yml`.
3. Push this folder to the repository.
4. Enable GitHub Pages from the repository settings if it is not enabled automatically.

## Recommended personal details to prepare

- English name and optional Chinese name.
- Current position and institution.
- Research areas.
- Email and profile links.
- Education history.
- Publication list with paper, project, code, and thumbnail links.
- Awards, talks, academic services, and selected experience.

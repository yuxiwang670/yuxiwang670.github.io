---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am **Yuxi Wang (王愉茜)**, a **Ph.D. candidate in Applied Psychology** at **Peking University**. My current research focuses on **metacognition and autonomous learning in AI agents**: whether a model knows when it does not know, and whether it can actively ask questions or seek information to reduce uncertainty.

More broadly, I study **active belief control** in autonomous AI agents operating under uncertainty. Rather than only evaluating model performance from the outside or cataloging failure modes after they occur, I am interested in how an agent forms internal beliefs about task rules, environmental states, and its own capabilities when information is incomplete, rules are unknown, and goals are ambiguous. A central question is how such an agent monitors the uncertainty and reliability of these beliefs, and how it decides whether to act directly, ask questions, continue exploring, request feedback, revise hypotheses, or pause/refuse action when the risk is high.

To address this problem, I aim to integrate computational cognition, Bayesian learning, concept learning, active learning, reinforcement learning, and metacognitive theory into a cognitive control framework for autonomous agents. This framework organizes **belief formation**, **uncertainty estimation**, **metacognitive monitoring**, **active information seeking**, **belief revision**, and **safe action gating** into a testable, interpretable, and trainable loop. From this perspective, metacognitive benchmarks, autonomous learning benchmarks, unknown-rule learning tasks, human-agent trust tasks, and agent-safety evaluations are not separate projects, but complementary environments for developing and testing active belief control. In the long run, I hope this framework can support cognitive evaluation, mechanistic explanation, and safety-oriented design for general-purpose AI agents.

For the most up-to-date publication list and citation metrics, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8F7li3AAAAAJ&hl=zh-CN). Google Scholar lists **15 citations**, **h-index 2**, and **i10-index 0** as of 2026-06-24.

# News
{% include section-news.html %}

# Publications

{% include section-publications.html %}

# Honors and Awards
{% include section-honors.html %}

# Educations
{% include section-educations.html %}

# Invited Talks
{% include section-invited-talks.html %}

# Internships
{% include section-internships.html %}

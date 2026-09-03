---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

👋 **I am Yuxi Wang (王愉茜), a research scientist at BIGAI.**

我是王愉茜，目前是 BIGAI 的研究员。

🧠 **My research asks: How can AI systems monitor and regulate their own cognitive processes?**

我的研究关注：AI 系统如何监控并调节自身的认知过程？

Drawing on my background in cognitive science and neuroscience, my current research focuses on **AI metacognition**—how artificial agents assess their own knowledge, uncertainty, and limitations, and use this information to guide learning, reasoning, and decision-making.

基于认知科学与神经科学的研究背景，我目前主要关注 **AI 元认知**：人工智能体如何评估自身的知识、不确定性与能力边界，并利用这些信息指导学习、推理与决策。

🔍 I also work on **the evaluation and interpretability of AI cognitive capabilities**. By drawing on theories and experimental paradigms from cognitive science, I develop cognitively grounded evaluations and benchmarks, and investigate the relationships among models’ internal representations, self-reports, and observable behavior.

我也关注 **AI 认知能力的评测与可解释性**。通过借鉴认知科学的理论与实验范式，我尝试构建具有认知理论基础的评测与基准，并考察模型内部表征、自我报告与外部行为之间的关系。

🌱 **Ultimately, I aim to contribute to the development of AI systems that can recognize their limitations, regulate their behavior, and adapt autonomously—making artificial intelligence more general, interpretable, reliable, and trustworthy.**

最终，我希望推动能够识别自身局限、调节自身行为并自主适应的 AI 系统发展，使人工智能更加通用、可解释、可靠且可信赖。

For the most up-to-date publication list and citation metrics, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8F7li3AAAAAJ&hl=zh-CN).
<!-- Google Scholar lists **15 citations**, **h-index 2**, and **i10-index 0** as of 2026-06-24. -->

# News
{% include section-news.html %}

# Publications

{% include section-publications.html source="collection" %}

# Invited Talks
*More updates coming soon.*

{% comment %}
{% include section-invited-talks.html %}
{% endcomment %}

{% comment %}
# Honors and Awards
{% include section-honors.html %}
{% endcomment %}

{% comment %}
# Educations
{% include section-educations.html %}
{% endcomment %}

{% comment %}
# Internships
{% include section-internships.html %}
{% endcomment %}

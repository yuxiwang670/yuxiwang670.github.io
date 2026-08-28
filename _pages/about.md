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

我是王愉茜，目前是 BIGAI 的 research scientist。

🧠 **My research asks: How can AI systems monitor and regulate their own cognitive processes?**

我的研究关注：AI 系统如何监控并调节自身的认知过程？

Inspired by cognitive science and neuroscience, I study **AI metacognition**—the capacity of artificial agents to assess their own knowledge, uncertainty, and limitations, and to use this information to regulate learning, reasoning, and decision-making.

受认知科学与神经科学启发，我研究 **AI 元认知**：人工智能体如何评估自身的知识、不确定性与能力边界，并利用这些信息调节学习、推理和决策。

🔍 **My current work investigates the computational and behavioral foundations of metacognition in AI.** I examine whether AI systems can reliably distinguish when they are likely to be correct or mistaken, monitor the sources and quality of evidence, update confidence appropriately, seek information selectively, and learn from feedback in unfamiliar environments.

我目前主要研究 AI 元认知的计算与行为基础，包括：AI 能否可靠地区分自身判断正确或错误的可能性，监控信息的来源与质量，合理更新信心，选择性地获取信息，并在陌生环境中利用反馈持续学习。

To address these questions, I combine computational cognitive modeling, Bayesian approaches, behavioral experiments, and cognitively grounded benchmark design. I also study how internal representations, reported confidence, and observable behavior relate to one another, aiming to distinguish genuine self-monitoring from superficial verbal or behavioral patterns.

在研究方法上，我结合计算认知建模、贝叶斯方法、行为实验和具有认知理论基础的评测设计，并考察模型内部表征、置信报告与外部行为之间的关系，以区分结构化的自我监控与表层的语言或行为模式。

🌱 **Ultimately, I aim to establish a cognitive and computational foundation for AI systems that can recognize their limitations, regulate their behavior, and adapt autonomously—contributing to the development of more general, reliable, and trustworthy artificial intelligence.**

最终，我希望为能够识别自身局限、调节自身行为并自主适应的 AI 系统建立认知与计算基础，从而推动更加通用、可靠且可信赖的人工智能。

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

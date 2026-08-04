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

🧠 **My research asks: How can we understand and develop cognitive capabilities that enable more general and adaptive artificial intelligence?**

我的研究关注：我们如何理解并发展能够支持更通用、更具适应性的人工智能的认知能力？

Inspired by cognitive science and neuroscience, I study the principles underlying intelligence and explore how they can guide the development of AI systems with stronger abilities in learning, adaptation, self-monitoring, and autonomous decision-making.

受认知科学和神经科学启发，我研究智能背后的基本原理，并探索这些原理如何指导 AI 系统的发展，使其具备更强的学习、适应、自我监控和自主决策能力。

🔍 **My current research focuses on AI cognitive capabilities, including metacognition, uncertainty awareness, self-monitoring, autonomous learning, and AI interpretability. Through computational cognitive modeling, Bayesian learning, and cognitively grounded benchmark design, I investigate how AI agents can understand their own knowledge states, recognize limitations, provide meaningful explanations for their behaviors, learn from feedback, and improve in unfamiliar environments.**

我目前的研究聚焦于 AI 认知能力，包括元认知、不确定性感知、自我监控、自主学习以及 AI 可解释性。我结合计算认知建模、贝叶斯学习和具有认知基础的 benchmark 设计，研究 AI 智能体如何理解自身知识状态、识别能力边界、解释自身行为决策、从反馈中学习，并在陌生环境中持续改进。

🔎 **I am also interested in developing interpretable and trustworthy AI systems. By studying the relationship between internal representations, decision processes, and observable behaviors of AI models, I aim to understand why AI systems make certain decisions and how they can better monitor, explain, and improve themselves.**

我也对构建可解释、可信赖的 AI 系统感兴趣。通过研究 AI 模型内部表征、决策过程与外部行为之间的关系，我希望理解 AI 系统为何做出特定决策，并探索如何让 AI 更好地监控、解释和改进自身。

🌱 **Ultimately, I aim to contribute to the cognitive foundations of artificial general intelligence (AGI) by developing AI systems that are not only capable of solving tasks, but also able to understand, adapt, explain, and regulate themselves.**

最终，我希望通过发展不仅能够完成任务、也能够理解、适应、解释并调节自身的 AI 系统，为通用人工智能（AGI）的认知基础做出贡献。

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

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

👋 **I am Yuxi Wang (王愉茜), a researcher at BIGAI.**

**我是王愉茜，目前是 BIGAI 的 researcher。**

🧠 **My research asks: How can we understand and develop cognitive capabilities that enable more general and adaptive artificial intelligence?**

**我的研究关注：我们如何理解并发展能够支持更通用、更具适应性的人工智能的认知能力？**

Inspired by **cognitive science and neuroscience**, I study the principles underlying intelligence and explore how they can guide the development of AI systems with stronger abilities in **learning, adaptation, self-monitoring, and autonomous decision-making**.

受**认知科学和神经科学**启发，我研究智能背后的基本原理，并探索这些原理如何指导 AI 系统的发展，使其具备更强的**学习、适应、自我监控和自主决策**能力。

🔍 My current research focuses on **AI cognitive capabilities**, including **metacognition, uncertainty awareness, self-monitoring, and autonomous learning**. Through **computational cognitive modeling, Bayesian learning, and cognitively grounded benchmark design**, I investigate how AI agents can understand their own knowledge states, recognize limitations, learn from feedback, and improve in unfamiliar environments.

我目前的研究聚焦于 **AI 认知能力**，包括**元认知、不确定性感知、自我监控和自主学习**。我结合**计算认知建模、贝叶斯学习和具有认知基础的 benchmark 设计**，研究 AI 智能体如何理解自身知识状态、识别能力边界、从反馈中学习，并在陌生环境中持续改进。

🌱 Ultimately, I aim to contribute to the cognitive foundations of **artificial general intelligence (AGI)** by developing AI systems that are not only capable of solving tasks, but also able to **understand, adapt, and regulate themselves**.

最终，我希望通过发展不仅能够完成任务、也能够**理解、适应并调节自身**的 AI 系统，为**通用人工智能（AGI）**的认知基础做出贡献。

For the most up-to-date publication list and citation metrics, please visit my [Google Scholar profile](https://scholar.google.com/citations?user=8F7li3AAAAAJ&hl=zh-CN).
<!-- Google Scholar lists **15 citations**, **h-index 2**, and **i10-index 0** as of 2026-06-24. -->

# News
{% include section-news.html %}

# Publications

{% include section-publications.html %}

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

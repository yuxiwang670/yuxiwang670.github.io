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

I am **Yuxi Wang (王愉茜)**, a **Ph.D. in Applied Psychology** from **Peking University**. My research focuses on **belief formation**, **cognitive bias**, and **metacognitive regulation** in human and artificial intelligence. The foundation of my work is computational cognitive science: I study how intelligent systems process uncertain information, form beliefs, monitor their own reliability, and update their judgments through evidence and feedback.

My previous work examined biased information processing in social anxiety, using behavioral experiments, Bayesian modeling, and cognitive neuroscience methods to understand how prior expectations and external evidence shape human judgments under uncertainty. Building on this foundation, my current research extends this perspective to **AI agents**. I am interested in how AI systems form beliefs, develop cognitive biases, monitor their own knowledge and limitations, and regulate their actions when information is incomplete or uncertain.

My research chain moves from **human cognitive bias** to **AI cognitive bias**, **AI metacognition**, **active belief control**, **human-AI trust**, and **cognitive safety**. Methodologically, I combine computational cognitive modeling, Bayesian learning, concept learning, active learning, reinforcement learning, and cognitively grounded benchmark design. My long-term goal is to develop evaluation frameworks and task environments that help us understand and improve the **metacognitive reliability**, **trustworthiness**, and **safety** of autonomous AI agents.

我是**王愉茜**，于**北京大学应用心理学专业**获得博士学位。我的研究关注人类与人工智能中的**信念形成**、**认知偏差**和**元认知调节**。我的研究基础是计算认知科学：我关注智能系统如何处理不确定信息、形成信念、监控自身可靠性，并通过证据和反馈更新判断。

我过去的研究主要考察社交焦虑中的偏差信息加工，结合行为实验、贝叶斯建模和认知神经科学方法，理解先验期待与外部证据如何共同塑造人在不确定情境下的判断。在此基础上，我目前的研究将这一视角拓展到**AI 智能体**，关注 AI 系统如何形成信念、发展认知偏差、监控自身知识与能力边界，并在信息不完整或不确定时调节自身行动。

我的研究链条从**人类认知偏差**延伸到 **AI 认知偏差**、**AI 元认知**、**主动信念控制**、**人机互信**和**认知安全**。在方法上，我结合计算认知建模、贝叶斯学习、概念学习、主动学习、强化学习和具有认知基础的 benchmark 设计。我的长期目标是构建评测框架和任务环境，帮助我们理解并提升自主 AI 智能体的**元认知可靠性**、**可信性**和**安全性**。

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

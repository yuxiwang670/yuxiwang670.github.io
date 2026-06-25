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

I am **Yuxi Wang (王愉茜)**, a **Ph.D. in Applied Psychology** from **Peking University**. My research investigates **cognitive bias, metacognition, and belief regulation** in human and artificial intelligence.

My previous work examined how humans integrate prior expectations and uncertain evidence to form biased judgments, particularly in social anxiety, using behavioral, computational, and cognitive neuroscience methods. This work shaped my broader interest in how intelligent systems construct beliefs under uncertainty, how those beliefs become biased or calibrated, and how metacognitive processes can regulate judgment and action.

My current and future research extends this perspective to **AI agents**. I study how AI systems form beliefs under uncertainty, monitor their own knowledge and limitations, update beliefs through feedback, and decide when to answer, ask for clarification, seek additional information, or refrain from acting. I am especially interested in **AI cognitive bias**, **metacognitive reliability**, **autonomous learning**, and their implications for **human-AI trust** and **AI safety**.

Methodologically, I combine computational cognitive modeling, Bayesian learning, concept learning, active learning, reinforcement learning, and cognitively grounded benchmark design. My long-term goal is to develop evaluation frameworks and task environments that help us understand, measure, and improve the trustworthiness and safety of autonomous AI agents.

我是**王愉茜**，于**北京大学应用心理学专业**获得博士学位。我的研究关注人类与人工智能中的**认知偏差、元认知与信念调节**。

我过去的研究主要探讨人在先验期待与不确定证据之间如何整合信息，并在此过程中形成带有偏差的判断，尤其关注社交焦虑中的社会认知偏差。这些研究结合行为实验、计算建模与认知神经科学方法，也启发了我进一步思考：智能系统如何在不确定环境中形成信念，这些信念如何变得偏差化或校准化，以及元认知机制如何调节判断与行动。

我目前及未来的研究将这一视角拓展到**AI 智能体**。我关注 AI 系统如何在不确定条件下形成信念，如何监控自身知识与能力边界，如何通过反馈更新信念，并进一步决定何时直接回答、何时主动澄清或寻求信息，以及何时应当暂停或避免行动。我尤其关注 **AI 认知偏差**、**元认知可靠性**、**自主学习**，以及它们对**人机互信**和 **AI 安全**的影响。

在方法上，我结合计算认知建模、贝叶斯学习、概念学习、主动学习、强化学习和具有认知基础的 benchmark 设计。我的长期目标是构建能够帮助我们理解、测量并提升自主 AI 智能体可信性与安全性的评测框架和任务环境。

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

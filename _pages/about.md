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

# Research Overview

<figure class="research-overview">
  <img src="images/research-overview.svg" alt="Research overview diagram linking human cognition and neuroscience to active belief control in autonomous AI agents">
</figure>

# News
- *2026.06*: Homepage profile updated from Google Scholar.
- *2026*: New publications appeared in Nature Human Behaviour, Psychiatry Research: Neuroimaging, and IEEE VR related venues.
- *2025*: Several works on depression, reinforcement learning, multimodal large language models, and intelligent machine simulation were added to Google Scholar.

# Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Brain 2025</div><img src='images/500x300.png' alt="paper thumbnail" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Treatment-resistant recurrent unipolar and bipolar depression: associative learning abnormalities](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:9yKSN-GCB0IC)

S Suveges, **Y Wang**, S Tolomeo, T Gilbertson, JD Steele

**Brain** 148(10), 3705-3717, 2025
- Investigates associative learning abnormalities in treatment-resistant recurrent unipolar and bipolar depression.

<div class="paper-links">
  <a class="paper-link" href="https://doi.org/10.1093/brain/awaf280">PDF</a>
  <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:9yKSN-GCB0IC">Cite</a>
  <a class="paper-link" href="https://doi.org/10.1093/brain/awaf280">DOI</a>
</div>
</div>
</div>

- [Psychodynamic profiles of major depressive disorder and generalized anxiety disorder in China](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:YsMSGLbcyi4C), J Xu, **Y Wang**, Y Peng, **Frontiers in Psychiatry** 15, 1312980, 2024.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/psychodynamic-mdd-gad-2024.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:YsMSGLbcyi4C">Cite</a>
    <a class="paper-link" href="https://doi.org/10.3389/fpsyt.2024.1312980">DOI</a>
  </div>

- [Evaluating multimodal large language models with daily composite tasks in home environments](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:eQOLeE2rZwMC), Z Zhang, **Y Wang**, H Xie, S Zhao, M Liu, Y Lu, X He, Z Cheng, Y Peng, **arXiv:2509.17425**, 2025.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/multimodal-llm-home-tasks-2025.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:eQOLeE2rZwMC">Cite</a>
    <a class="paper-link" href="https://arxiv.org/abs/2509.17425">DOI</a>
  </div>

- [Social functioning in autism: a systematic review and meta-analysis](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:Se3iqnhoufwC), S Li, H Wang, G Chen, X Cheng, **Y Wang**, W Hu, A Hamilton, L Schilbach, et al., **Nature Human Behaviour**, 2026.
  <div class="paper-links">
    <a class="paper-link" href="https://doi.org/10.1038/s41562-026-02457-w">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:Se3iqnhoufwC">Cite</a>
    <a class="paper-link" href="https://doi.org/10.1038/s41562-026-02457-w">DOI</a>
  </div>

- [Distinct neural signatures of reward processing underlying bipolar disorder and major depressive disorder: a systematic review and meta-analysis](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:roLk4NBRz8UC), **Y Wang**, Y Peng, JD Steele, S Tolomeo, **Psychiatry Research: Neuroimaging**, 112196, 2026.
  <div class="paper-links">
    <a class="paper-link" href="https://doi.org/10.1016/j.pscychresns.2026.112196">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:roLk4NBRz8UC">Cite</a>
    <a class="paper-link" href="https://doi.org/10.1016/j.pscychresns.2026.112196">DOI</a>
  </div>

- [Revisiting Resting-State Functional Connectivity of the Amygdala and Subgenual Anterior Cingulate Cortex in Adolescents and Adults With Depression](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:UeHWp8X0CEIC), S Fan, **Y Wang**, Y Wang, Y Zang, **Biological Psychiatry: Cognitive Neuroscience and Neuroimaging** 10(7), 759-768, 2025.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/resting-state-fc-depression-2025.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:UeHWp8X0CEIC">Cite</a>
    <a class="paper-link" href="https://doi.org/10.1016/j.bpsc.2024.11.004">DOI</a>
  </div>

- [贝叶斯框架下社交焦虑的社会认知特性](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:Tyk-4Ss8FVUC), 彭玉佳, **王愉茜**, 鞠芊芊, 刘峰, 徐佳, **心理科学进展** 33(8), 1267-1274, 2025.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/bayesian-social-anxiety-2025.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:Tyk-4Ss8FVUC">Cite</a>
    <a class="paper-link" href="https://doi.org/10.3724/SP.J.1042.2025.1267">DOI</a>
  </div>

- [基于生物运动的社交焦虑者情绪加工与社会意图理解负向偏差机制](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:IjCSPb-OGe4C), 彭玉佳, **王愉茜**, 路迪, **心理科学进展** 31(6), 905-914, 2023.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/biomotion-social-anxiety-2023.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:IjCSPb-OGe4C">Cite</a>
    <a class="paper-link" href="https://doi.org/10.3724/SP.J.1042.2023.00905">DOI</a>
  </div>

- [成人社交焦虑问卷中文版的效度和信度评价](https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:2osOgNQ5qMEC), **王愉茜**, 臧寅垠, 彭玉佳, **Chinese Mental Health Journal / 中国心理卫生杂志** 38(8), 730-736, 2024.
  <div class="paper-links">
    <a class="paper-link" href="assets/pdfs/sad-questionnaire-cn-2024.pdf">PDF</a>
    <a class="paper-link" href="https://scholar.google.com/citations?view_op=view_citation&hl=zh-CN&user=8F7li3AAAAAJ&citation_for_view=8F7li3AAAAAJ:2osOgNQ5qMEC">Cite</a>
    <a class="paper-link" href="https://doi.org/10.3969/j.issn.1000-6729.2024.08.015">DOI</a>
  </div>

# Honors and Awards
- *2024*, Scientific Research Award, School of Psychological and Cognitive Sciences, Peking University.
- *2024*, Three-class Scholarship, School of Psychological and Cognitive Sciences, Peking University.
- *2023*, Three-class Scholarship, School of Psychological and Cognitive Sciences, Peking University.
- *2019*, Departmental Distinction in Biomedical Engineering, University of Dundee.
- *2019*, Best Students & Best Project, University of Dundee.
- *2018 - 2019*, Scholarship for Master's Degree, China Scholarship Council.
- *2018*, Alumni Scholarship, University of Dundee.
- *2017 - 2018*, Scholarship for Outstanding Undergraduate Exchange, China Scholarship Council.
- *2015, 2016, 2017*, People's Third-class Scholarship, University of Science and Technology Beijing.
- *2015*, National Encouragement Scholarship, University of Science and Technology Beijing.

# Educations
- *2022 - present*, **Ph.D. candidate, Applied Psychology**, Peking University, Beijing, China.
- *2018 - 2019*, **M.Sc. with Distinction, Biomedical Engineering**, University of Dundee, Dundee, UK.
- *2014 - 2018*, **B.Sc., Biotechnology**, University of Science and Technology Beijing, Beijing, China.

# Invited Talks
- Workshops, summer schools, and academic training activities since 2017.

# Internships
- *2019 - 2022*, Research Assistant in Applied Psychology, Peking University, Beijing, China.
- *2014 - 2018*, Undergraduate internships and B.Sc. training, University of Science and Technology Beijing, Beijing, China.

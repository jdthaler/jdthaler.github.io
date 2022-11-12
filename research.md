---
layout: article
title: Research Topics
aside:
  toc: true
---


{% for topic in site.data.research.topics %}
### {{topic.title}}
{% for paper in site.data.cv_papers.papers %}
{% if topic.key == paper.topic%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}})
{% endif %}
{% endfor%}
{% endfor%}

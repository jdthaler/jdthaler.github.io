---
layout: article
title: Research Topics
aside:
  toc: true
---

{% for theme in site.data.research.themes %}
## {{theme.title}} {#{{theme.key}}}
{% endfor %}

{% for topic in site.data.research.topics %}
## {{topic.title}}

{% for subtopic in topic.subtopics %}
### {{subtopic.title}}
{% if subtopic.description %} {{subtopic.description}} {% endif %}

{% for paper in site.data.cv_papers.papers %}
{% if subtopic.key == paper.topic%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}})
{% endif %}

{% endfor%}
{% endfor%}
{% endfor%}

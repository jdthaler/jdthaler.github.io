---
layout: article
title: Research Topics
aside:
  toc: true
---

[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill}

{% for topic in site.data.research.topics %}
## {{topic.title}} {#{{topic.key}}}

### Key Papers

{% for paper in site.data.cv_papers.papers -%}
{%- for subtopic in topic.subtopics -%}
{%- if subtopic.key == paper.topic -%}
  {%- if paper.priority >= 6 %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** \\
        *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
  {%- endif -%}
{%- endif -%}
{%- endfor %}
{%- endfor %}


### Subtopics


{% for subtopic in topic.subtopics %}
<details markdown="1">

<summary><b>{{subtopic.title}}</b></summary>

{% for paper in site.data.cv_papers.papers -%}
{% if subtopic.key == paper.topic %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** {% if paper.priority >= 6 %}`recommended`{:.success}{% endif %} \\
    *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
{%- endif %}
{%- endfor%}

</details>
{% endfor %}

{% endfor %}

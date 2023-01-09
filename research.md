---
layout: article
title: Research
aside:
  toc: true
---

[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill}

{% for topic in site.data.research.topics %}
## {{topic.title}} {#{{topic.key}}}

### Selected Papers

{% for paper in site.data.cv_papers.papers -%}
{%- for subtopic in topic.subtopics -%}
{%- if subtopic.key == paper.topic -%}
  {%- if paper.priority >= 5 %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** \\
        *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
  {%- endif -%}
{%- endif -%}
{%- endfor %}
{%- endfor %}


### Research Topics


{% for subtopic in topic.subtopics %}
<details markdown="1">

<summary><b>{{subtopic.title}}</b></summary>

{% for paper in site.data.cv_papers.papers -%}
{% if subtopic.key == paper.topic %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** {% if paper.priority >= 3 %}`recommended`{:.success}{% endif %} \\
    *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
{%- endif %}
{%- endfor%}

</details>
{% endfor %}

{% endfor %}

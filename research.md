---
layout: article
title: Research
aside:
  toc: true
---

<center>
<img class="image-h image-h--xl rounded" src="images/stamp_research.jpg" title="Jesse Thaler"/>
</center>

<br>

[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--outline-primary.button--pill}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--outline-primary.button--pill}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--outline-primary.button--pill}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--outline-primary.button--pill}

{% for topic in site.data.research.topics %}
## {{topic.title}} {#{{topic.key}}}

<center>
<div>
<img class="image-h image-h--xl rounded" src="{{topic.image}}" title="{{topic.title}}"/>
</div>
</center>

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

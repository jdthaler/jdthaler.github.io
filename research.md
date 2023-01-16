---
layout: article
title: Research
aside:
  toc: true
---

<center>
{% assign topimage = site.data.images.research[0] %}
<img class="image-h image-h--xl rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</center>

The goal of my research in theoretical particle physics is galvanize the search for new phenomena beyond the Standard Model as well as to illuminate the structure of the Standard Model itself.  In my research, I often combine first-principles calculations in quantum field theory with data analysis techniques from machine learning.

[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill.button--sm}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--outline-primary.button--pill.button--sm}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--outline-primary.button--pill.button--sm}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--outline-primary.button--pill.button--sm}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--outline-primary.button--pill.button--sm}

{% for topic in site.data.research.topics %}
## {{topic.title}} {#{{topic.key}}}

<center>
<a href="{{topic.image_url}}">
<img class="image-h image-h--xl rounded" src="{{topic.image}}" title="{{topic.title}}"/>
</a>
</center>

{{topic.description}}

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

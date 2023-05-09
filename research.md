---
layout: article
title:  Research in Theoretical Physics
aside:
  toc: true
---


{% assign topimage = site.data.research.research_top %}

<style>
  .hero-example--linear-gradient {
    background-image: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.5)), url("{{topimage.image}}");
  }
  .smooth-tag {
    scroll-behavior: smooth;
  }
</style>

<div class="hero hero--dark hero-example--linear-gradient">
<div class="hero__content px-4  py-2" style="text-align: right;">
{% for topic in site.data.research.topics %}
<div markdown="1"  style="align: right;">
[{{topic.title}}](#{{topic.key}}){:.button.button--theme-dark.button--pill.button--lg.smooth-tag}
</div>
{%- endfor %}
</div>
</div>

{{topimage.description}}

[Publications by Year](cv#publications--preprints){:.button.button--secondary.button--pill.button--sm}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

{% for topic in site.data.research.topics %}

<h3>&nbsp;</h3>

## {{topic.title}} {#{{topic.key}}}

<div class="item">
<div class="item__image">
<a href="{{topic.image_url}}" target="_blank">
<img class="image-96--xl" src="{{topic.image}}" title="{{topic.title}}"/>
</a>
</div>
<div class="item__content">
{{topic.description}}
</div>
</div>


### Selected Papers

{% for paper in site.data.papers.papers -%}
{%- for subtopic in topic.subtopics -%}
{%- if subtopic.key == paper.topic -%}
  {%- if paper.priority >= 5 %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}}){:target="_blank"}** \\
        *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){:target="_blank"}{% endif %}*
  {%- endif -%}
{%- endif -%}
{%- endfor %}
{%- endfor %}


### Research Topics


{% for subtopic in topic.subtopics %}
<details markdown="1">

<summary><b>{{subtopic.title}}</b></summary>

{% for paper in site.data.papers.papers -%}
{% if subtopic.key == paper.topic %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}}){:target="_blank"}** {% if paper.priority >= 3 %}`recommended`{:.success}{% endif %} \\
    *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){:target="_blank"}{% endif %}*
{%- endif %}
{%- endfor%}

</details>
{% endfor %}

{% endfor %}

<h3>&nbsp;</h3>

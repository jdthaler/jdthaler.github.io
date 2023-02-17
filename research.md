---
layout: article
title: Research
aside:
  toc: true
---


{% assign topimage = site.data.research.research_top %}

<div class="item">
<div class="item__image">
<img class="image-sq--lg rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</div>
<div class="item__content">
{{topimage.description}}
  </div>
</div>

<!--<style>
  .hero-example--linear-gradient {
    background-image: linear-gradient(135deg, rgba(0, 0, 0, .5), rgba(0, 0, 0, .25)), url("{{topimage.image}}");
  }
</style>

<div class="hero hero--dark hero-example--linear-gradient">
  <div class="hero__content">
    <h3>{{topimage.title}}</h3>
  </div>
</div>

{{topimage.description}}-->


[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill.button--sm}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--outline-primary.button--pill.button--sm}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--outline-primary.button--pill.button--sm}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--outline-primary.button--pill.button--sm}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--outline-primary.button--pill.button--sm}





{% for topic in site.data.research.topics %}

## {{topic.title}} {#{{topic.key}}}


<!--<style>
  .hero-example--{{topic.key}} {
    background-image: linear-gradient(135deg, rgba(0, 0, 0, .5), rgba(0, 0, 0, .25)), url("{{topic.image}}");
  }
</style>

<div class="hero hero--dark hero-example--{{topic.key}}">
  <div class="hero__content" markdown=1>
### {{topic.title}} {#{{topic.key}}}
  <p>{{topic.description}}</p>
  </div>
</div>-->



<div class="item">
<div class="item__image">
<a href="{{topic.image_url}}">
<img class="image-96--xl rounded" src="{{topic.image}}" title="{{topic.title}}"/>
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

{% for paper in site.data.papers.papers -%}
{% if subtopic.key == paper.topic %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** {% if paper.priority >= 3 %}`recommended`{:.success}{% endif %} \\
    *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
{%- endif %}
{%- endfor%}

</details>
{% endfor %}

{% endfor %}

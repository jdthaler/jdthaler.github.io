---
layout: article
title: Research Topics
aside:
  toc: true
---

[Research in Detail](research_detail){:.button.button--outline-primary.button--pill}
[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill}

{% for topic in site.data.research.topics %}
## {{topic.title}} {#{{topic.key}}}

#### Key Papers

{% for paper in site.data.cv_papers.papers -%}
{%- for subtopic in topic.subtopics -%}
{%- if subtopic.key == paper.topic -%}
  {%- if paper.priority >= 6 %}
  * **[{{paper.title}}](https://doi.org/{{paper.doi}})**, *{{paper.authors}} ({{paper.year}})* 
  {%- endif -%}
{%- endif -%}
{% endfor %}
{% endfor %}


#### Additional Topics

{% for subtopic in topic.subtopics %}
  * [{{subtopic.title}}](research_detail#{{subtopic.key}})
{% endfor %}

{% endfor %}

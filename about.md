---
layout: article
title: Jesse Thaler
aside:
  toc: true
---

{% assign topimage = site.data.bio.about_top %}

<div class="item">
<div class="item__image">
<img class="image-h image-h--lg rounded" src="{{topimage.image}}" title="{{topimage.hover}}" align="left"/>
</div>
<div class="item__content" markdown="1">
  I am a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics. My current research is focused on maximizing the discovery potential of the Large Hadron Collider through new theoretical frameworks and novel data analysis techniques. I joined the MIT Physics Department in 2010, and I am currently a Professor in the Center for Theoretical Physics. In 2020, I became the inaugural Director of the NSF Institute for Artificial Intelligence and Fundamental Interactions.
  </div>
</div>

[Personal Page](personal){:.button.button--outline-primary.button--pill.button--sm}
[Press Information](press){:.button.button--outline-primary.button--pill.button--sm}
[MIT Physics Page](http://web.mit.edu/physics/people/faculty/thaler_jesse.html){:.button.button--outline-primary.button--pill.button--sm}
[Wikipedia](https://en.wikipedia.org/wiki/Jesse_Thaler){:.button.button--outline-primary.button--pill.button--sm}
[Full CV](cv){:.button.button--outline-primary.button--pill.button--sm}

## Education

  * **Harvard University**, Ph.D. Physics, *2006*
  * **Brown University**, Sc.B. Math/Physics, *2002*

## Key Positions

  * **Massachusetts Institute of Technology**
      * Professor of Physics, *2021 - Present*
      * Associate Professor of Physics, *2015 - 2021 (tenured in 2017)*
      * Assistant Professor of Physics, *2010 - 2015*
  * **NSF Institute for Artificial Intelligence and Fundamental Interactions**
      * Director, *2020 - Present*
  * **University of California, Berkeley**
      * Miller Research Fellow, *2006 - 2009*

<!--
### Affilations

{% for affiliation in site.data.bio.affiliations %}
  * **{{affiliation.name}}**
{%- endfor %}
-->

## Selected Awards

{% for award in site.data.bio.awards -%}
  {%- if award.priority >= 6 %}
  * **{{award.name}}**, *{{award.org}}*, *{{award.date}}*
  {%- endif -%}
{% endfor %}

## Selected Publications

[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--outline-primary.button--pill.button--sm}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--outline-primary.button--pill.button--sm}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--outline-primary.button--pill.button--sm}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--outline-primary.button--pill.button--sm}

{% for paper in site.data.papers.papers -%}
  {%- if paper.priority >= 6 %}
  * **[{{paper.title}}](https://arxiv.org/abs/{{paper.arxiv}})** \\
    *{{paper.authors}}{% if paper.doi %}, [{{paper.short_journal | default: "DOI" }}](https://doi.org/{{paper.doi}}){% endif %}*
  {%- endif -%}
{% endfor %}

## In the News

<details markdown=1>
<summary><b>Profiles and Highlights</b></summary>

{% for news in site.data.news.profiles -%}
  * "[{{news.title}}]({{news.url}})", *{{news.journal}}, {{news.date}}*
{% endfor %}

</details>


<details markdown=1>
<summary><b>Awards and Honors</b></summary>

{% for news in site.data.news.awards -%}
  * **{{news.short}}**:  "[{{news.title}}]({{news.url}})", *{{news.journal}}, {{news.date}}*
{% endfor %}

</details>


<details markdown=1>
<summary><b>Quotations and Perspectives</b></summary>

{% for news in site.data.news.perspectives -%}
  * "[{{news.title}}]({{news.url}})", *{{news.journal}}, {{news.date}}*
{%- if news.quote %}
  > *{{news.quote}}*
{%- endif %}
{% endfor %}



</details>


<details markdown=1>
<summary><b>Group Members in the News</b></summary>

{% for news in site.data.news.group_news -%}
  * **{{news.person}}**:  "[{{news.title}}]({{news.url}})", *{{news.journal}}, {{news.date}}*
{% endfor %}

</details>

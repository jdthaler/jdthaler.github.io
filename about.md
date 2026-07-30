---
layout: article
title: Jesse Thaler
aside:
  toc: true
permalink: /about/
---

{% assign topimage = site.data.bio.about_top %}

<div class="item">
<div class="item__image">
<img class="image-h image-h--lg rounded" src="{{topimage.image}}" alt="{{topimage.alt}}" title="{{topimage.hover}}" align="left"/>
</div>
<div class="item__content" markdown="1">
  I am a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics. My current research is focused on maximizing the discovery potential of the Large Hadron Collider through new theoretical frameworks and novel data analysis techniques. I joined the MIT Physics Department in 2010, and I am currently a Professor in the MIT Center for Theoretical Physics - a Leinweber Institute. From 2020 to 2025, I was the inaugural Director of the NSF Institute for Artificial Intelligence and Fundamental Interactions.  Starting in 2026, I will direct the MIT Laboratory for Nuclear Science.
  </div>
</div>

[Personal Page](/personal){:.button.button--secondary.button--pill.button--sm}
[Press Information](/press){:.button.button--secondary.button--pill.button--sm}
[Full CV](/cv){:.button.button--secondary.button--pill.button--sm}
[MIT Physics Page](https://web.mit.edu/physics/people/faculty/thaler_jesse.html){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Wikipedia](https://en.wikipedia.org/wiki/Jesse_Thaler){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}


## Key Positions

{% for place in site.data.bio.employment %}{% if place.current and place.priority >= 6 %}  * **{{place.name}}**
{% for role in place.roles %}{% if role.priority >= 6 %}      * {{role.title}}, *{% assign _d = role.dates | default: place.dates %}{% include snippets/years-from-dates.html dates=_d %}{{__return}}{% if role.note %} ({{role.note}}){% endif %}*
{% endif %}{% endfor %}{% endif %}{% endfor %}{% for role in site.data.bio.leadership %}  * **{{role.name}}**
      * {{role.role}}, *{% include snippets/years-from-dates.html dates=role.dates %}{{__return}}*
{% endfor %}{% for place in site.data.bio.employment %}{% unless place.current %}{% if place.priority >= 6 %}  * **{{place.name}}**
{% for role in place.roles %}{% if role.priority >= 6 %}      * {{role.title}}, *{% assign _d = role.dates | default: place.dates %}{% include snippets/years-from-dates.html dates=_d %}{{__return}}{% if role.note %} ({{role.note}}){% endif %}*
{% endif %}{% endfor %}{% endif %}{% endunless %}{% endfor %}


## Education

{% for school in site.data.about.education -%}
{% for degree in school.degrees -%}
  {%- if degree.priority >= 6 %}
  * **{{school.org}}**, {{degree.type}} {{degree.field}}, {{degree.year}}
  {%- endif -%}
{% endfor %}{% endfor %}

## Selected Awards

{% for award in site.data.bio.awards -%}
  {%- if award.priority >= 6 %}
  * **{{award.name}}**, *{{award.org}}*, *{{award.date}}*
  {%- endif -%}
{% endfor %}

## Selected Publications

[Inspire](https://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[arXiv](https://arxiv.org/a/thaler_j_1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

{% for paper in site.data.papers.papers -%}
  {%- if paper.priority >= 6 %}
  * {% include cv/paper_short_item.html paper = paper %}
  {%- endif -%}
{% endfor %}

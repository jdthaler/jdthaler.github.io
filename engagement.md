---
layout: article
title: Public Engagement
aside:
  toc: true
permalink: engagement/
---

{% assign topimage = site.data.public.public_top %}

<style>
  .hero-example--linear-gradient {
    background-image: linear-gradient(90deg, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.3)), url("{{topimage.image}}");
    background-position: top;
  }
</style>

<div class="hero hero--dark hero-example--linear-gradient">
<div class="hero__content px-4 py-2" style="text-align: right;">
{% for topic in site.data.public.topics %}
<div markdown="1">
[{{topic.title}}](#{{topic.key}}){:.button.button--theme-dark.button--pill.button--lg}
</div>
{%- endfor %}
</div>
</div>


{{topimage.description}}

[Engagement CV](/cv#public-engagement){:.button.button--secondary.button--pill.button--sm}


{% for topic in site.data.public.topics %}

<h3>&nbsp;</h3>

## {{topic.title}} {#{{topic.key}}}

<div class="item">
<div class="item__image">
<a href="{{topic.image_url}}" target="_blank">
<img class="image-sq--lg" src="{{topic.image}}" title="{{topic.image_hover}}"/>
</a>
</div>
<div class="item__content" markdown=1>
{% for subtopic in topic.subtopics -%}
{%- for entry in site.data.public.entries -%}
{%- if subtopic.key == entry.topic %}
  * {{entry.markdown}}
{%- endif -%}
{%- endfor -%}
{%- endfor %}
</div>
</div>

{%- endfor %}

<h3>&nbsp;</h3>

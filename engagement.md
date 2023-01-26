---
layout: article
title: Public Engagement
aside:
  toc: true
---

{% assign topimage = site.data.public.public_top %}

<div class="item">
<div class="item__image">
<a href="{{topimage.image_url}}">
<img class="image-h image-h--lg rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</a>
</div>
<div class="item__content" markdown=1>
{{topimage.description}}
  </div>
</div>


[Engagement CV](cv#public-engagement){:.button.button--outline-primary.button--pill.button--sm}


{% for topic in site.data.public.topics %}
## {{topic.title}} {#{{topic.key}}}

<div class="item">
<div class="item__image">
<a href="{{topic.image_url}}">
<img class="image-h image-h--lg rounded" src="{{topic.image}}" title="{{topic.image_hover}}"/>
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

<!--{{topic.description}}-->
<!--### {{subtopic.title}}-->
<!--   {%- if entry.description %}-->
<!--     > {{entry.description}} {% endif -%}-->



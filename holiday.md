---
layout: article
title: Holiday Cards
aside:
  toc: true
permalink: holiday/
---

Click any image for a high resolution version!
{% for card in site.data.holiday.cards %}
## {{card.year}}
{%- assign _front = '/holiday/' | append: card.file | append: '_front.jpg' -%}
{%- assign _back = '/holiday/' | append: card.file | append: '_back.jpg' %}

<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--8">
      <center>
      <a href="{{_front}}">
        <img class="image-h image-h--xl" style="object-fit: contain" src="{% include snippets/get-preview-url.html url=_front %}{{__return}}" alt="{{card.year}} holiday card, front" title="{{card.year}} Front"/>
      </a>
      </center>
    </div>
{%- if card.back %}
    <div class="cell cell--4">
      <center>
      <a href="{{_back}}">
        <img class="image-h image-h--xl" style="object-fit: contain" src="{% include snippets/get-preview-url.html url=_back %}{{__return}}" alt="{{card.year}} holiday card, back" title="{{card.year}} Back"/>
      </a>
      </center>
    </div>
{%- endif %}
  </div>
</div>
{% endfor %}
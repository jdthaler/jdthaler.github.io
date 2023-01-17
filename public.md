---
layout: article
title: Public Engagement
aside:
  toc: true
---

<center>
{% assign topimage = site.data.public.public_top %}
<a href="{{topimage.image_url}}">
<img class="image-h image-h--xl rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</a>
</center>
{{topimage.description}}

[Engagement CV](cv#public-engagement){:.button.button--outline-primary.button--pill.button--sm}


{% for topic in site.data.public.topics %}
## {{topic.title}} {#{{topic.key}}}

<center>
<a href="{{topic.image_url}}">
<img class="image-h image-h--xl rounded" src="{{topic.image}}" title="{{topic.image_hover}}"/>
</a>
</center>

{% for subtopic in topic.subtopics %}

### {{subtopic.title}}

{% for entry in site.data.public.entries -%}
{%- if subtopic.key == entry.topic %}
  * {{entry.markdown}}
    {%- if entry.description %}
     > {{entry.description}} {% endif -%}
{%- endif -%}
{%- endfor %}

{% endfor %}

{% endfor %}



## Graphic Design

[Design CV](cv#graphic-design){:.button.button--outline-primary.button--pill.button--sm}

### Logos

<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--3">
          <a href="design/jthaler_IAIFI_Logo.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_IAIFI_Logo.png" title="IAIFI Logo"/>
          <br>
              <b>IAIFI</b>
          </a>
    </div>
    <div class="cell cell--3">
          <a href="design/jthaler_OmniFold_Logo.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_OmniFold_Logo.png" title="OmniFold Logo"/>
          <br>
              <b>OmniFold</b>
          </a>
    </div>
    <div class="cell cell--3">
          <a href="design/jthaler_MOD_Logo.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_MOD_Logo.png" title="MOD"/>
          <br>
              <b>MOD</b>
          </a>
    </div>
    <div class="cell cell--3">
          <a href="design/jthaler_DarkLight_Logo.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_DarkLight_Logo.png" title="DarkLight Logo"/>
          <br>
              <b>DarkLight</b>
          </a>
    </div>
    <div class="cell cell--6">
          <a href="design/jthaler_ABRALogo_Large.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_ABRALogo_Large.png" title="ABRACADABRA"/>
          <br>
              <b>ABRACADABRA</b>
          </a>
    </div>
    <div class="cell cell--3">
          <a href="design/jthaler_ABRALogo_Medium.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_ABRALogo_Medium.png" title="ABRA"/>
          <br>
              <b>ABRA</b>
          </a>
    </div>
    <div class="cell cell--3">
          <a href="design/jthaler_ABRALogo_Small.pdf">
            <img class="image-h image-h--xs" src="design/jthaler_ABRALogo_Small.png" title="A."/>
          <br>
              <b>A.</b>
          </a>
    </div>
  </div>
</div>


### Images


<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--4">
          <a href="design/jthaler_IAIFI_Banner.jpg">
            <img class="image-h image-h--sm" src="design/jthaler_IAIFI_Banner.jpg" title="[IAIFI Banner"/>
          <br>
              <b>IAIFI Banner</b>
          </a>
    </div>
    <div class="cell cell--4">
          <a href="design/jthaler_MOD_EventDisplay.pdf">
            <img class="image-h image-h--sm" src="design/jthaler_MOD_EventDisplay.png" title="MOD Event"/>
          <br>
              <b>MOD Event Display</b>
          </a>
    </div>
    <div class="cell cell--4">
          <a href="design/jthaler_BOOST2019_Poster.pdf">
            <img class="image-h image-h--sm" src="design/jthaler_BOOST2019_Poster.png" title="BOOST 2019 Poster"/>
          <br>
              <b>BOOST 2019 Poster</b>
          </a>
    </div>

  </div>
</div>


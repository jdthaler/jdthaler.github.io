---
layout: article
title: Press Information
aside:
  toc: true
permalink: press/
---

## Photographs

<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--6">
          <a href="/images/jthaler_mit_spotlight.jpg">
            <img class="image-h image-h--sm" src="/images/preview/jthaler_mit_spotlight.jpg" alt="" title="Thaler Blackboard Shot"/>
          <br>
              <b>Blackboard Shot</b>
          </a>
          <br>
          <a href="/images/jthaler_mit_spotlight_large_uncropped.jpg">Full resolution</a> (uncropped)
    </div>
    
    <div class="cell cell--6">
          <a href="/images/jthaler_photo_2017.jpg">
            <img class="image-h image-h--sm" src="/images/preview/jthaler_photo_2017.jpg" alt="" title="Thaler Head Shot"/>
          <br>
              <b>Head Shot</b>
          </a>
          <br>
          <a href="/images/jthaler_photo_2017_large_uncropped.jpg">Full resolution</a> (uncropped)
    </div>
  </div>
</div>


##   Biography

{{ site.data.bio.blurbs.short }}

## Extended Biography

### Research Interests

{{ site.data.bio.blurbs.research_interests }}

### Biographical Sketch

{{ site.data.bio.blurbs.biographical_sketch }}

### Links to Additional Information

[About](/about){:.button.button--secondary.button--pill.button--sm}
[Full CV](/cv){:.button.button--secondary.button--pill.button--sm}
[MIT Physics Page](https://web.mit.edu/physics/people/faculty/thaler_jesse.html){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Wikipedia](https://en.wikipedia.org/wiki/Jesse_Thaler){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

## Image Credits

{% assign frontimage = site.data.bio.index_top %}
{% assign aboutimage = site.data.bio.about_top %}
{% assign publicimage = site.data.public.public_top %}
{% assign researchimage = site.data.research.research_top %}
{% assign personalimage = site.data.bio.personal_top %}

  * [![{{frontimage.hover}}]({% include snippets/get-preview-url.html url=frontimage.image %}{{__return}}){:.image--xs}]({{frontimage.image}}) Front Page: {% if frontimage.image_url %}[{{frontimage.image_credit}}]({{frontimage.image_url}}){% else %}{{frontimage.image_credit}}{% endif %}
  * [![{{aboutimage.hover}}]({% include snippets/get-preview-url.html url=aboutimage.image %}{{__return}}){:.image--xs}]({{aboutimage.image}}) About Page: {% if aboutimage.image_url %}[{{aboutimage.image_credit}}]({{aboutimage.image_url}}){% else %}{{aboutimage.image_credit}}{% endif %}
  * [![{{researchimage.hover}}]({% include snippets/get-preview-url.html url=researchimage.image %}{{__return}}){:.image--xs}]({{researchimage.image}}) Research Page: {% if researchimage.image_url %}[{{researchimage.image_credit}}]({{researchimage.image_url}}){% else %}{{researchimage.image_credit}}{% endif %}
{% for topic in site.data.research.topics -%}
  * [![{{topic.title}}]({% include snippets/get-preview-url.html url=topic.image %}{{__return}}){:.image--xs}]({{topic.image}}) Research, {{topic.title}}: {% if topic.image_url %}[{{topic.image_credit}}]({{topic.image_url}}){% else %}{{topic.image_credit}}{% endif %}
{% endfor -%}
  * [![{{publicimage.hover}}]({% include snippets/get-preview-url.html url=publicimage.image %}{{__return}}){:.image--xs}]({{publicimage.image}}) Public Engagement Page: {% if publicimage.image_url %}[{{publicimage.image_credit}}]({{publicimage.image_url}}){% else %}{{publicimage.image_credit}}{% endif %}
{% for topic in site.data.public.topics -%}
  * [![{{topic.title}}]({% include snippets/get-preview-url.html url=topic.image %}{{__return}}){:.image--xs}]({{topic.image}}) Public Engagement, {{topic.title}}: {% if topic.image_url %}[{{topic.image_credit}}]({{topic.image_url}}){% else %}{{topic.image_credit}}{% endif %}
{% endfor -%}
{%- comment -%}
These two are flush left, unlike the indented entries above. The loop just
closed ends with `-%}`, which eats the newline, so a following indented
bullet is read as a sublist of the last item rather than a sibling.
Indenting these to match would silently nest them.
{%- endcomment -%}
{% for address in site.data.about.addresses -%}
* [![{{address.hover}}]({% include snippets/get-preview-url.html url=address.image %}{{__return}}){:.image--xs}]({{address.image}}) Contact Page, {{address.org}}: {% if address.image_url %}[{{address.image_credit}}]({{address.image_url}}){% else %}{{address.image_credit}}{% endif %}
{% endfor -%}
* [![{{personalimage.hover}}]({% include snippets/get-preview-url.html url=personalimage.image %}{{__return}}){:.image--xs}]({{personalimage.image}}) Personal Page: {% if personalimage.image_url %}[{{personalimage.image_credit}}]({{personalimage.image_url}}){% else %}{{personalimage.image_credit}}{% endif %}

---
layout: article
title: Research Group
aside:
  toc: true

---

Great ideas can come from researchers at any career stage, so I strive to cultivate a collaborative atmosphere in my group while also providing individual mentorship.  We pursue a broad range of research in theoretical particle physics, and we often find connections to adjacent fields.  


[Mentoring CV](cv#mentoring){:.button.button--outline-primary.button--pill.button--sm}
[Joining My Group](join){:.button.button--outline-primary.button--pill.button--sm}

## Current

{% for category in site.data.cv_mentoring.categories -%}
### {{category.name}}

<div class="grid-container">
  <div class="grid grid--py-3">

{% for person in site.data.cv_mentoring[category.block] -%}
  {% if person.current -%}
    <div class="cell cell--3">
          {% if person.url %} <a href="{{person.url}}">{% endif%} 
          <img class="image image--sm image-h--sm rounded" style="object-fit:cover" src="{{person.image | default: "images/blank_profile.png"}}" title="{{person.name}}"/><br>
              <b>{{person.name}}</b>
          {% if person.url %} </a>{% endif%} 
    </div>
  {%- endif %}
{% endfor %}
  </div>
</div>

{% endfor %}


## Alumni


{% for category in site.data.cv_mentoring.categories -%}
### {{category.name}}

{% for person in site.data.cv_mentoring[category.block] -%}
  {% if person.current -%}{% else -%}
    {% if person.url %}* **[{{person.name}}]({{person.url}})**{% else %}* **{{person.name}}**{% endif %}
  {%- endif %}
{% endfor %}
{% endfor %}






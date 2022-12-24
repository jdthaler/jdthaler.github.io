---
layout: article
title: Research Group
aside:
  toc: true

---


## Current


{% for category in site.data.cv_mentoring.categories -%}
### {{category.name}}

<div class="grid-container">
  <div class="grid grid--py-3">

{% for person in site.data.cv_mentoring[category.block] -%}
  {% if person.current -%}
    <div class="cell cell--3">
        <center>
          <img class="image image--sm" src="images/blank_profile.png" title="{{person.name}}"/><br>
              <b>{{person.name}}</b><br>
        </center>
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
  * **{{person.name}}**
  {%- endif %}
{% endfor %}
{% endfor %}






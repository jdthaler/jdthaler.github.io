---
layout: article
title: Research Group
aside:
  toc: true

---


## Current

<div class="grid-container">
  <div class="grid grid--py-3">
{% for category in site.data.cv_mentoring -%}
{% for person in category[1] -%}
  {% if person.current -%}
    <div class="cell cell--4">
        <center>
          <img class="image image--sm" src="design/jthaler_IAIFI_Logo.png" title="{{person.name}}"/><br>
              <b>{{person.name}}</b><br>
        </center>
    </div>
  {%- endif %}
{% endfor %}
{% endfor %}
  </div>
</div>

## Alumni

<div class="grid-container">
  <div class="grid grid--py-3">
{% for category in site.data.cv_mentoring -%}
{% for person in category[1] -%}
  {% if person.current -%}{% else %}
    <div class="cell cell--4">
        <center>
              <b>{{person.name}}</b>
        </center>
    </div>
  {%- endif %}
{% endfor %}
{% endfor %}
  </div>
</div>







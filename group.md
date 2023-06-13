---
layout: article
title: Research Group
aside:
  toc: true
permalink: group/
---

{% assign topimage = site.data.mentoring.group_top %}
{{topimage.description}} 


[Joining My Group](join){:.button.button--secondary.button--pill.button--sm}
[Mentoring CV](cv#mentoring){:.button.button--secondary.button--pill.button--sm}
[MIT Physics Community Values](https://physics.mit.edu/about-physics/community-values/){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}


{% for category in site.data.mentoring.current_categories -%}
## {{category.name}}

<div class="grid-container">
  <div class="grid grid--p-2">

{% for block in category.blocks -%}
{% for person in site.data.mentoring[block] -%}
  {% if person.current -%}
    <div class="cell cell--3">
          {% if person.url %} <a href="{{person.url}}" target="_blank">{% endif%} 
          <img class="image image-sq--sm rounded" src="{{person.image | default: "/images/blank_profile.png"}}" title="{{person.name}}"/><br>
              <b>{{person.name}}</b>
          {% if person.url %} </a>{% endif%} 
    </div>
  {%- endif %}
{% endfor %}
{% endfor %}
  </div>
</div>

{% endfor %}


## Alumni


{% for category in site.data.mentoring.alumni_categories -%}
<details markdown=1>
<summary><b>{{category.name}}</b></summary>

{% for person in site.data.mentoring[category.block] -%}
  {% if person.current -%}{% else -%}
    {% if person.url %}* **[{{person.name}}]({{person.url}}){:target="_blank"}**{% else %}* **{{person.name}}**{% endif %}
    {%- if person.after[0] %}, {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
  {%- endif %}
{% endfor %}

</details>
{% endfor %}






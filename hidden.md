---
layout: article
title: Hidden Information
aside:
  toc: true
---

## Email Lists

### Current Email List

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- if person.email and person.current %}{{person.email}}, {% endif -%}
{%- endfor -%}
{%- endfor %}

### Email Lists for Remaining 2023

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- unless person.updated == 2023 or person.deceased or person.email == nil %}{{person.email}}, {% endunless %}
{%- endfor -%}
{%- endfor %}


### Missing Email List

{% for category in site.data.mentoring.alumni_categories %}
{% for person in site.data.mentoring[category.block] -%}
{%- if person.email %}{% else %}{{person.name}}{% endif -%}
{% endfor %}
{% endfor %}


### Full Email List

{% for category in site.data.mentoring.alumni_categories %}
{%- for person in site.data.mentoring[category.block] -%}
{%- if person.email %}{{person.email}}, {% endif -%}
{%- endfor %}
{%- endfor %}

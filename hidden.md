---
layout: article
title: Hidden Information
aside:
  toc: true
---

## Today's Date

{{ site.time | date: '%B %d, %Y' }}

{% assign current_year = 2025 %}

## Email Lists

### Current Email List

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- if person.email and person.current %}{{person.email}}, {% endif -%}
{%- endfor -%}
{%- endfor %}

### Email Lists for Remaining {{current_year}}

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- unless person.updated == current_year or person.deceased or person.email == nil %}{{person.email}}, {% endunless %}
{%- endfor -%}
{%- endfor %}

### Email Lists Done for {{current_year}}

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- if person.updated == current_year %}{{person.email}}, {% endif %}
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

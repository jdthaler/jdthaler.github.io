---
layout: article
title: Hidden Information
aside:
  toc: true
---

## Missing Emails

{% for category in site.data.cv_mentoring %}
{% for person in category[1] %}
{% if person.email %}{% elsif person.deceased%}{% else %}{{person.name}} {% endif %}
{% endfor %}
{% endfor %}

## Email Lists

{% for category in site.data.cv_mentoring -%}
{%- for person in category[1] -%}
{%- if person.email %}{{person.email}}, {% endif -%}
{%- endfor -%}
{%- endfor %}

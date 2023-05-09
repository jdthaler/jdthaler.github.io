---
layout: article
title: Hidden Information
aside:
  toc: true
---




## Email Lists for Remaining 2023

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- unless person.updated == 2023 or person.deceased or person.email == nil %}{{person.email}}, {% endunless %}
{%- endfor -%}
{%- endfor %}


## Full Email List

{% for category in site.data.mentoring -%}
{%- for person in category[1] -%}
{%- if person.email %}{{person.email}}, {% endif -%}
{%- endfor -%}
{%- endfor %}




<details>
<summary markdown=1># OAISHOIHD
{:.inline-block}
</summary>
Hello
</details>

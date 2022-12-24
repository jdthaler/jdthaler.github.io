---
layout: article
title: Research
aside:
  toc: true
---

[Detailed Research](research_detail){:.button.button--outline-primary.button--pill}

{% for theme in site.data.research.themes %}
## {{theme.title}} {#{{theme.key}}}
{% endfor %}

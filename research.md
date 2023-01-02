---
layout: article
title: Research Topics
aside:
  toc: true
---

[Research in Detail](research_detail){:.button.button--outline-primary.button--pill}
[Publications by Year](cv#publications--preprints){:.button.button--outline-primary.button--pill}

{% for theme in site.data.research.themes %}
## {{theme.title}} {#{{theme.key}}}
{% endfor %}

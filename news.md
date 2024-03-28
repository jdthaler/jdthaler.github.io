---
layout: article
title: In the News
aside:
  toc: true
permalink: /news/
---


## Recent News

{% assign news_list = site.data.news.profiles | concat: site.data.news.awards | concat: site.data.news.perspectives | concat: site.data.news.group_news %}

{% assign sorted_news_list = news_list | sort: "date" | reverse%} 
{% assign seconds = 2 | times: 60 | times: 60 | times: 24 | times: 365 %}
{% assign two_years_ago = "now" | date: "%s" | minus: seconds %}

{% for news in sorted_news_list %}

{% assign itemdate = news.date | date: "%s" | minus: 0 %}
{% if itemdate < two_years_ago %}{% break %}{% endif %}

<div class="item"> 
  <div class="item__image" class="m-2">
    <a href="{{news.url}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{news.image | default: "/images/bubble_chamber.jpg"}}" title="{{news.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * "[{{news.title}}]({{news.url}}){:target="_blank"}" \\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
  </div> 
</div>
{% endfor %}



## News Archive


<details markdown=1>
<summary><b>Profiles and Highlights</b></summary>

{% for news in site.data.news.profiles %}
<div class="item">
  <div class="item__image" class="m-2">
    <a href="{{news.url}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{news.image | default: "/images/bubble_chamber.jpg"}}" title="{{news.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * "[{{news.title}}]({{news.url}}){:target="_blank"}" \\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
  </div>
</div>
{% endfor %}

</details>


<details markdown=1>
<summary><b>Awards and Honors</b></summary>

{% for news in site.data.news.awards %}
<div class="item">
  <div class="item__image" class="m-2">
    <a href="{{news.url}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{news.image | default: "/images/bubble_chamber.jpg"}}" title="{{news.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * **{{news.short}}**: "[{{news.title}}]({{news.url}}){:target="_blank"}" \\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
  </div>
</div>
{% endfor %}

</details>


<details markdown=1>
<summary><b>Quotations and Perspectives</b></summary>

{% for news in site.data.news.perspectives %}
<div class="item">
  <div class="item__image" class="m-2">
    <a href="{{news.url}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{news.image | default: "/images/bubble_chamber.jpg"}}" title="{{news.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * "[{{news.title}}]({{news.url}}){:target="_blank"}" \\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
{%- if news.quote %}
  > *{{news.quote}}*
{%- endif %}
  </div>
</div>
{% endfor %}

</details>


<details markdown=1>
<summary><b>Group Members in the News</b></summary>

{% for news in site.data.news.group_news %}
<div class="item">
  <div class="item__image" class="m-2">
    <a href="{{news.url}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{news.image | default: "/images/bubble_chamber.jpg"}}" title="{{news.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * **{{news.person}}**: "[{{news.title}}]({{news.url}}){:target="_blank"}"\\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
  </div>
</div>
{% endfor %}

</details>

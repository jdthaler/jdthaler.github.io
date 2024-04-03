---
layout: article
title: In the News
aside:
  toc: true
permalink: /news/
---

Press coverage and updates related to me and my research group.  Last updated:  {{ "now" | date: "%B %e, %Y" }}

[Press Information](/press){:.button.button--secondary.button--pill.button--sm}
[News Archive](#news-archive){:.button.button--secondary.button--pill.button--sm}


{% assign two_year_seconds = 2.0 | times: 60 | times: 60 | times: 24 | times: 365 %}
{% assign two_years_ago = "now" | date: "%s" | minus: two_year_seconds %}

{% assign one_year_seconds = 1.0 | times: 60 | times: 60 | times: 24 | times: 365 %}
{% assign one_year_ago = "now" | date: "%s" | minus: one_year_seconds %}


## Recent News Articles

_Press coverage in the past 24 months:_

{% assign news_list = site.data.news.profiles | concat: site.data.news.awards | concat: site.data.news.perspectives | concat: site.data.news.group_news %}

{% assign sorted_news_list = news_list | sort: "date" | reverse%} 

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
  * {% if news.person%}**{{news.person}}**: {% endif %} {% if news.short%}**{{news.short}}**: {% endif %} "[{{news.title}}]({{news.url}}){:target="_blank"}" \\
    *{{news.journal}}, {{news.date | date: "%B %Y"}}*
{%- if news.quote %}
  > *{{news.quote}}*
{%- endif %}
  </div> 
</div>
{% endfor %}


## Recent Papers

[All Papers by Year](/cv/#publications--preprints){:.button.button--secondary.button--pill.button--sm}
[All Papers by Topic](/research/){:.button.button--secondary.button--pill.button--sm}

_Papers posted to the arXiv from the past 12 months:_

{% assign one_arxiv_year_ago = "now" | date: "%y%m" | minus: 100 %}

{% for paper in site.data.papers.papers -%}
{% assign arxivdate = paper.arxiv | minus: 0 %}
{% if arxivdate < one_arxiv_year_ago %}{% break %}{% endif %}

<div class="item"> 
  <div class="item__image" class="m-2">
    <a href="https://arxiv.org/abs/{{paper.arxiv}}">
      <img class="image image-96--sm" style="object-fit: contain" src="{{paper.image | default: "/images/bubble_chamber.jpg"}}" title="{{paper.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * {% include cv/paper_short_item.html paper = paper %}
  </div> 
</div>
{% endfor %}


## Recent Events

_Talks and panels from the past 12 months:_

{% assign talk_list = site.data.talks.colloquia | concat: site.data.talks.public | concat: site.data.talks.schools | concat: site.data.talks.invited | concat: site.data.talks.local | concat: site.data.talks.seminars | concat: site.data.talks.additional %}

{% assign sorted_talk_list = talk_list | where: "track","true" | sort: "date" | reverse %} 

{% for talk in sorted_talk_list -%}
{%- assign itemdate = talk.date | date: "%s" | minus: 0 -%}
{%- if itemdate < one_year_ago -%}{%- break -%}{%- endif -%}
{%- unless talk.title or talk.panelist -%}{%- continue -%}{%- endunless -%}
{% include cv/talk_item.html talk = talk %}
{%- endfor %}


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

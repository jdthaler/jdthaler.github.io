---
layout: article
title: In the News
aside:
  toc: true
permalink: /news/
---

Press coverage and updates related to me and my research group.  Last updated:  {{ "now" | date: "%B %e, %Y" }}

{% assign two_year_seconds = 2.0 | times: 60 | times: 60 | times: 24 | times: 365 %}
{% assign two_years_ago = "now" | date: "%s" | minus: two_year_seconds %}

{% assign one_year_seconds = 1.0 | times: 60 | times: 60 | times: 24 | times: 365 %}
{% assign one_year_ago = "now" | date: "%s" | minus: one_year_seconds %}


## Recent News Articles

[Press Information](/press){:.button.button--secondary.button--pill.button--sm}
[News Archive](#news-archive){:.button.button--secondary.button--pill.button--sm}

_Press coverage in the past 24 months:_

{% assign news_list = '' | split: '' %}

{% for category in site.data.news.categories %}
{% assign news_list = news_list | concat: site.data.news[category.key] %}
{% endfor %}

{% assign sorted_news_list = news_list | sort: "date" | reverse %} 

{% for news in sorted_news_list %}

{% assign itemdate = news.date | date: "%s" | minus: 0 %}
{% if itemdate < two_years_ago %}{% break %}{% endif %}

{% include news_card.html news = news %}
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
      {%- assign _img = paper.image | default: site.data.news.default_image -%}{%- include snippets/get-preview-url.html url=_img -%}<img class="image image-96--sm" style="object-fit: contain" src="{{__return}}" alt="{{paper.title}}" title="{{paper.title}}"/>
    </a>
  </div>
  <div class="item__content" markdown="1">
  * {% include cv/paper_short_item.html paper = paper %}
  </div> 
</div>
{% endfor %}


## Recent/Upcoming Events

[All Presentations](/cv/#presentations){:.button.button--secondary.button--pill.button--sm}

_Talks and panels from the past 12 months:_

{% assign talk_list = '' | split: '' %}

{% for category in site.data.talks.categories %}
{% assign talk_list = talk_list | concat: site.data.talks[category.key] %}
{% endfor %}

{% assign sorted_talk_list = talk_list | where: "track","true" | sort: "date" | reverse %} 

{% for talk in sorted_talk_list -%}
{%- assign itemdate = talk.date | date: "%s" | minus: 0 -%}
{%- if itemdate < one_year_ago -%}{%- break -%}{%- endif -%}
{%- unless talk.title or talk.panelist -%}{%- continue -%}{%- endunless -%}
{% include cv/talk_item.html talk = talk %}
{%- endfor %}


## News Archive

{% for category in site.data.news.categories -%}
<details markdown=1>
<summary><b>{{category.title}}</b></summary>

{% for news in site.data.news[category.key] %}
{% include news_card.html news = news %}
{% endfor %}

</details>
{% endfor %}

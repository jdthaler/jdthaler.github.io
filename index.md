---
layout: article
---

{% assign topimage = site.data.bio.index_top %}
<center>
<img class="rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</center>
{{topimage.description}}

### Research

<div class="grid-container">
  <div class="grid grid--px-2">
  {% for topic in site.data.research.topics %}
      <div class="cell cell--4">
          <center>
          <a href="research.html#{{topic.key}}">
            <img class="rounded" style="object-fit: cover" src="{{topic.image}}" title="{{topic.title}}"/>
          <br>
              <b>{{topic.title}}</b>
          </a>
          </center>
    </div>
  {% endfor %}
    </div>
</div>


### Positions


<div class="grid-container">
  <div class="grid grid--py-3">
    {% for position in site.data.bio.positions %}

    <div class="cell cell--6">
          <center>
          <a href="{{position.url}}">
            <img class="image-h image-h--xs image-contain" src="{{position.image}}" title="{{position.hover}}"/>
          <br>
              <b>{{position.title}}, {{position.acronym}}</b>
          </a>
          </center>
    </div>
    {% endfor %}
  </div>
</div>


### Affiliations

<div class="grid-container">
  <div class="grid grid--py-3">
    {% for affiliation in site.data.bio.affiliations %}
    <div class="cell cell--3">
          <center>
          <a href="{{affiliation.url}}">
            <img class="image-h image-h--xs image-contain" src="{{affiliation.image}}" title="{{affiliation.acronym}}"/>
          <br>
              <div class="">{{affiliation.name}} ({{affiliation.acronym}})</div>
          </a>
          </center>
    </div>
    {% endfor %}    
  </div>
</div>




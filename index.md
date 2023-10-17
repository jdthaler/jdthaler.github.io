---
layout: article
---

{% assign topimage = site.data.bio.index_top %}
<center>
<img class="" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</center>
**[Jesse Thaler](about)** is a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics.

He is a Professor of Physics at the **[Massachusetts Institute of Technology (MIT)](https://physics.mit.edu/){:target="_blank"}** and Director of the **[NSF Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](https://iaifi.org/){:target="_blank"}**.

### Research

<div class="grid-container">
  <div class="grid grid--px-2">
  {% for topic in site.data.research.topics %}
      <div class="cell cell--4">
          <center>
          <a href="research#{{topic.key}}">
            <img class="" style="object-fit: cover" src="{{topic.image}}" title="{{topic.title}}"/>
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
          <a href="{{position.url}}" target="_blank">
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
    {% for affiliation in site.data.bio.affiliations %}{% if affiliation.priority >= 6 %}
    <div class="cell cell--3">
          <center>
          <a href="{{affiliation.url}}" target="_blank">
            <img class="image-h image-h--xs image-contain" src="{{affiliation.image}}" title="{{affiliation.acronym}}"/>
          <br>
              <div class="">{{affiliation.name}} ({{affiliation.acronym}})</div>
          </a>
          </center>
    </div>
    {% endif %}
    {% endfor %}    
  </div>
</div>


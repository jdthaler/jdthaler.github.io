---
layout: article
---

<center>
{% assign topimage = site.data.images.index[0] %}
<img class="rounded" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</center>

**[Jesse Thaler](about)** is a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics.

He is a Professor of Physics at the **[Massachusetts Institute of Technology (MIT)](https://physics.mit.edu/)** and Director of the **[NSF Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](http://iaifi.org/)**.

### Research

<div class="grid-container">
  <div class="grid grid--py-3">
  {% for topic in site.data.research.topics %}
      <div class="cell cell--4">
          <center>
          <a href="research.html#{{topic.key}}">
            <img class="image image--md rounded" style="object-fit: cover" src="{{topic.image}}" title="{{topic.title}}"/>
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
    <div class="cell cell--6">
          <center>
          <a href="https://physics.mit.edu/">
            <img class="image-h image-h--xs" src="images/logo_mit_physics.png" title="MIT Physics"/>
          <br>
              <b>Professor of Physics, MIT</b>
          </a>
          </center>
    </div>
    <div class="cell cell--6">
          <center>
          <a href="http://iaifi.org/">
            <img class="image-h image-h--xs" src="images/logo_iaifi_nsf.png" title="IAIFI"/>
          <br>
              <b>Director, IAIFI</b>
          </a>
          </center>
    </div>
  </div>
</div>


### Affiliations

<div class="grid-container">
  <div class="grid grid--py-3">
    {% for affiliation in site.data.bio.affiliations %}
    <div class="cell cell--3">
          <center>
          <a href="{{affiliation.url}}">
            <img class="image-h image-h--xs" src="{{affiliation.image}}" title="{{affiliation.acronym}}"/>
          <br>
              <div class="">{{affiliation.name}} ({{affiliation.acronym}})</div>
          </a>
          </center>
    </div>
    {% endfor %}    
  </div>
</div>




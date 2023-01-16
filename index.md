---
layout: article
---

<center>
<img class="rounded" src="images/jthaler_mit_spotlight.jpg" title="Jesse Thaler"/>
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
    <div class="cell cell--3">
          <center>
          <a href="http://ctp.mit.edu/">
            <img class="image-h image-h--xs" src="images/logo_ctp.png" title="CTP"/>
          <br>
              <div class="">Center for Theoretical Physics (CTP)</div>
          </a>
          </center>
    </div>
        <div class="cell cell--3">
          <center>
          <a href="http://web.mit.edu/lns/">
            <img class="image-h image-h--xs" src="images/logo_lns.png" title="LNS"/>
          <br>
              <div class="">Laboratory for Nuclear Science (LNS)</div>
          </a>
          </center>
    </div>
    <div class="cell cell--3">
          <center>
          <a href="https://idss.mit.edu/">
            <img class="image-h image-h--xs" src="images/logo_sdsc.png" title="SDSC"/>
          <br>
                <div class="">Statistics and Data Science Center (SDSC)</div>
          </a>
          </center>
    </div>

    <div class="cell cell--3">
          <center>
          <a href="https://idss.mit.edu/">
            <img class="image-h image-h--xs" src="images/logo_idss.jpg" title="IDSS"/>
          <br>
          <div class="">Institute for Data, Systems, and Society (IDSS)</div>
          </a>
          </center>
    </div>

  </div>
</div>


### Navigation

<div align="center" markdown=1>
{% for button in site.data.navigation.header %}[{{button.title}}]({{button.url}}){:.button.button--outline-primary.button--pill} {% endfor %}
[Personal Page](personal){:.button.button--outline-primary.button--pill}
</div>





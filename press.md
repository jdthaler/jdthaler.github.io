---
layout: article
title: Press Information
aside:
  toc: true
  
---

## Photographs

<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--6">
          <a href="images/jthaler_mit_spotlight.jpg">
            <img class="image-h image-h--sm" src="images//jthaler_mit_spotlight.jpg" title="Thaler Blackboard Shot"/>
          <br>
              <b>Blackboard Shot</b>
          </a>
    </div>
    
    <div class="cell cell--6">
          <a href="images/jthaler_photo_2017.jpg">
            <img class="image-h image-h--sm" src="images/jthaler_photo_2017.jpg" title="Thaler Head Shot"/>
          <br>
              <b>Head Shot</b>
          </a>
    </div>
  </div>
</div>

## Extended Biography

### Research Interests

Jesse Thaler is a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics.  His current research is focused on maximizing the discovery potential of the Large Hadron Collider (LHC) through new theoretical frameworks and novel data analysis techniques.  Prof. Thaler is an expert in jets, which are collimated sprays of particles that are copiously produced at the LHC, and he studies the substructure of jets to enhance the search for new phenomena and illuminate the dynamics of gauge theories.  He is also interested in new strategies to probe the nature of dark matter at the LHC and beyond, as well as in the theoretical structures and experimental signatures of supersymmetry.

### Biographical Sketch

Jesse Thaler joined the MIT Physics Department in 2010, and is currently a Professor in the Center for Theoretical Physics.  From 2006 to 2009, he was a fellow at the Miller Institute for Basic Research in Science at the University of California, Berkeley.  He received his Ph.D. in Physics from Harvard University in 2006, and his Sc.B. in Math/Physics from Brown University in 2002.   In 2020, Prof. Thaler became the inaugural Director of the NSF AI Institute for Artificial Intelligence and Fundamental Interactions.

## Image Credits

{% assign frontimage = site.data.bio.index_top %}
{% assign aboutimage = site.data.bio.about_top %}
{% assign publicimage = site.data.public.public_top %}

  * ![{{frontimage.hover}}]({{frontimage.image}}){:.image--xs} Front Page: [{{frontimage.image_credit}}](frontimage.image_url)
  * ![{{aboutimage.hover}}]({{aboutimage.image}}){:.image--xs} About Page: [{{aboutimage.image_credit}}](aboutimage.image_url)
{% for topic in site.data.research.topics -%}
  * ![{{topic.title}}]({{topic.image}}){:.image--xs} Research, {{topic.title}}: [{{topic.image_credit}}]({{topic.image_url}})
{% endfor -%}
  * ![{{publicimage.hover}}]({{publicimage.image}}){:.image--xs} Public Engagement Page: [{{publicimage.image_credit}}](publicimage.image_url)
{% for topic in site.data.public.topics -%}
  * ![{{topic.title}}]({{topic.image}}){:.image--xs} Public Engagement, {{topic.title}}: [{{topic.image_credit}}]({{topic.image_url}})
{% endfor -%}

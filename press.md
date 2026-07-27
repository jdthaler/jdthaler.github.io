---
layout: article
title: Press Information
aside:
  toc: true
permalink: press/
---

## Photographs

<div class="grid-container">
  <div class="grid grid--py-3">
    <div class="cell cell--6">
          <a href="/images/jthaler_mit_spotlight.jpg">
            <img class="image-h image-h--sm" src="/images/preview/jthaler_mit_spotlight.jpg" alt="" title="Thaler Blackboard Shot"/>
          <br>
              <b>Blackboard Shot</b>
          </a>
          <br>
          <a href="/images/jthaler_mit_spotlight_large_uncropped.jpg">Full resolution</a> (uncropped)
    </div>
    
    <div class="cell cell--6">
          <a href="/images/jthaler_photo_2017.jpg">
            <img class="image-h image-h--sm" src="/images/preview/jthaler_photo_2017.jpg" alt="" title="Thaler Head Shot"/>
          <br>
              <b>Head Shot</b>
          </a>
          <br>
          <a href="/images/jthaler_photo_2017_large_uncropped.jpg">Full resolution</a> (uncropped)
    </div>
  </div>
</div>


##   Biography

Jesse Thaler is a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics.  His current research is focused on maximizing the discovery potential of the Large Hadron Collider through new theoretical frameworks and novel data analysis techniques. Prof. Thaler joined the MIT Physics Department in 2010, and he is currently a Professor in the MIT Center for Theoretical Physics - a Leinweber Institute. In 2020, he became the inaugural Director of the NSF Institute for Artificial Intelligence and Fundamental Interactions.

## Extended Biography

### Research Interests

Jesse Thaler is a theoretical particle physicist who fuses techniques from quantum field theory and machine learning to address outstanding questions in fundamental physics.  His current research is focused on maximizing the discovery potential of the Large Hadron Collider (LHC) through new theoretical frameworks and novel data analysis techniques.  Prof. Thaler is an expert in jets, which are collimated sprays of particles that are copiously produced at the LHC, and he studies the substructure of jets to enhance the search for new phenomena and illuminate the dynamics of gauge theories.  He is also interested in new strategies to probe the nature of dark matter at the LHC and beyond, as well as in the theoretical structures and experimental signatures of supersymmetry.

### Biographical Sketch

Jesse Thaler joined the MIT Physics Department in 2010, and is currently a Professor in the MIT Center for Theoretical Physics - a Leinweber Institute.  From 2006 to 2009, he was a fellow at the Miller Institute for Basic Research in Science at the University of California, Berkeley.  He received his Ph.D. in Physics from Harvard University in 2006, and his Sc.B. in Math/Physics from Brown University in 2002.   In 2020, Prof. Thaler became the inaugural Director of the NSF Institute for Artificial Intelligence and Fundamental Interactions.

### Links to Additional Information

[About](/about){:.button.button--secondary.button--pill.button--sm}
[Full CV](/cv){:.button.button--secondary.button--pill.button--sm}
[MIT Physics Page](https://web.mit.edu/physics/people/faculty/thaler_jesse.html){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Wikipedia](https://en.wikipedia.org/wiki/Jesse_Thaler){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

## Image Credits

{% assign frontimage = site.data.bio.index_top %}
{% assign aboutimage = site.data.bio.about_top %}
{% assign publicimage = site.data.public.public_top %}

  * [![{{frontimage.hover}}]({% include snippets/get-preview-url.html url=frontimage.image %}{{__return}}){:.image--xs}]({{frontimage.image}}) Front Page: [{{frontimage.image_credit}}]({{frontimage.image_url}})
  * [![{{aboutimage.hover}}]({% include snippets/get-preview-url.html url=aboutimage.image %}{{__return}}){:.image--xs}]({{aboutimage.image}}) About Page: [{{aboutimage.image_credit}}]({{aboutimage.image_url}})
{% for topic in site.data.research.topics -%}
  * [![{{topic.title}}]({% include snippets/get-preview-url.html url=topic.image %}{{__return}}){:.image--xs}]({{topic.image}}) Research, {{topic.title}}: [{{topic.image_credit}}]({{topic.image_url}})
{% endfor -%}
  * [![{{publicimage.hover}}]({% include snippets/get-preview-url.html url=publicimage.image %}{{__return}}){:.image--xs}]({{publicimage.image}}) Public Engagement Page: [{{publicimage.image_credit}}]({{publicimage.image_url}})
{% for topic in site.data.public.topics -%}
  * [![{{topic.title}}]({% include snippets/get-preview-url.html url=topic.image %}{{__return}}){:.image--xs}]({{topic.image}}) Public Engagement, {{topic.title}}: [{{topic.image_credit}}]({{topic.image_url}})
{% endfor -%}

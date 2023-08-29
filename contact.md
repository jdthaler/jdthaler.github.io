---
layout: article
title: Contact Information
permalink: contact/
---
{% assign topimage = site.data.bio.contact_top %}

{% assign name = site.data.about.name %}
{% assign address = site.data.about.address %}
{% assign email = site.data.about.email %}
{% assign phone = site.data.about.phone %}
{% assign urls = site.data.about.urls %}


<div class="item">
<div class="item__image">
<img class="image-96--xl" src="{{topimage.image}}" title="{{topimage.hover}}"/>
</div>
<div class="item__content" markdown=1>
{{name.first}} {{name.last}}\\
{{address.org}}\\
{{address.street}}, [{{address.office}}]({{address.office_url}})\\
{{address.city}}, {{address.state}} {{address.zip}}

{{phone.work}}

*Pronouns*:  {{name.pronouns}} \\
*Pronunciation*:  {{name.pronunciation}}
</div>
</div>

[Joining My Group](/join){:.button.button--secondary.button--pill.button--sm}
[{{email.work}}](mailto:{{email.work}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Twitter]({{urls.twitter}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[LinkedIn]({{urls.linkedin}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[GitHub]({{urls.github}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}


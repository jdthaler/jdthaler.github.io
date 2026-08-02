---
layout: article
title: Contact Information
permalink: contact/
---
{% assign name = site.data.about.name %}
{% assign email = site.data.about.email %}
{% assign phone = site.data.about.phone %}
{% assign urls = site.data.about.urls %}

{% for address in site.data.about.addresses %}
<div class="item">
<div class="item__image">
<img class="image-96--xl" src="{% include snippets/get-preview-url.html url=address.image %}{{__return}}" alt="{{address.alt}}" title="{{address.hover}}"/>
</div>
<div class="item__content" markdown=1>
{% if forloop.first %}**{{name.first}} {{name.last}}**\\
{% endif %}{{address.org}}\\
{{address.street}}, [{{address.office}}]({{address.office_url}})\\
{{address.city}}, {{address.state}} {{address.zip}}
{% if address.official_office %}
Official MIT office number:  [{{address.official_office}}]({{address.official_office_url}})
{% endif %}{% if address.note %}
{{address.note}}
{% endif %}
</div>
</div>
{% endfor %}

Reachable at either office:  {{phone.work}} \\
Fax:  {{phone.fax}}


*Pronouns*:  {{name.pronouns}} \\
*Pronunciation*:  {{name.pronunciation}}




[Joining My Group](/join){:.button.button--secondary.button--pill.button--sm}
[{{email.work}}](mailto:{{email.work}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Twitter]({{urls.twitter}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[LinkedIn]({{urls.linkedin}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[GitHub]({{urls.github}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}


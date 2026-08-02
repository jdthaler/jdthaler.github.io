---
layout: article
title: Contact Information
permalink: contact/
---
{% assign name = site.data.about.name %}
{% assign email = site.data.about.email %}
{% assign phone = site.data.about.phone %}
{% assign urls = site.data.about.urls %}

## {{name.first}} {{name.last}}

*Pronouns*:  {{name.pronouns}} \\
*Pronunciation*:  {{name.pronunciation}}

Phone:  {{phone.work}}

[Joining My Group](/join){:.button.button--secondary.button--pill.button--sm}
[{{email.work}}](mailto:{{email.work}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Twitter]({{urls.twitter}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[LinkedIn]({{urls.linkedin}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[GitHub]({{urls.github}}){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

{% for address in site.data.about.addresses %}
## {{address.acronym}} Office

<div class="item">
<div class="item__image">
<img class="image-96--xl" src="{% include snippets/get-preview-url.html url=address.image %}{{__return}}" alt="{{address.alt}}" title="{{address.hover}}"/>
</div>
<div class="item__content" markdown=1>
{{name.first}} {{name.last}}\\
{{address.org}}\\
{{address.street}}, [{{address.office}}]({{address.office_url}})\\
{{address.city}}, {{address.state}} {{address.zip}}

MIT floor plan office number:  [{{address.official_office}}]({{address.official_office_url}})

</div>
</div>
{% endfor %}

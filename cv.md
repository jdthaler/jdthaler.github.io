---
layout: article
title: Curriculum Vitae
aside:
  toc: true
permalink: cv/

---

[Short CV](/about){:.button.button--secondary.button--pill.button--sm}
[Press Information](/press){:.button.button--secondary.button--pill.button--sm}
[Papers by Year](#publications--preprints){:.button.button--secondary.button--pill.button--sm}
[Presentations](#presentations){:.button.button--secondary.button--pill.button--sm}
[PDF CV (March 2025)](/pdfs/jthaler_cv_2025_03_18.pdf){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

## Jesse Diaz Thaler

#### Research in Theoretical Particle Physics

{% for topic in site.data.research.topics %}  * **[{{topic.title}}](/research/#{{topic.key}})**
{% endfor %}

## Positions

### MIT

 * **Massachusetts Institute of Technology**, *January 2010-Present*
   * Professor of Physics, *July 2021-Present*
   * Associate Professor of Physics with Tenure, *May 2017-July 2021*
   * Associate Professor of Physics, *July 2015-May 2017*
   * Class of 1943 Career Development Professor, *July 2012-July 2015*
   * Assistant Professor of Physics, *January 2010-July 2015*
   
### Leadership

 * **[NSF Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](https://iaifi.org/){:target="_blank"}**, Director, *August 2020-Present*

### Affiliations

{% for affiliation in site.data.bio.affiliations -%}
  * **{%- if affiliation.url -%}
      [{% if affiliation.mit %}MIT {% endif %}{{affiliation.name}}{% if affiliation.acronym %} ({{affiliation.acronym}}){% endif %}]({{affiliation.url}}){:target="_blank"}
    {%- else -%}
        {% if affiliation.mit %}MIT {% endif %}{{affiliation.name}}{% if affiliation.acronym %} ({{affiliation.acronym}}){% endif %}
    {%- endif -%}**, {% if affiliation.position %}{{affiliation.position}}, {% endif %} *{{affiliation.dates}}*
{% endfor %}

### Berkeley

 * **Lawrence Berkeley National Laboratory**, *July 2009-December 2009*
   * Physicist Postdoctoral Fellow, Theoretical Physics Group

 * **University of California, Berkeley**, *July 2006-June 2009*
   * Miller Research Fellow, Miller Institute for Basic Research in Science


## Education

{% for school in site.data.about.education -%}
### {{school.short_org}}
  * **{{school.org}}**, *{{school.dates}}*
{%- for degree in school.degrees %}
    * {{degree.type}} {{degree.field}}, {% if degree.thesis %}"[{{degree.thesis}}]({{degree.thesis_url}}){:target="_blank"}",{% endif %} *{{degree.month}} {{degree.year}}*
{%- endfor %}
{% if school.advisor %}    * Advisor: {{school.advisor}}
{% endif %}
{% endfor %}


## Awards & Fellowships

{% for award in site.data.bio.awards -%}
  {%- if award.url %}
  * **[{{award.name}}]({{award.url}}){:target="_blank"}**, *{{award.org}}*, *{{award.date}}*
  {%- else %}
  * **{{award.name}}**, *{{award.org}}*, *{{award.date}}*
  {%- endif %}
{%- endfor %}


## Mentoring

[Research Group](/group){:.button.button--secondary.button--pill.button--sm}
[Joining My Group](/join){:.button.button--secondary.button--pill.button--sm}

### Postdoctoral Researchers

{% for person in site.data.mentoring.postdocs -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {{person.at[0].title}}, *{{person.at[0].dates}}*{% if person.at[1] %}; {{person.at[1].title}}, *{{person.at[1].dates}}* {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
    * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.before[0] %}
    * Before MIT: {{person.before[0].org}} ({{person.before[0].title}}){% endif %}{% if person.before[1] %}, {{person.before[1].org}} ({{person.before[1].title}}){% endif %}{% if person.before[2] %}, {{person.before[2].org}} ({{person.before[2].title}}) {% endif %}
  {%- if person.after[0] %}
    * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
    * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


### Ph.D. Students

{% for person in site.data.mentoring.phd_students -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}Ph.D.{% else %}anticipated Ph.D.{% endif %} {{person.date}}
  {%- if person.thesis %}
      * Thesis: {% if person.thesis_url %} ["{{person.thesis}}"]({{person.thesis_url}}) {% else %} "{{person.thesis}}" {% endif %}  {% if person.joint %} (with {{person.joint}}) {% endif %} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[0] %}
      * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


### M.Eng. Students

{% for person in site.data.mentoring.meng_students -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}M.Eng.{% else %}anticipated M.Eng.{% endif %} {{person.date}}
  {%- if person.thesis %}
      * Thesis: {% if person.thesis_url %} ["{{person.thesis}}"]({{person.thesis_url}}) {% else %} "{{person.thesis}}" {% endif %}  {% if person.joint %} (with {{person.joint}}) {% endif %} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[0] %}
      * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


### B.S. Students

{% for person in site.data.mentoring.bs_students -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis or person.graduated %}B.S.{% else %}anticipated B.S.{% endif %} {{person.date}}
  {%- if person.thesis %}
      * Senior Thesis, {{person.thesis_dates}}:  {% if person.thesis_url %} ["{{person.thesis}}"]({{person.thesis_url}}) {% else %} "{{person.thesis}}" {% endif %}     {% if person.joint %} (with {{person.joint}}) {% endif %} {% endif %}
  {%- if person.independent %}
      * Independent Research: {{person.independent}} {% endif %}
  {%- if person.urop %}
      * UROP Research: {{person.urop}} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[0] %}
      * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {%- if person.after[-1].concurrent %} and {{person.after[-2].title}}, *{{person.after[-2].org}}*{% endif %}{% endif %}
{% endfor %}


### Visitors

{% for person in site.data.mentoring.visitors -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {{person.program}}, *{{person.dates}}*
  {%- if person.project %}
      * Project: "{{person.project}}" {% endif %}
  {%- if person.home %}
      * Home Institution: {{person.home}} {% if person.home_advisor %} ({{person.home_advisor}}) {% endif %} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[-1] %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


## Teaching

### MIT

{% for course in site.data.teaching.courses -%}
  * **{{course.number}} --- {{course.title}}**
{%- for role in course.roles %}
    * {{role.name}}:  {% for iteration in role.iterations %}{% if iteration.url %}[{{iteration.date}}]({{iteration.url}}){:target="_blank"}{% else %}{{iteration.date}} `upcoming`{:.main3}{% endif %}{% if forloop.last != true %}, {% endif %}{% endfor %}
{%- endfor %}
{% endfor %}


### Guest Lectures

{% for lecture in site.data.teaching.guest_lectures -%}
  * **["{{lecture.title}}"]({{lecture.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**, {{lecture.course_number}} ({{lecture.course_name}}), *{{lecture.date}}*
{% endfor %}


### Before MIT

{% for position in site.data.teaching.before_mit -%}
  * {{position.role}}, *{{position.org}}, {{position.date}}*
{% endfor %}


## Publications & Preprints

[Papers by Topic](/research){:.button.button--secondary.button--pill.button--sm}
[Inspire](https://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[arXiv](https://arxiv.org/a/thaler_j_1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

{% for year in site.data.papers.years %}
#### {{year}}
{% for paper in site.data.papers.papers -%}
{% if year == paper.year -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){:target="_blank"}, {% endif %} {% if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}){:target="_blank"}, {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{%- endif %}
{% endfor %}
{% endfor %}


### Conference Proceedings

{% for paper in site.data.papers.conference -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){:target="_blank"}, {% endif %} {% if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}){:target="_blank"}, {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{% endfor%}


### Incidental Authorship

{% for paper in site.data.papers.incidental -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){:target="_blank"}{% endif %}
    {%- if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}){:target="_blank"}{% endif %}
    {%- if paper.arxiv and paper.doi or paper.journal_url-%}, {% endif %}
    {%- if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}){:target="_blank"}{% endif %}.
{% endfor %}


## Presentations

{% for category in site.data.talks.categories %}
### {{category.title}}

{% for talk in site.data.talks[category.key] -%}
{% include cv/talk_item.html talk = talk %}
{%- endfor %}

{% endfor %}

## Research Grants

{% for grant in site.data.funding.grants -%}
  * {{grant.name}}
  {%- if grant.collaborators %} (with {{grant.collaborators}}), {% else %}, {% endif -%}
  {%- if grant.title and grant.url %}"[{{grant.title}}]({{grant.url}}){:target="_blank"}", {% elsif grant.title %}"{{grant.title}}", {% endif -%}
  *{{grant.org}}*, *{{grant.dates}}* {% if grant.amount %}({{grant.amount}}){% endif %}
{% endfor %}


## Advising

### Ph.D. Thesis Committees
{% include cv/thesis_list.html list = site.data.advising.phd_theses %}


### Academic Advising

{% for advising in site.data.advising.academic_advising %}
  * **{% if advising.url %}[{{advising.name}}]({{advising.url}}){:target="_blank"}{% else %}{{advising.name}}{% endif %}**, *{{advising.dates}}*
{%- for cohort in advising.cohorts %}
    * {{cohort.name}}: {% for member in cohort.members %}{{member.name}}{% if forloop.last != true %}, {% endif %}{% endfor %}
{%- endfor %}
{%- endfor %}


### External Ph.D. Examiner
{% include cv/thesis_list.html list = site.data.advising.external_phd_theses %}


### External Mentoring

{% for mentoring in site.data.advising.external_mentoring %}
  * **{{mentoring.name}}**, {{mentoring.program}}, *{{mentoring.org}}, {{mentoring.dates}}*
{%- endfor %}


## Service

### Internal Service

{% for category in site.data.service.internal_categories %}
#### {{category.title}}

{% for item in site.data.service[category.key] -%}
{% include cv/service_item.html item = item %}
{%- endfor %}

{% endfor %}


### External Service

#### Institutions

{% for tag in site.data.service.institutions %}
{%- assign institution = site.data.service[tag] %}
  * {% if institution.url %}**[{{institution.name}}]({{institution.url}}){:target="_blank"}**{% else %}**{{institution.name}}**{% endif %}
{%- for role in institution.roles %}
    * {% if role.job_url %}[{{role.job}}]({{role.job_url}}){:target="_blank"}{% else %}{{role.job}}{% endif %}, {% if role.issue %}"{% if role.issue_url %}[{{role.issue}}]({{role.issue_url}}){:target="_blank"}{% else %}{{role.issue}}{% endif %}",{% endif %} *{{role.dates}}* 
{%- endfor %}
{%- endfor %}

{% for category in site.data.service.external_categories %}
#### {{category.title}}

{% for item in site.data.service[category.key] -%}
{% include cv/service_item.html item = item %}
{%- endfor %}

{% endfor %}
#### Peer Review
{% include cv/simple_list.html list = site.data.service.peer_review %}

#### Funding Agency Review 
{% include cv/simple_list.html list = site.data.service.agency_review %}


## Public Engagement
 
[Engagement Portfolio](/engagement){:.button.button--secondary.button--pill.button--sm} 
[IMDb](https://www.imdb.com/name/nm6007880/){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
 
{% for entry in site.data.public.entries %}
  * **"{% if entry.url %}[{{entry.title}}]({{entry.url}}){:target="_blank"}{% else %}{{entry.title}}{% endif %}"**{% if entry.collaborators %} (with {% if entry.collaborators_url %}[{{entry.collaborators}}]({{entry.collaborators_url}}){:target="_blank"}{% else %}{{entry.collaborators}}{% endif %}){% endif %},
   {% if entry.type %}{{entry.type}}, {% endif -%}
   {% if entry.event %}{% if entry.event_url %}[{{entry.event}}]({{entry.event_url}}){:target="_blank"}{% else %}{{entry.event}}{% endif %}, {% endif -%}   
   {% if entry.org %}*{{entry.org}}*, {% endif -%}
   {% if entry.date %}*{{entry.date | date: "%B %Y"}}* {% endif -%}
   {% if entry.doi %}[{{entry.journal}}](https://doi.org/{{entry.doi}}){:target="_blank"}{% endif %}
{%- endfor %}
  * Appearance in Documentary Film, **["Particle Fever"](https://www.imdb.com/title/tt1385956/){:target="_blank"}**, 2013 
    * After film Q&A, BOOST 2015 Workshop Public Event, August 2015
    * After film Q&A, MIT Lecture Series Committee, September 2014
    * After film Q&A, Portsmouth Music Hall, May 2014
  * **TheoryNet**, High School Physics Outreach
    * Scott Goelzer, Coe-Brown Northwood Academy (Fall 2020-Spring 2021)
    * Elaine Picard, Concord-Carlisle High School (Fall 2015-Spring 2016, Spring 2017, Spring 2020)
    * Michael Wadness, Medford High School  (Fall 2012-Spring 2015, Spring 2018, Spring 2022)
    * Michael Hirsh, Needham High School  (Spring 2010-Spring 2012)
  * Additional Outreach
    * Neil Basu, American School in London (May 2024)
    * Hiroko Kaczmarek, Cambridge Rindge and Latin School (May 2021)
  * High School Job Shadowing
    * Audrey Grimes (York High School, December 2017)
    * Cole Gilbert (Traip Academy, November 2017)    
    * Joshua Reynolds (York High School, April 2016)
    * Edward Bengtson (York High School, April 2014)

## Graphic Design

[Design Portfolio](/personal#graphic-design){:.button.button--secondary.button--pill.button--sm}

  * **[Image Design](design/jthaler_Flavour_PRD.pdf){:target="_blank"}** (with Gavin Salam), [Flavoured Jet Algorithms](https://arxiv.org/abs/2306.07314){:target="_blank"}, *Physical Review D, October 2023*
  * **[Banner Design](design/jthaler_IAIFI_Banner.jpg){:target="_blank"}**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](https://iaifi.org/){:target="_blank"}, *August 2020*  (based on artwork by [agsandrew](https://agsandrew.myportfolio.com/{:target="_blank"}) - stock.adobe.com)
  * **[Logo Design](design/jthaler_IAIFI_Logo.pdf){:target="_blank"}**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](https://iaifi.org/){:target="_blank"}, *August 2020*
  * **[Logo Design](design/jthaler_OmniFold_Logo.pdf){:target="_blank"}**, [OmniFold](https://github.com/ericmetodiev/OmniFold/){:target="_blank"}, *MIT, November 2019*
  * **[Poster Design](design/jthaler_BOOST2019_Poster.pdf){:target="_blank"}** ([with bleeds](design/jthaler_BOOST2019_Poster_Bleed.pdf){:target="_blank"}), [BOOST 2019 Workshop](https://indico.cern.ch/e/boost2019), *MIT, July 2019*
  * **[Logo Design](design/jthaler_ABRALogo_Large.pdf){:target="_blank"}** ([Alt.](design/jthaler_ABRALogo_Medium.pdf){:target="_blank"}, [A.](design/jthaler_ABRALogo_Small.pdf){:target="_blank"}), [ABRACADABRA Experiment](https://abracadabra.mit.edu/), *MIT, August 2017*
  * **[Logo Design](design/jthaler_MOD_Logo.pdf){:target="_blank"}** ([Event Display](design/jthaler_MOD_EventDisplay.pdf){:target="_blank"}), MIT Open Data, *MIT, July 2015*
  * **[Logo Design](design/jthaler_DarkLight_Logo.pdf){:target="_blank"}**, [DarkLight Experiment](http://dmtpc.mit.edu/DarkLight/){:target="_blank"}, *MIT, September 2010*


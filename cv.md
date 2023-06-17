---
layout: article
title: Curriculum Vitae
aside:
  toc: true
permalink: cv/

---

[Short CV](/about){:.button.button--secondary.button--pill.button--sm}
[Press Information](/press){:.button.button--secondary.button--pill.button--sm}
[Publications by Year](#publications--preprints){:.button.button--secondary.button--pill.button--sm}
[Presentations](#presentations){:.button.button--secondary.button--pill.button--sm}
[PDF CV (June 2023)](/pdfs/jthaler_cv_2023_06.pdf){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

## Jesse Diaz Thaler

#### Research in Theoretical Particle Physics

{% for topic in site.data.research.topics %}  * **[{{topic.title}}](research.html#{{topic.key}})**
{% endfor %}


## Positions

### MIT

 * **Massachusetts Institute of Technology**, *January 2010 - Present*
   * Professor of Physics, *July 2021 - Present*
   * Associate Professor of Physics with Tenure, *May 2017 - July 2021*
   * Associate Professor of Physics, *July 2015 - May 2017*
   * Class of 1943 Career Development Professor, *July 2012 - July 2015*
   * Assistant Professor of Physics, *January 2010 - July 2015*
 * **Leadership**
    * Director, [NSF Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](https://iaifi.org/){:target="_blank"}, *August 2020 - Present*
 * **Affiliations**
   * [MIT Center for Theoretical Physics (CTP)](http://ctp.mit.edu/){:target="_blank"} and [Laboratory for Nuclear Science (LNS)](http://web.mit.edu/lns/){:target="_blank"}, *January 2010 - Present*
   * [MIT Statistics and Data Science Center (SDSC)](https://stat.mit.edu/){:target="_blank"} and [Institute for Data, Systems, and Society (IDSS)](https://idss.mit.edu/){:target="_blank"}, *January 2020 - Present*

### Visiting

 * **Harvard University**, *September 2018 - August 2019*
   * Visiting Scholar, Simons Fellowship in Theoretical Physics
 * **Boston University**, *June 2017 - August 2017*
   * Visiting Researcher

### Berkeley

 * **Lawrence Berkeley National Laboratory**, *July 2009 - December 2009*
   * Physicist Postdoctoral Fellow, Theoretical Physics Group

 * **University of California, Berkeley**, *July 2006 - June 2009*
   * Miller Research Fellow, Miller Institute for Basic Research in Science


## Education

### Harvard

  * **Harvard University**, *Fall 2002 - Spring 2006*
    * Ph.D. Physics, "[Symmetry Breaking at the Energy Frontier](http://inspirehep.net/record/738871){:target="_blank"}", *June 2006* 
    * A.M. Physics, *June 2004*
    * Advisor:  Nima Arkani-Hamed

### Brown

  * **Brown University**, *Fall 1998 - Spring 2002*
    * Sc.B. Math/Physics, *May 2002*
    * Advisor: Antal Jevicki

### PEA

  * **Phillips Exeter Academy**, *Fall 1994 - Spring 1998*


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
  {% if person.url %}  * **[{{person.name}}]({{person.url}}){:target="_blank"}**,{% else %}  * **{{person.name}}**,{% endif %} {{person.at[0].title}}, *{{person.at[0].dates}}* {% if person.at[1] %}; {{person.at[1].title}}, *{{person.at[1].dates}}* {% endif %}
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
    * {{role.name}}:  {% for iteration in role.iterations %}[{{iteration.date}}]({{iteration.url}}){:target="_blank"}{% if forloop.last != true %}, {% endif %}{% endfor %}
{%- endfor %}
{% endfor %}


### Guest Lectures

{% for lecture in site.data.teaching.guest_lectures -%}
  * ["{{lecture.title}}"]({{lecture.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}, {{lecture.course_number}} ({{lecture.course_name}}), *{{lecture.date}}*
{% endfor %}


### Before MIT

{% for position in site.data.teaching.before_mit -%}
  * {{position.role}}, *{{position.org}}, {{position.date}}*
{% endfor %}


## Publications & Preprints

[Publications by Topic](/research){:.button.button--secondary.button--pill.button--sm}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}

{% for year in site.data.papers.years %}
#### {{year}}
{% for paper in site.data.papers.papers -%}
{% if year == paper.year -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){:target="_blank"}, {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}){:target="_blank"}.
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

### Public Lectures

{% for talk in site.data.talks.public -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %} {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{%- endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){:target="_blank"}{% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Lecture Series & Schools

{% for talk in site.data.talks.schools -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %} {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{% endif %}
      {%- if talk.parts %} (
      {%- for part in talk.parts -%}
          {%if part.video %}[video]({{part.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %}{% if part.url %}**["{{part.title}}"]({{part.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{part.title}}"**{% endif %}
      {%- if forloop.last != true-%}, {% endif -%}{% endfor -%}
      )
      {%- endif -%},
   {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){:target="_blank"}{% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Colloquia

{% for talk in site.data.talks.colloquia -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %} {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{% endif %}, {{talk.event}}, *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Invited Talks

{% for talk in site.data.talks.invited -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %}{% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{% endif %}
    {%- if talk.collab %} (with {{talk.collab}}), {% else %}, {% endif %}
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){:target="_blank"}{% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Seminars

{% for talk in site.data.talks.seminars -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %}{% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{% endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Local Presentations

{% for talk in site.data.talks.local -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"}{% endif %}{% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% else %}**"{{talk.title}}"**{% endif %}, {{talk.event}}, *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Additional Events

{% for talk in site.data.talks.additional -%}
  * {%if talk.video %}[video]({{talk.video}}){:.button.button--primary.button--rounded.button--xs.button--outline-success}{:target="_blank"} {% endif %}{% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}}){:target="_blank"}**{% elsif talk.panelist %}**Panelist**{% elsif talk.convener %}**Convener**{% elsif talk.title %}**"{{talk.title}}"**{% else %}**No Talk**{% endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){:target="_blank"}{% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
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

{% for phd_thesis in site.data.advising.phd_theses %}
  * **{{phd_thesis.name}}**, "{{phd_thesis.title | default: "TBA"}}" ({{phd_thesis.advisor}}), *{{phd_thesis.date | default: "in progress"}}*
{%- endfor %}

### Academic Advising

{% for service in site.data.advising.academic_advising %}
  * **{% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}**, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


### External Ph.D. Examiner

{% for phd_thesis in site.data.advising.external_phd_theses %}
  * **{{phd_thesis.name}}**, "{{phd_thesis.title | default: "TBA"}}" ({{phd_thesis.advisor}}), *{{phd_thesis.org}}, {{phd_thesis.date | default: "in progress"}}*
{%- endfor %}

### External Mentoring

{% for mentoring in site.data.advising.external_mentoring %}
  * **{{mentoring.name}}**, {{mentoring.program}}, *{{mentoring.org}}, {{mentoring.dates}}*
{%- endfor %}




## Service

### Internal Service

#### MIT Faculty

{% for service in site.data.service.mit_faculty %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### MIT Physics

{% for service in site.data.service.mit_physics %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### MIT Laboratory for Nuclear Science

{% for service in site.data.service.mit_lns %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### MIT Center for Theoretical Physics

{% for service in site.data.service.mit_ctp %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### MIT Statistics and Data Science Center

{% for service in site.data.service.mit_sdsc %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### MIT International Science and Technology Initiatives

{% for service in site.data.service.mit_misti %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


#### Before MIT

{% for service in site.data.service.before_mit %}
  * {% if service.url %}[{{service.name}}]({{service.url}}){:target="_blank"}{% else %}{{service.name}}{% endif %}, *{{service.dates}}*
{%- for detail in service.details %}
     * {{detail}}
{%- endfor %}
{%- endfor %}


### External Service


#### Workshop/Conference Organization


  * General Member, Aspen Center for Physics (Summer 2020-Summer 2025)
    * Liason, Winter Workshop, "Theoretical Physics for Machine Learning" (Winter 2023)
    * Organizer, Summer Workshop, "Interplay of Fundamental Physics and Machine Learning" (Summer 2022)
    * Nominations Committee (Summer 2021; Chair, Summer 2022; Ex officio, Summer 2023)
    * Summer Program Committee (Summer 2020)
  * Topical Convener in [Collider Phenomenology](https://snowmass21.org/theory/phenomenology){:target="_blank"}, [Snowmass Theory Frontier](https://snowmass21.org/theory/start){:target="_blank"} (July 2021, July 2022)
  * Organizer, GGI Workshop: "[Machine Learning at GGI](https://agenda.infn.it/event/32043/){:target="_blank"}" (August/September 2022)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Online Workshop:  "[Boost 2021](https://indico.cern.ch/event/1037559/){:target="_blank"}" (August 2021)
  * Advisory Committee, Heidelberg Workshop:  "[ML4Jets](https://indico.cern.ch/event/980214/){:target="_blank"}" (July 2021)
  * Organizer, Fermilab Remote Workshop:  "[CMS Open Data for Theorists](https://indico.cern.ch/e/CMSOpenDataForTheorists){:target="_blank"}" (September 2020)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Hamburg Workshop:  "[Boost 2020](https://indico.cern.ch/e/boost2020){:target="_blank"}" (July 2020)
  * Advisory Committee, Mainz Workshop:  "[Machine Learning for Particle Physics](https://indico.mitp.uni-mainz.de/event/199/){:target="_blank"}" (May 2020 → June 2021)
  * Advisory Committee, New York Workshop:  "[ML4Jets](https://indico.cern.ch/event/809820/){:target="_blank"}" (January 2020)
  * Local Organizing Committee, Boston Workshop:  "[Boost 2019](https://indico.cern.ch/e/boost2019){:target="_blank"}" (July 2019)
  * Advisory Committee, Paris Workshop:  "[Boost 2018](https://indico.cern.ch/e/boost2018){:target="_blank"}" (July 2018)
  * Local Organizing Committee, MIT Workshop: "[Rising Stars in Physics](https://physicsrisingstars.mit.edu/){:target="_blank"}" (April 2018)
  * Advisory Committee, Buffalo Workshop:  "Boost 2017" (July 2017)
  * Jet Convener, Les Houches Workshop:  "Physics at TeV Colliders" (June 2017)
  * Advisory Committee, Cleveland Workshop:  "BLV 2017" (May 2017)
  * Scientific Organizing Committee, Boston Workshop:  "Lattice for BSM Physics 2017" (April 2017)
  * Organizer, Aspen Center for Physics Workshop: "The LHC Awakens: A New Energy Frontier" (August 2016)
  * Advisory Committee, Zurich Workshop:  "Boost 2016" (July 2016)
  * Organizer, Galileo Galilei Institute Workshop: "Gearing up for LHC13" (Fall 2015)
  * Advisory Committee, Chicago Workshop:  "Boost 2015" (August 2015)
  * Jet Convener, Les Houches Workshop:  "Physics at TeV Colliders" (June 2015)
  * Advisory Committee, London Workshop:  "Boost 2014" (August 2014)
  * Organizer, Harvard/MIT Workshop: "Boston Jet Physics" (January 2014)
  * Advisory Committee, Flagstaff Workshop:  "Boost 2013" (August 2013)
  * Advisory Committee, Valencia Workshop:  "Boost 2012" (July 2012)
  * Program Committee, PANIC 2011: "Particle and Nuclei International Conference" (July 2011)
  * Organizer, Aspen Center for Physics Workshop: "Year One of the LHC" (July 2011)
  * Organizer, Aspen Center for Physics Conference: "New Data from the Energy Frontier" (February 2011)
  * Organizer, Harvard/MIT Workshop: "Boston Jet Physics" (January 2011)
  * Organizer, MIT/Berkeley Workshop: "Implications of First LHC Data" (August 2010)
  * Advisory Committee, Oxford University Workshop: "Boost 2010" (June 2010)

#### Scientific Advising

  * [High Energy Physics Advisory Panel (HEPAP)](https://science.osti.gov/hep/hepap){:target="_blank"}
    * Member, HEPAP, *August 2021 - March 2024*
    * Member, Particle Physics Project Prioritization Panel (P5), *December 2022 - October 2023*
    * ["The NSF AI Institute for Artificial Intelligence and Fundamental Interactions"](https://github.com/jdthaler/jdthaler.github.io/raw/main/talks/jthaler_2020_12_IAIFI_HEPAP_Overview.pdf){:target="_blank"}, [HEPAP Presentation](https://science.osti.gov/hep/hepap/Meetings/202012){:target="_blank"}, *December 2020*
    * ["The High Energy Physics Landscape in 2019"](https://github.com/jdthaler/jdthaler.github.io/raw/main/talks/jthaler_2019_05_HEPAP.pdf){:target="_blank"}, [HEPAP Presentation](https://science.osti.gov/hep/hepap/Meetings/201905){:target="_blank"}, *May 2019*
  * Sakurai Dissertation Award Selection Committee, American Physical Society, *Fall 2016, Fall 2022, Fall 2023; Chair: Fall 2023*
  * International Scientific Advisory Board, [AI for Science and Science for AI (AISSAI) Center](https://www.cnrs.fr/en/artificial-intelligence-science-science-artificial-intelligence-aissai-center){:target="_blank"}, French CNRS, *2022 - present*
  * International Advisory Committee, Grant-in-Aid for Transformative Research Areas, JSPS/MEXT Japan, *2022 - 2026*
  * Science Advisory Board, USQCD Collaboration, *Spring 2013 - Fall 2016*
  * LHC Theory Initiative, Fellowship Selection Committee, *Fall 2013 - Fall 2014; Chair: Fall 2014*

#### Peer Review

  * [Journal of High Energy Physics](https://jhep.sissa.it/){:target="_blank"}
    * Editorial Board, *Fall 2019 - present*
  * [SciPost Physics](https://scipost.org/SciPostPhys){:target="_blank"}
    * Editorial College, *Fall 2019 - present*
  * Frontiers of Artificial Intelligence
    * Co-Topic Editor, ["Efficient AI in Particle Physics and Astrophysics"](https://www.frontiersin.org/research-topics/19095/efficient-ai-in-particle-physics-and-astrophysics){:target="_blank"}, *Spring 2022*
  * Physical Review Letters
  * Physical Review D
  * Journal of Cosmology and Astroparticle Physics
  * Physics of the Dark Universe
  * Nuclear Physics B
  * Physics Letters B
  * European Physical Journal C
  * Journal of Physics G
  * Physics Reports
  * Annals of Physics
  * Particle Data Group

#### Funding Agency Review 

  * U.S. Department of Energy
  * National Science Foundation
  * European Research Council
  * Heising-Simons Foundation
  * Research Corporation for Science Advancement (Cottrell)
  * The Royal Society
  * Swiss National Science Foundation
  * Natural Sciences and Engineering Research Council of Canada
  * Israel Science Foundation
  * Netherlands Organisation for Scientific Research
  * German Academic Exchange Service (DAAD)
  * French National Research Agency
  * Hungarian National Research, Development, and Innovation Office

## Public Engagement
 
[Engagement Portfolio](/engagement){:.button.button--secondary.button--pill.button--sm} 
[IMDb](http://www.imdb.com/name/nm6007880/){:.button.button--secondary.button--pill.button--sm}{:target="_blank"}
 
{% for entry in site.data.public.entries %}
  * {{entry.markdown}}
{%- endfor %}
  * Appearance in Documentary Film, **["Particle Fever"](https://www.imdb.com/title/tt1385956/){:target="_blank"}**, 2013 
    * After film Q&A, BOOST 2015 Workshop Public Event, August 2015
    * After film Q&A, MIT Lecture Series Committee, September 2014
    * After film Q&A, Portsmouth Music Hall, May 2014
  * **TheoryNet**, High School Physics Outreach
    * Scott Goelzer, Coe-Brown Northwood Academy (Fall 2020-Present)
    * Elaine Picard, Concord-Carlisle High School (Fall 2015-Spring 2016, Spring 2017, Spring 2020)
    * Michael Wadness, Medford High School  (Fall 2012-Spring 2015, Spring 2018, Spring 2022)
    * Michael Hirsh, Needham High School  (Spring 2010-Spring 2012)
  * Additional Outreach
    * Hiroko Kaczmarek, Cambridge Rindge and Latin School (May 2021)
  * High School Job Shadowing
    * Audrey Grimes (York High School, December 2017)
    * Cole Gilbert (Traip Academy, November 2017)    
    * Joshua Reynolds (York High School, April 2016)
    * Edward Bengtson (York High School, April 2014)

## Graphic Design

[Design Portfolio](/personal#graphic-design){:.button.button--secondary.button--pill.button--sm}

  * **[Banner Design](design/jthaler_IAIFI_Banner.jpg){:target="_blank"}**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](http://www.iaifi.org/){:target="_blank"}, *August 2020*  (based on artwork by [agsandrew](https://agsandrew.myportfolio.com/{:target="_blank"}) - stock.adobe.com)
  * **[Logo Design](design/jthaler_IAIFI_Logo.pdf){:target="_blank"}**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](http://www.iaifi.org/){:target="_blank"}, *August 2020*
  * **[Logo Design](design/jthaler_OmniFold_Logo.pdf){:target="_blank"}**, [OmniFold](https://github.com/ericmetodiev/OmniFold/){:target="_blank"}, *MIT, November 2019*
  * **[Poster Design](design/jthaler_BOOST2019_Poster.pdf){:target="_blank"}** ([with bleeds](design/jthaler_BOOST2019_Poster_Bleed.pdf){:target="_blank"}), [BOOST 2019 Workshop](https://indico.cern.ch/e/boost2019), *MIT, July 2019*
  * **[Logo Design](design/jthaler_ABRALogo_Large.pdf){:target="_blank"}** ([Alt.](design/jthaler_ABRALogo_Medium.pdf){:target="_blank"}, [A.](design/jthaler_ABRALogo_Small.pdf){:target="_blank"}), [ABRACADABRA Experiment](http://abracadabra.mit.edu/), *MIT, August 2017*
  * **[Logo Design](design/jthaler_MOD_Logo.pdf){:target="_blank"}** ([Event Display](design/jthaler_MOD_EventDisplay.pdf){:target="_blank"}), MIT Open Data, *MIT, July 2015*
  * **[Logo Design](design/jthaler_DarkLight_Logo.pdf){:target="_blank"}**, [DarkLight Experiment](http://dmtpc.mit.edu/DarkLight/){:target="_blank"}, *MIT, September 2010*


## Memberships

{% for membership in site.data.service.memberships %}
  * **[{{membership.name}}]({{membership.url}}){:target="_blank"}** 
{%- endfor %}


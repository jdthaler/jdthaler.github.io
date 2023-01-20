---
layout: article
title: Curriculum Vitae
aside:
  toc: true

---

[Short CV](about#short-cv){:.button.button--outline-primary.button--pill.button--sm}
[PDF CV (May 2022)](pdfs/jthaler_CV_2022_May.pdf){:.button.button--outline-primary.button--pill.button--sm}

## Jesse Diaz Thaler


* **Wires**
  *  *Email:* [jthaler@mit.edu](mailto: jthaler@mit.edu) 
  *  *Web:* [http://www.jthaler.net/](http://www.jthaler.net) 
  *  *Zoom:*  [https://mit.zoom.us/my/jthaler](https://mit.zoom.us/my/jthaler) 
* **Digits**
  * *Office:* (617) 253-3713 
  * *Cell:* (617) 642-8622
  * *Fax:* (617) 253-8674 
* **Snails**
  * Jesse Thaler\\
    MIT Center for Theoretical Physics\\
    77 Massachusetts Ave, [6-318](http://whereis.mit.edu/?go=6)\\
    Cambridge, MA 02139

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
    * Director, [NSF Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](https://iaifi.org/), *August 2020 - Present*
 * **Affiliations**
   * [MIT Center for Theoretical Physics (CTP)](http://ctp.mit.edu/) and [Laboratory for Nuclear Science (LNS)](http://web.mit.edu/lns/), *January 2010 - Present*
   * [MIT Statistics and Data Science Center (SDSC)](https://stat.mit.edu/) and [Institute for Data, Systems, and Society (IDSS)](https://idss.mit.edu/), *January 2020 - Present*

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
    * Ph.D. Physics, "[Symmetry Breaking at the Energy Frontier](http://inspirehep.net/record/738871)", *June 2006* 
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
  * **[{{award.name}}]({{award.url}})**, *{{award.org}}*, *{{award.date}}*
  {%- else %}
  * **{{award.name}}**, *{{award.org}}*, *{{award.date}}*
  {%- endif %}
{%- endfor %}

## Mentoring

[Research Group](group){:.button.button--outline-primary.button--pill.button--sm}
[Joining My Group](join){:.button.button--outline-primary.button--pill.button--sm}

### Postdoctoral Researchers

{% for person in site.data.mentoring.postdocs -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {{person.at[0].title}}, *{{person.at[0].dates}}* {% if person.at[1] %}; {{person.at[1].title}}, *{{person.at[1].dates}}* {% endif %}
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
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}Ph.D.{% else %}anticipated Ph.D.{% endif %} {{person.date}}
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
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}M.Eng.{% else %}anticipated M.Eng.{% endif %} {{person.date}}
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
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis or person.graduated %}B.S.{% else %}anticipated B.S.{% endif %} {{person.date}}
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
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {{person.program}}, *{{person.dates}}*
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

  * **8.398 --- Selected Topics in Graduate Physics**
    * Instructor:  [Spring 2021](https://canvas.mit.edu/courses/7673), [Fall 2021](https://canvas.mit.edu/courses/11329), [Spring 2022](https://canvas.mit.edu/courses/13866), [Fall 2022](https://canvas.mit.edu/courses/16823), [Spring 2023](https://canvas.mit.edu/courses/19643)

  * **8.03 --- Physics III, Waves & Vibrations**
    * Recitation:  [Fall 2020](https://canvas.mit.edu/courses/4560)

  * **8.044 --- Statistical Physics I**
    * Recitation:  [Spring 2020](http://stellar.mit.edu/S/course/8/sp20/8.044/)
  
  * **8.831 --- Supersymmetric Quantum Field Theories**
      * Lecture:  [Spring 2017](http://stellar.mit.edu/S/course/8/sp17/8.831/), [Fall 2019](http://stellar.mit.edu/S/course/8/fa19/8.831/)

  * **8.051 --- Quantum Mechanics II (MITx-based)**
    * Instructor:  [Spring 2018](http://stellar.mit.edu/S/course/8/sp18/8.051/)

  * **8.033 --- Relativity**
    * Lecture: [Fall 2017](http://stellar.mit.edu/S/course/8/fa17/8.033/)
    * Recitation:  [Fall 2016](http://stellar.mit.edu/S/course/8/fa16/8.033/)

  * **8.02 --- Physics II, Electricity & Magnetism** 
    * TEAL:  [Spring 2014](http://stellar.mit.edu/S/course/8/sp14/8.02/), [Spring 2015](http://stellar.mit.edu/S/course/8/sp15/8.02/), [Spring 2016](http://stellar.mit.edu/S/course/8/sp16/8.02/)

  * **8.012 --- Physics I, Classical Mechanics** 
    * Recitation: [Fall 2014](http://stellar.mit.edu/S/course/8/fa14/8.012/)

  * **8.06 --- Quantum Mechanics III**
    * Lecture: [Spring 2011](http://stellar.mit.edu/S/course/8/sp11/8.06/), [Spring 2012](http://stellar.mit.edu/S/course/8/sp12/8.06/), [Spring 2013](http://stellar.mit.edu/S/course/8/sp13/8.06/)
    * Recitation: [Spring 2010](http://stellar.mit.edu/S/course/8/sp10/8.06/)

  * **8.05 --- Quantum Mechanics II**
    * Recitation: [Fall 2010](http://stellar.mit.edu/S/course/8/fa10/8.05/), [Fall 2012](http://stellar.mit.edu/S/course/8/fa12/8.05/)

### Guest Lectures

  * ["Collision Course"](http://www.jthaler.net/talks/jthaler_2022_01_EnergyFlowNetworks_8_S50.pdf), 8.S50 (Computational Data Science in Physics), *IAP 2022*
  * ["Collision Course"](http://www.jthaler.net/talks/jthaler_2021_01_EnergyFlowNetworks_8_S50.pdf), 8.S50 (Computational Data Science in Physics), *IAP 2021*
  * ["The Hidden Geometry of Particle Collisions"](http://www.jthaler.net/talks/jthaler_2020_11_HiddenGeometry_8_398.pdf), 8.398 (Selected Topics in Graduate Physics), *Fall 2020*
  * ["One Lecture on Jets"](http://www.jthaler.net/talks/jthaler_2019_11_JetLecture_8_701.pdf), 8.701 (Introduction to Nuclear and Particle Physics), *Fall 2019*
  * ["One Lecture on Jets"](http://www.jthaler.net/talks/jthaler_2019_10_JetLecture_8_811.pdf), 8.811 (Particle Physics II), *Fall 2019*

### Before MIT

  * Teaching Fellow, Widely Applied Physics (Nima Arkani-Hamed), *Harvard University, Fall 2005*
  * Teaching Assistant, Linear Algebra (Thomas Banchoff), *Brown University, Spring 2001*
  * Math/Physics Tutor, *Brown University, 1999 - 2000*
  * Classroom Assistant, Algebra I and II, *Textron/Chamber of Commerce Charter High School, Providence, RI, Fall 1999*


## Publications & Preprints

[Publications by Topic](research){:.button.button--outline-primary.button--pill.button--sm}
[Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1){:.button.button--outline-primary.button--pill.button--sm}
[arXiv](http://arxiv.org/a/thaler_j_1){:.button.button--outline-primary.button--pill.button--sm}
[ORCID](https://orcid.org/0000-0002-2406-8160){:.button.button--outline-primary.button--pill.button--sm}
[Google Scholar](https://scholar.google.com/citations?user=djDP5SMAAAAJ){:.button.button--outline-primary.button--pill.button--sm}

{% for year in site.data.papers.years %}
#### {{year}}
{% for paper in site.data.papers.papers -%}
{% if year == paper.year -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{%- endif %}
{% endfor %}
{% endfor %}


### Conference Proceedings

{% for paper in site.data.papers.conference -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} {% if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{% endfor%}

### Incidental Authorship

{% for paper in site.data.papers.incidental -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){% endif %}
    {%- if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}){% endif %}
    {%- if paper.arxiv and paper.doi or paper.journal_url-%}, {% endif %}
    {%- if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}){% endif %}.
{% endfor %}


## Presentations

### Colloquia

{% for talk in site.data.talks.colloquia -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{% endif %}, {{talk.event}}, *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Public Lectures

{% for talk in site.data.talks.public -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{%- endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}


### Lecture Series & Schools

{% for talk in site.data.talks.schools -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{% endif %}
      {%- if talk.parts %} (
      {%- for part in talk.parts -%}
        {% if part.url %}**[{{part.title}}]({{part.url}})**{% else %}**{{part.title}}**{% endif %}
      {%- if forloop.last != true-%}, {% endif -%}{% endfor -%}
      )
      {%- endif -%},
   {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}


### Invited Talks

{% for talk in site.data.talks.invited -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{% endif %}
    {%- if talk.collab %} (with {{talk.collab}}), {% else %}, {% endif %}
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Local Presentations

{% for talk in site.data.talks.local -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{% endif %}, {{talk.event}}, *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Seminars

{% for talk in site.data.talks.seminars -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% else %}**"{{talk.title}}"**{% endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}

### Additional Events

{% for talk in site.data.talks.additional -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url | prepend: "https://github.com/jdthaler/jdthaler.github.io/raw/main/"}})**{% elsif talk.panelist %}**Panelist**{% elsif talk.convener %}**Convener**{% elsif talk.title %}**"{{talk.title}}"**{% else %}**No Talk**{% endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} `virtual` {% endif %}
{% endfor %}


## Research Grants

  * AI Research Institute, "[Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)](http://iaifi.org/)", *National Science Foundation, 2020-2025* ($20M)
  * MIT-Israel Zuckerman STEM Fund Award (with Tracy Slatyer, Tomer Volansky, and Yotam Soreq), "The Quest for Dark Matter Interactions", *MIT International Science and Technology Initiative, 2020-2021* ($25.5k)
  * PIER Hamburg-MIT Seed Project (with Gregor Kasieczka, Phil Harris, Andreas Hinzmann, Roman Kogler, Iain Stewart), "Probing the Standard Model with Jet Substructure", *Partnership for Innovation, Education and Research, 2019-2020* (€17k)
  * Quantum Information Science (QuantISED) Award (with Aram Harrow), "[Quantum Algorithms for Collider Physics](https://doi.org/10.2172/1688696)", *U.S. Department of Energy, Office of High Energy Physics, 2018-2020* ($264k)
  * Simons Fellowship, "Theoretical Investigations In and Beyond the Standard Model", *Simons Foundation, 2018-2019* ($143k)
  * Comparative Review Funding Award, "[Boosting the Search for New Physics at the Frontiers](https://doi.org/10.2172/1361051)", *U.S. Department of Energy, Office of High Energy Physics, 2016-2017* ($120k)
  * The Charles E. Reed Faculty Initiatives Fund, "Boosting Jet Physics with Archival Collider Data", *MIT Research Support Committee, 2015-2017* ($75k) 
  * MIT-Belgium Seed Fund Award (with Fabio Maltoni), "Beyond the Standard Model at the LHC", *MIT International Science and Technology Initiative, 2013-2014* ($23.1k)
  * Sloan Research Fellowship, *Alfred P. Sloan Foundation, 2013-2016* ($50k)
  * Global Seed Fund Award (with Iain Stewart, Andre Hoang, and Gavin Salam), "Probing a New Energy Frontier with Jets at the Large Hadron Collider", *MIT International Science and Technology Initiative, 2012-2013* ($15k)
  * Early Career Research Award, "[Interpreting New Data from the Energy Frontier](https://doi.org/10.2172/1326460)", *U.S. Department of Energy, Office of Science, 2011-2016* ($750k)
  * Cooperative Research Agreement, “Laboratory for Nuclear Science, High Energy Physics Program: Task C, Center for Theoretical Physics”, *U.S. Department of Energy, Office of Science*

## Service

### Internal Service

#### Ph.D. Thesis Committees

{% for phd-thesis in site.data.service.phd-theses %}
  * **{{phd-thesis.name}}**, "{{phd-thesis.title | default: "TBA"}}" ({{phd-thesis.advisor}}), *{{phd-thesis.date | default: "in progress"}}*
{%- endfor %}

#### MIT Faculty

  * [MIT Faculty Committee on Curricula](https://registrar.mit.edu/faculty-curriculum-support/faculty-curriculum-committees/committee-curricula) (Fall 2017-Spring 2020)
  * MIT First-Year Advisor (Fall 2019-Spring 2020)
    * Class of 2023:  Richter Brzeski, Megha Maran, Catalina Monsalve Rodriguez, Dylan Weber

#### MIT Physics

  * MIT Physics Ad Hoc Committee on Graduate Student Professional Development (Spring 2022)
  * MIT Physics Graduate Admissions Committee (Spring 2021)
  * MIT Physics [Communic.8 Faculty Liaison](https://piazza.com/mit/fall2020/communic8) (Fall 2020-present)
  * MIT Physics Qualifying Exam, Written Exam Grading Committee (January 2020)
  * MIT Physics Promotion Committee (Fall 2019, Fall 2020, Fall 2021, Fall 2022, Chair: Fall 2020, Fall 2021, Fall 2022)
  * MIT Physics [Pappalardo Fellowships Executive Committee](http://web.mit.edu/Physics/research/pappalardo/index.html) (Fall 2016-Fall 2017)
  * MIT Physics Colloquium Committee (Spring 2010-Spring 2014, Chair: Fall 2012-Spring 2014)
  * MIT Physics Graduate Academic Advisor (Fall 2017-present)
    * Anticipated Ph.D. 2025:  Ryan Abbott
    * Anticipated Ph.D. 2024:  Bruno Scheihing Hitschfeld, Stella Schindler
    * Anticipated Ph.D. 2022:  Eric Anschuetz, Samuel Leutheusser, Gregory Ridgway, Annie Wei, Ryan Weller
    * Ph.D. 2020:  Jasmine Brewer
  * MIT Physics Undergraduate Academic Advisor (Fall 2011-present)
    * Class of 2024:  Omar Abdelghani, Chirag Falor, Lily Moseni, Dylan Raphael, David Suarez, Chris Viets
    * Class of 2018/2019/2020:  Robert Arnott, Zachary Bogorad, Hannah Field, Rodmy Paredes Alfaro, Saranesh Prembabu, Joshua Rhodes, Kevin Tang, Michael Winer
    * Class of 2014/2015:  Allison Christian, Jay Lawhorn, Joseph Perricone, Jeffrey Prouty, Melih Ucer, Pranjal Vachaspati, Prashanth Venkataram (& Grace Krusell, David Luciano, Netia McCray, Maxwell Plaut)
  * MIT Physics Qualifying Exam, Part III Committee (Spring 2015-Spring 2017)
  * MIT Physics Qualifying Exam, Part II Committee (Spring 2012-Fall 2014, Chair: Fall 2013-Spring 2014)
  * MIT Physics Qualifying Exam, Part II Grading Committee (September 2010)

#### MIT Laboratory for Nuclear Science

  * MIT LNS Advisory Group (Fall 2017, Spring 2020-present)
  * MIT LNS Colloquium Committee (Fall 2015-Spring 2018, Chair:  Fall 2017-Spring 2018)


#### MIT Center for Theoretical Physics

  * MIT CTP Oral Qualifying Exam Committee (Fall 2022)
  * MIT CTP Faculty Mentor (April 2021-present)
  * MIT CTP Faculty Search Committee (Fall 2017, Fall 2019, Fall 2021; Chair: Fall 2019)
  * MIT CTP Deputy Group Leader in High-Energy Physics (Spring 2020-present)
  * MIT CTP Visitor Coordinator (Fall 2016-present)
  * MIT CTP Nuclear/Particle Seminar Committee (Fall 2010-Fall 2016, Fall 2020-Spring 2021, Fall 2022)
  * MIT CTP Postdoc Selection Committee (Fall 2009-present)

#### MIT Statistics and Data Science Center

  * [MIT Physics, Statistics, and Data Science (PhysSDS) Committee](https://web.mit.edu/physics/current/graduate/psds_phd.html) (Co-Chair: Fall 2020)

#### MIT International Science and Technology Initiatives


  * MISTI Global Seed Funds Evaluation Committee (Fall 2012, Fall 2013, Fall 2014)


#### Before MIT

  * Berkeley CTP Particle Seminar Organizer (2007-2009)
  * Miller Symposium Committee (2008-2009)

### External Service

#### External Ph.D. Examiner

{% for phd-thesis in site.data.service.external-phd-theses %}
  * **{{phd-thesis.name}}**, "{{phd-thesis.title | default: "TBA"}}" ({{phd-thesis.advisor}}), *{{phd-thesis.uni}}, {{phd-thesis.date | default: "in progress"}}*
{%- endfor %}

#### External Mentoring

{% for mentoring in site.data.service.external-mentoring %}
  * **{{mentoring.name}}**, {{mentoring.program}}, *{{mentoring.uni}}, {{mentoring.date}}*
{%- endfor %}

#### Workshop/Conference Organization


  * General Member, Aspen Center for Physics (Summer 2020-Summer 2025)
    * Liason, Winter Workshop, "Theoretical Physics for Machine Learning" (Winter 2023)
    * Organizer, Summer Workshop, "Interplay of Fundamental Physics and Machine Learning" (Summer 2022)
    * Nominations Committee (Summer 2021; Chair, Summer 2022; Ex officio, Summer 2023)
    * Summer Program Committee (Summer 2020)
  * Topical Convener in [Collider Phenomenology](https://snowmass21.org/theory/phenomenology), [Snowmass Theory Frontier](https://snowmass21.org/theory/start) (July 2021)
  * Organizer, GGI Workshop: "[Machine Learning at GGI](https://agenda.infn.it/event/32043/)" (August/September 2022)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Online Workshop:  "[Boost 2021](https://indico.cern.ch/event/1037559/)" (August 2021)
  * Advisory Committee, Heidelberg Workshop:  "[ML4Jets](https://indico.cern.ch/event/980214/)" (July 2021)
  * Organizer, Fermilab Remote Workshop:  "[CMS Open Data for Theorists](https://indico.cern.ch/e/CMSOpenDataForTheorists)" (September 2020)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Hamburg Workshop:  "[Boost 2020](https://indico.cern.ch/e/boost2020)" (July 2020)
  * Advisory Committee, Mainz Workshop:  "[Machine Learning for Particle Physics](https://indico.mitp.uni-mainz.de/event/199/)" (May 2020 → June 2021)
  * Advisory Committee, New York Workshop:  "[ML4Jets](https://indico.cern.ch/event/809820/)" (January 2020)
  * Local Organizing Committee, Boston Workshop:  "[Boost 2019](https://indico.cern.ch/e/boost2019)" (July 2019)
  * Advisory Committee, Paris Workshop:  "[Boost 2018](https://indico.cern.ch/e/boost2018)" (July 2018)
  * Local Organizing Committee, MIT Workshop: "[Rising Stars in Physics](https://physicsrisingstars.mit.edu/)" (April 2018)
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

  * [High Energy Physics Advisory Panel (HEPAP)](https://science.osti.gov/hep/hepap)
    * Member, HEPAP, *August 2021 - March 2024*
    * Member, Particle Physics Project Prioritization Panel (P5), *December 2022 - October 2023*
    * ["The NSF AI Institute for Artificial Intelligence and Fundamental Interactions"](http://www.jthaler.net/talks/jthaler_2020_12_IAIFI_HEPAP_Overview.pdf), [HEPAP Presentation](https://science.osti.gov/hep/hepap/Meetings/202012), *December 2020*
    * ["The High Energy Physics Landscape in 2019"](http://www.jthaler.net/talks/jthaler_2019_05_HEPAP.pdf), [HEPAP Presentation](https://science.osti.gov/hep/hepap/Meetings/201905), *May 2019*
  * Sakurai Dissertation Award Selection Committee, American Physical Society (Fall 2016, Fall 2022)
  * International Scientific Advisory Board, [AI for Science and Science for AI (AISSAI) Center](https://www.cnrs.fr/en/artificial-intelligence-science-science-artificial-intelligence-aissai-center), French CNRS, *2022-present*
  * International Advisory Committee, Grant-in-Aid for Transformative Research Areas, JSPS/MEXT Japan, *2022-2026*
  * Science Advisory Board, USQCD Collaboration (Spring 2013-Fall 2016)
  * LHC Theory Initiative, Fellowship Selection Committee (Fall 2013-Fall 2014, Chair: Fall 2014)

#### Peer Review

  * [Journal of High Energy Physics](https://jhep.sissa.it/)
    * Editorial Board, *Fall 2019 - present*
  * [SciPost Physics](https://scipost.org/SciPostPhys)
    * Editorial College, *Fall 2019 - present*
  * Frontiers of Artificial Intelligence
    * Co-Topic Editor, ["Efficient AI in Particle Physics and Astrophysics"](https://www.frontiersin.org/research-topics/19095/efficient-ai-in-particle-physics-and-astrophysics), *Spring 2022*
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
 
[Engagement Portfolio](public){:.button.button--outline-primary.button--pill.button--sm} 
[IMDb](http://www.imdb.com/name/nm6007880/){:.button.button--outline-primary.button--pill.button--sm}
 
{% for entry in site.data.public.entries %}
  * {{entry.markdown}}
{%- endfor %}
  * Appearance in Documentary Film, **["Particle Fever"](https://www.imdb.com/title/tt1385956/)**, 2013 
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

[Design Portfolio](public#graphic-design){:.button.button--outline-primary.button--pill.button--sm}

  * **[Banner Design](design/jthaler_IAIFI_Banner.jpg)**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](http://www.iaifi.org/), *August 2020*  (based on artwork by [agsandrew](https://agsandrew.myportfolio.com/) - stock.adobe.com)
  * **[Logo Design](design/jthaler_IAIFI_Logo.pdf)**, [NSF AI Institute for Artificial Intelligence and Fundamental Interactions](http://www.iaifi.org/), *August 2020*
  * **[Logo Design](design/jthaler_OmniFold_Logo.pdf)**, [OmniFold](https://github.com/ericmetodiev/OmniFold/), *MIT, November 2019*
  * **[Poster Design](design/jthaler_BOOST2019_Poster.pdf)** ([with bleeds](design/jthaler_BOOST2019_Poster_Bleed.pdf)), [BOOST 2019 Workshop](https://indico.cern.ch/e/boost2019), *MIT, July 2019*
  * **[Logo Design](design/jthaler_ABRALogo_Large.pdf)** ([Alt.](design/jthaler_ABRALogo_Medium.pdf), [A.](design/jthaler_ABRALogo_Small.pdf)), [ABRACADABRA Experiment](http://abracadabra.mit.edu/), *MIT, August 2017*
  * **[Logo Design](design/jthaler_MOD_Logo.pdf)** ([Event Display](design/jthaler_MOD_EventDisplay.pdf)), MIT Open Data, *MIT, July 2015*
  * **[Logo Design](design/jthaler_DarkLight_Logo.pdf)**, [DarkLight Experiment](http://dmtpc.mit.edu/DarkLight/), *MIT, September 2010*


## Memberships

{% for membership in site.data.service.memberships %}
  * **[{{membership.name}}]({{membership.url}})** 
{%- endfor %}


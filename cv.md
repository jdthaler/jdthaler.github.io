---
layout: article
title: Full CV
aside:
  toc: true

---


[PDF Version](pdfs/jthaler_CV_2022_May.pdf) (updated May 2022)

## Jesse Diaz Thaler



* **Wires**
  *  *Email:* [jthaler@mit.edu](jthaler@mit.edu) 
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
 * **Portals**
   * [MIT Physics](http://web.mit.edu/physics/people/faculty/thaler_jesse.html)
   * [Inspire](http://inspirehep.net/author/profile/Jesse.Thaler.1)
   * [arXiv](http://arxiv.org/a/thaler_j_1)
   * [ORCID](https://orcid.org/0000-0002-2406-8160)
   * [Wikipedia](https://en.wikipedia.org/wiki/Jesse_Thaler)
   * [IMDb](http://www.imdb.com/name/nm6007880/)


#### Research in Theoretical Particle Physics

{% for theme in site.data.research.themes %}  * **[{{theme.title}}](research.html#{{theme.key}})**
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

{% for award in site.data.cv_awards.awards -%}
  {%- if award.url %}
  * **[{{award.name}}]({{award.url}})**, *{{award.org}}*, *{{award.date}}*
  {%- else %}
  * **{{award.name}}**, *{{award.org}}*, *{{award.date}}*
  {%- endif %}
{%- endfor %}

## Mentoring

### Postdoctoral Researchers

{% for person in site.data.cv_mentoring.postdocs -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {{person.at[0].title}}, *{{person.at[0].dates}}* {% if person.at[1] %} ; {{person.at[1].title}}, *{{person.at[1].dates}}* {% endif %}
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

{% for person in site.data.cv_mentoring.phd_students -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}Ph.D.{% else %}anticipated Ph.D.{% endif %} {{person.date}}
  {%- if person.thesis %}
      * Thesis: "{{person.thesis}}"  {% if person.joint %} (with {{person.joint}}) {% endif %} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[0] %}
      * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}

### M.Eng. Students

{% for person in site.data.cv_mentoring.meng_students -%}
  {% if person.url %}  * **[{{person.name}}]({{person.url}})**,{% else %}  * **{{person.name}}**,{% endif %} {% if person.thesis %}M.Eng.{% else %}anticipated M.Eng.{% endif %} {{person.date}}
  {%- if person.thesis %}
      * Thesis: "{{person.thesis}}"  {% if person.joint %} (with {{person.joint}}) {% endif %} {% endif %}
  {%- if person.awards %}{% for award in person.awards %}
      * {{award.name}}, *{{award.org}}, {{award.date}}*  
  {%- endfor %}{% endif %}
  {%- if person.after[0] %}
      * After MIT: {{person.after[0].title}}, *{{person.after[0].org}}* {% endif %}
  {%- if person.after.size > 1 %}
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


### B.S. Students

{% for person in site.data.cv_mentoring.bs_students -%}
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
      * Currently: {{person.after[-1].title}}, *{{person.after[-1].org}}* {% endif %}
{% endfor %}


### Visiting Students/Postdocs

{% for person in site.data.cv_mentoring.visitors -%}
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
    * Instructor:  [Spring 2021](https://canvas.mit.edu/courses/7673), [Fall 2021](https://canvas.mit.edu/courses/11329), [Spring 2022](https://canvas.mit.edu/courses/13866), [Fall 2022](https://canvas.mit.edu/courses/16823), Spring 2023

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

  * ["Collision Course"](http://www.jthaler.net/talks/jthaler_2022_01_EnergyFlowNetworks_8_S50.pdf), 8.S50 (Computational Data Science in Physics), *IAP 2021*
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

{% for year in site.data.cv_papers.years %}
#### {{year}}
{% for paper in site.data.cv_papers.papers -%}
{% if year == paper.year -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{%- endif %}
{% endfor %}
{% endfor %}


### Conference Proceedings

{% for paper in site.data.cv_papers.conference -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}), {% endif %} {% if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}), {% endif %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}).
{% endfor%}

### Incidental Authorship

{% for paper in site.data.cv_papers.incidental -%}
  * **{{paper.title}}**. \\
    {{paper.authors}}.\\
    {% if paper.doi %}  [{{paper.journal}}](https://doi.org/{{paper.doi}}){% endif %}
    {%- if paper.journal_url %}  [{{paper.journal}}]({{paper.journal_url}}){% endif %}
    {%- if paper.arxiv and paper.doi or paper.journal_url-%}, {% endif %}
    {%- if paper.arxiv %} [arXiv:{{paper.arxiv}}](https://arxiv.org/abs/{{paper.arxiv}}){% endif %}.
{% endfor %}


## Presentations

### Colloquia

{% for talk in site.data.cv_talks.colloquia -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url}})**{% else %}**"{{talk.title}}"**{% endif %}, {{talk.event}}, *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} (Virtual Talk) {% endif %}
{% endfor %}

### Public Lectures

{% for talk in site.data.cv_talks.public -%}
  * {% if talk.url %}**["{{talk.title}}"]({{talk.url}})**{% else %}**"{{talk.title}}"**{% endif %},
    {% if talk.event_url %}[{{talk.event}}]({{talk.event_url}}){% else %}{{talk.event}}{% endif %},
    *{{talk.org}}, {{talk.date}}*
    {%- if talk.virtual %} (Virtual Talk) {% endif %}
{% endfor %}


### Lecture Series & Schools

  * "[[http://www.jthaler.net/talks/jthaler_2022_09_Perimeter_TableTop.pdf|The Standard Model]]", [[https://events.perimeterinstitute.ca/event/14/|School on Table-Top Experiments for Fundamental Physics]], //Perimeter Institute, September 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_03_DarkMatter_LL.pdf|Confronting the Invisible Universe]]", Intro to Modern Physics, //MIT Lincoln Labs, March 2022// 
  * "QCD & Collider Physics" ([[http://www.jthaler.net/talks/jthaler_2020_01_GGI_QCDCollider_Lecture1.pdf|Overview and Inspiration]], [[http://www.jthaler.net/talks/jthaler_2020_01_GGI_QCDCollider_Lecture2.pdf|From Diagrams to Cross Sections]], [[http://www.jthaler.net/talks/jthaler_2020_01_GGI_QCDCollider_Lecture3.pdf|An Introduction to Jets]], [[http://www.jthaler.net/talks/jthaler_2020_01_GGI_QCDCollider_Lecture4.pdf|A Case Study in Jet Substructure]]), //[[http://www.ggi.infn.it/ggilectures/ggilectures2020/| GGI Lectures on the Theory of Fundamental Interactions]], Florence, January 2020//
  * "Collider Physics" ([[http://www.jthaler.net/talks/jthaler_2018_07_Cargese_JetLecture1.pdf|Ingredients and Kinematics]], [[http://www.jthaler.net/talks/jthaler_2018_07_Cargese_JetLecture2.pdf|From Diagrams to Cross Sections]], [[http://www.jthaler.net/talks/jthaler_2018_07_Cargese_JetLecture3.pdf|An Introduction to Jets]]), //[[https://indico.desy.de/indico/event/18951/overview|Cargese 2018 International Summer School]], Corsica, July 2018//
  * [[http://www.jthaler.net/talks/jthaler_2017_01_Japan_Lecture1.pdf|"Introduction to Jet Substructure at the LHC"]], [[http://www.jthaler.net/talks/jthaler_2017_01_Japan_Lecture2.pdf|"A New Angle on Jet Substructure"]], [[http://www.jthaler.net/talks/jthaler_2017_01_Japan_Lecture3.pdf|"Introduction to Jet Physics from QCD"]], [[http://www.jthaler.net/talks/jthaler_2017_01_Japan_Lecture4.pdf|"Jets at the Frontier of Perturbative QCD"]], //Theoretical and Experimental Issues on Jet Structure at Hadron Colliders, Kavli IMPU and KEK, January 2017//
  * "Jet Physics" ([[http://www.jthaler.net/talks/jthaler_2016_07_MITP_Lecture1.pdf|Introduction to Jets]], [[http://www.jthaler.net/talks/jthaler_2016_07_MITP_Lecture2.pdf|Jet Algorithms]], [[http://www.jthaler.net/talks/jthaler_2016_07_MITP_Lecture3.pdf|The Soft/Collinear Limit of QCD]], [[http://www.jthaler.net/talks/jthaler_2016_07_MITP_Lecture4.pdf|The Substructure (R)evolution]]), //MITP Summer School, Mainz, July 2016//
  * "The Case for Jet Substructure", //Theorist of the Month, DESY, June 2014//
  * "Jet Substructure", //PiTP Summer School, Princeton, July 2013//
  * "Super-tricks for Superspace", //TASI Summer School, C.U. Boulder, June 2012//
  * "Little Lessons for a Little Higgs", //ICTP Winter School, Trieste, January 2012//
  * "Goldstini", "The Shape of Jets to Come", "Event Topologies for Early LHC", //Topic of the Week Lecture Series, Fermilab, November 2010//
  * "Entering the LHC Era", //MIT-CTP Felix Villars Theoretical Physics Retreat, January 2010//

### Invited Talks

  * "[[http://www.jthaler.net/talks/jthaler_2022_07_Snowmass_Pheno.pdf|The Frontiers of Phenomenological Theory]]", [[https://indico.fnal.gov/event/22303/|Snowmass Community Summer Study]], //U. Washington, Seattle, July 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_07_KIAS_Summer_School.pdf|Weak Supervision for the Strong Force]]", [[http://events.kias.re.kr/h/QUCAI2022/|QUC Summer School]], //KIAS, July 2022// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2022_06_PhysicsMeetsML.pdf|Weak Supervision for the Strong Force]]", [[http://www.physicsmeetsml.org/posts/sem_2022_06_01/|Physics Meets ML]], //Virtual, June 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_03_Brown_Snowmass.pdf|Machine Learning in Collider Physics]]", [[https://indico.fnal.gov/event/52465/|Snowmass Energy Frontier Workshop]], //Brown, March 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_03_OT_Simons.pdf|Optimal Transport for QCD and Jets]]", [[http://scgp.stonybrook.edu/archives/31750|Flowing into the Future]], //Simons Center, Stony Brook, March 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_02_KITP_Snowmass_2022.pdf|Machine Learning for the Theory Frontier]]", [[https://www.kitp.ucsb.edu/activities/snowmass-c22|Snowmass Theory Frontier Conference]], //KITP, February 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2021_11_ISTLisbon.pdf|Collision Course:  Particle Physics meets Machine Learning]]", [[http://phdopendays.tecnico.ulisboa.pt|PhD Open Days]], //IST Lisbon, November 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_07_LISHEP_AI.pdf|Artificial Intelligence and Fundamental Physics]]", [[https://indico.cern.ch/event/879856/|LISHEP 2021]], //Brazil, July 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_06_Amsterdam_Master.pdf|Artificial Intelligence and High-Energy Physics]]", [[https://indico.cern.ch/event/1027683/|Master Your Physics]], //U. Amsterdam, June 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_06_CERN_Jets.pdf|Theory Perspective on Machine Learning for Jets ]]", [[https://indico.cern.ch/event/1009701/|Jets and their Substructure from LHC Data]], //CERN-TH Workshop, June 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_05_MITP_Lattice_QCD_ML.pdf|QCD and Jets through the Lens of Machine Learning]]", [[https://indico.mitp.uni-mainz.de/event/231/overview|Machine Learning Techniques in Lattice QCD]], //MITP Workshop, May 2021// (Virtual Talk) 
  * "[[http://www.jthaler.net/talks/jthaler_2021_05_ICLR_Simulation.pdf|Deep Learning for Collider Physics Simulation]]", [[https://simdl.github.io/schedule/|Deep Learning for Simulation (SimDL)]], //ICLR 2021 Workshop, May 2021// (Recorded Talk) 
  * "[[http://www.jthaler.net/talks/jthaler_2021_04_APS_April_AI.pdf|Artificial Intelligence and High-Energy Physics]]", [[https://meetings.aps.org/Meeting/APR21/Session/H02|Recent Advances in Theoretical Physics]], //APS April Meeting, April 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_03_KITP_ML_w_Dreyer.pdf|QCD and Jets through the Lens of Machine Learning]]" (with Frédéric Dreyer), [[https://www.kitp.ucsb.edu/activities/precision21|New Physics from Precision at High Energies]], //KITP, Santa Barbara, March 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_02_AAAS_AI_Theory.pdf|Artificial Intelligence for Physics Discovery: Theory Perspective]]", [[https://aaas.confex.com/aaas/2021/meetingapp.cgi/Paper/28417|AAAS Annual Meeting]], [[https://indico.cern.ch/event/1031957/|Session on Artificial Intelligence for Physics]], //February 2021// (Recorded Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_01_HKUST_HEP.pdf|Machine Learning for Fundamental Physics]]", [[https://indico.cern.ch/event/971970/|HKUST IAS Program on High Energy Physics]], //January 2021// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_12_IFT_Xmas.pdf|Collider Physics and Machine Learning]]", [[https://workshops.ift.uam-csic.es/Xmas20|XXVI IFT Christmas Workshop]], //December 2020// (Virtual Talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_11_IAIFI_GeorgiaTech.pdf|Collision Course:  Artificial Intelligence meets Fundamental Interactions]]", IDEaS AI Seminar, //Georgia Tech, November 2020// (Virtual Talk)
  * [[http://www.jthaler.net/talks/jthaler_2019_07_QCDLHC_ML.pdf|"Deep Learning (and Deep Thinking) for QCD"]], [[https://indico.fnal.gov/event/19380/|QCD@LHC 2019]], //Buffalo, July 2019//
  * [[http://www.jthaler.net/talks/jthaler_2019_05_Pheno_ML.pdf|"Deep Learning (and Deep Thinking) in Collider Physics"]], [[https://indico.cern.ch/event/777988/|Pheno 2019]], //Pittsburg, May 2019//
  * [[http://www.jthaler.net/talks/jthaler_2019_02_Hamburg_Collision.pdf|"Collision Course: Particle Physics as a Machine-Learning Testbed"]], [[https://indico.cern.ch/event/765224/|Deep Learning in the Natural Sciences]], //University of Hamburg, February 2019//
  * [[http://www.jthaler.net/talks/jthaler_2019_01_AspenML_Collision.pdf|"Collision Course: Particle Physics as a Machine-Learning Testbed"]], [[https://sites.google.com/view/phys4ml|Theoretical Physics for Machine Learning]], //Aspen Center for Physics, January 2019//
  * [[http://www.jthaler.net/talks/jthaler_2018_11_ML4Jets_Intro.pdf|"A Theorist's Perspective on Machine Learning for Jets"]] (Opening Talk), [[https://indico.cern.ch/event/745718/|Machine Learning for Jet Physics]], //Fermilab, November 2018//
  * [[http://www.jthaler.net/talks/jthaler_2018_07_SUSY18_Jets.pdf|"New Improvements in Jet Physics"]], [[https://susy2018.ifae.es/|SUSY 2018]], //Barcelona, July 2018//
  * [[http://www.jthaler.net/talks/jthaler_2018_07_Boost2018_Summary.pdf|"Theory Summary"]] (Closing Talk), [[https://indico.cern.ch/e/boost2018|Boost 2018]], //Paris, July 2018//
  * [[http://www.jthaler.net/talks/jthaler_2018_06_CMSWeek_OpenData.pdf|"The Future is Open:  Jet Substructure with CMS Public Data"]], CMS Week, // CERN, June 2018//
  * [[http://www.jthaler.net/talks/jthaler_2017_06_CERN_OpenData.pdf|"The Future is Open:  Jet Substructure with CMS Public Data"]], [[https://indico.cern.ch/event/572734/|LHC and the Standard Model: Physics and Tools]], // CERN, June 2017//
  * [[http://www.jthaler.net/talks/jthaler_2017_03_Aspen_Jet.pdf|"Recent Progress in Jet Physics"]], [[https://indico.cern.ch/event/550030/|From the LHC to Dark Matter and Beyond]], //Aspen Center for Physics, March 2017//
  * [[http://www.jthaler.net/talks/jthaler_2017_01_APS_DM_Overview.pdf|"New Frontiers in Dark Matter Detection"]], APS April Meeting, //Washington, DC, January 2017//
  * [[http://www.jthaler.net/talks/jthaler_2017_01_APS_GPMFC_ABRA.pdf|"Prospects for Cosmic Axion Detection with ABRACADABRA"]], GPMFC Workshop on Ultralight Dark Matter, //Washington, DC, January 2017//
  * "Using Jets and QCD to Boost the Search for New Physics", Physics in LHC and Early Universe, //U. Tokyo, January 2017//
  * "The Shape of Jets to Come" (Refocus Talk), Boost 2016, //Zurich, July 2016// 
  * "Probing the Core of QCD with Jet Substructure", Stress-testing the Standard Model at the LHC, //KITP, Santa Barbara, May 2016//
  * "Jet Substructure: Boosting the Search for New Physics at the LHC", APS April Meeting, //Salt Lake City, April 2016//
  * "Theoretical Advances in Jet Substructure", Rencontres de Moriond QCD, //La Thuile, March 2016//
  * "Theoretical Advances in Jet Substructure", Particle Physics on the Verge of Another Discovery, //Aspen Center for Physics, January 2016//
  * "Probing the Core of QCD", Boost 2015, //Chicago, August 2015// (Advisory Committee)
  * "Unsafe but Calculable: Jets at the Frontier of Perturbative QCD", PASCOS 2015, //ICTP, Trieste, July 2015//
  * "Pushing the Frontiers of Perturbative QCD", Pheno 2015, //Pittsburg, May 2015//
  * "Hidden Sectors and Dark Forces", BLV 2015, //UMass Amherst, April 2015//
  * "Physics Opportunities for Future Circular Colliders", FCC Week, //Washington, DC, March 2015//
  * "Jets in QCD: The Case for Jet Substructure", Quark Confinement and the Hadron Spectrum XI, //St. Petersburg, September 2014//
  * "New Observables for Jet Substructure", 43rd International Symposium on Multiparticle Dynamics (ISMD13), //Chicago, September 2013// 
  * "The Case for Jet Substructure", SEARCH 2013, //Stonybrook, August 2013//
  * "Theoretical Progress in Dissecting Jets", Boost 2013, //Flagstaff, August 2013//
  * "Supersymmetry at the Frontiers" (Rapporteur Talk), Snowmass on the Pacific, //KITP, Santa Barbara, May 2013// 
  * "Jet Substructure and N-subjettiness", Monte Carlo for Beyond the Standard Model 2012, //Cornell, March 2012// 
  * "Big Questions in Particle Physics" (Pedagogical Lecture), [[http://web.mit.edu/panic11/|PANIC11]], //MIT, July 2011//
  * "Two Views of the Universe" (Closing Talk), Hadron Collider Physics Symposium, //Toronto, August 2010// 
  * "Supersymmetry Breaks (Again)", in honor of Gerry Guralnik's 2010 Sakurai Prize, //Brown University, May 2010// 
  * "Goldstini", Emerging Problems in Particle Phenomenology, //ITS/CUNY, April 2010// 
  * "The Window to the Terascale" (Opening Talk), Physics in the LHC Era, //Aspen Center for Physics, February 2009//   

### Local Presentations


  * "[[http://www.jthaler.net/talks/jthaler_2022_05_IAIFI_Faculty_Lunch.pdf|Deep Learning: Lessons from the Launch of IAIFI]]", MIT Physics Faculty Lunch, //May 2022//
  * "SPS/PGSC Career Panel", MIT Physics, //November 2021//
  * "[[http://www.jthaler.net/talks/jthaler_2021_07_IAIFI_WarriorScholar.pdf|IAIFI at MIT Physics]]", Warrior-Scholar Program Open House, //July 2021//
  * "[[http://www.jthaler.net/talks/jthaler_2020_09_IAIFI_AI+D.pdf|The NSF AI Institute for Artificial Intelligence and Fundamental Interactions]]", MIT AI+D Lunch, //September 2020//
  * "Making the Cut - Job Searching During a COVID-19 Economy: A Panel Discussion", MIT Postdoctoral Association, //June 2020//
  * "[[http://www.jthaler.net/talks/jthaler_2019_09_FacultyLunch.pdf|Collision Course:  Particle Physics meets Machine Learning]]", MIT Physics Faculty Lunch, //September 2019//
  * "The Nuts and Bolts of Academic Job Search", MIT Graduate Student Council, //July 2018//
  * "(B)SM Physics", Physics Graduate Student Lunch, //November 2016//
  * "Jet Substructure", Tenure-Track Faculty Lunch, //November 2015//
  * "Implications of the Higgs Boson", MIT PhysPOP Orientation Lecture, //August 2013//
  * "The Higgs Boson: Keystone of the Standard Model", MIT MISTI Presentation, //April 2013//
  * "Dark Matter Beyond the Standard Model", MIT Astronomical Event, //October 2012//
  * "Hints of New Physics at the Energy Frontier", MIT Physics Alumni Breakfast, //May 2012//
  * "Beyond the Standard Model at the Frontiers", MIT PhysPOP Orientation Lecture, //August 2011//
  * "Goldstini at the LHC", MIT Physics Visiting Committee Presentation, //October 2010//
  * "Supersymmetry Breaks (Again)", MIT Physics Faculty Lunch, //April 2010//
  * "The LHC Won’t Destroy the Planet (But Will Spark a Revolution)", //MIT Physics IAP Lecture 2010//

### Invited Seminars

  * "[[http://www.jthaler.net/talks/jthaler_2022_11_Brown_Seminar.pdf|Machine Learning for the Skeptical HEP Theorist]]", Brown, November 2022
  * "[[http://www.jthaler.net/talks/jthaler_2022_05_HiddenGeometry_Bern.pdf|The Geometry of Particle Collisions: Hidden in Plain Sight]]", Bern, May 2022 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2022_04_SLAC_Quantum.pdf|Quantum (Inspired) Algorithms for Collider Physics]]", SLAC, Apr 2022 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2022_04_HiddenGeometry_Austin.pdf|The Geometry of Particle Collisions: Hidden in Plain Sight]]", UT Austin, Apr 2022 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2022_03_HiddenGeometry_Sussex.pdf|The Hidden Geometry of Particle Collisions]]", Sussex, Mar 2022 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_12_HiddenGeometry_SDSC.pdf|The Geometry of Particle Collisions: Hidden in Plain Sight]]", [[https://stat.mit.edu/seminars/|MIT Stochastics and Statistics Seminar]], Dec 2021 (in-person talk!) 
  * "[[http://www.jthaler.net/talks/jthaler_2021_11_QuantHEP.pdf|Quantum (Inspired) Algorithms for Collider Physics]]", [[http://quanthep-seminar.org/session/session-13/|QuantHEP Seminar]], Nov 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_10_HiddenGeometry_Zurich.pdf|The Hidden Geometry of Particle Collisions]]", [[https://www.physik.uzh.ch/en/seminars/ttpseminar/HS2021/thaler.html|Zurich]], Oct 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_06_HiddenGeometry_GGI.pdf|The Hidden Geometry of Particle Collisions]]", [[https://www.ggi.infn.it/images/TeaBreaks/Jesse_v1.jpg|GGI Tea Breaks' Seminar]], June 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_06_IAIFI_STAMPS.pdf|A Few Collisions between Particle Physics and Machine Learning]]", CMU STAMPS Group Meeting, June 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_06_HiddenGeometry_Heidelberg_MITP.pdf|The Hidden Geometry of Particle Collisions]]", [[https://www.thphys.uni-heidelberg.de/~teilchentee/index.php?n1=ss21&n2=9|Joint Heidelberg Teilchentee]] / [[https://indico.mitp.uni-mainz.de/event/199/sessions/855/|MITP Workshop Seminar]], June 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_05_HiddenGeometry_IPPP.pdf|The Hidden Geometry of Particle Collisions]]", [[https://conference.ippp.dur.ac.uk/event/1006/|IPPP Durham]], May 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_04_HiddenGeometry_TUM.pdf|The Hidden Geometry of Particle Collisions]]", Munich, April 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_04_HiddenGeometry_Florida.pdf|The Hidden Geometry of Particle Collisions]]", Joint Florida HEP Seminar, April 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_02_HiddenGeometry_Oxford.pdf|The Hidden Geometry of Particle Collisions]]", Oxford, February 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2021_02_HiddenGeometry_Paris.pdf|The Hidden Geometry of Particle Collisions]]", [[https://indico.in2p3.fr/event/22930/|Particle Physics in Paris]], February 2021 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_11_HiddenGeometry_UCDavis.pdf|The Hidden Geometry of Particle Collisions]]", U.C. Davis, November 2020 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_11_HiddenGeometry_UCSD.pdf|The Hidden Geometry of Particle Collisions]]", U.C. San Diego, November 2020 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_11_HiddenGeometry_LBNL.pdf|The Hidden Geometry of Particle Collisions]]", LBNL RPM, November 2020 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_10_HiddenGeometry_Cambridge.pdf|The Hidden Geometry of Particle Collisions]]", Cambridge, October 2020 (virtual talk)
  * "[[http://www.jthaler.net/talks/jthaler_2020_06_TIFR_FreeMeson.pdf|The Hidden Geometry of Particle Collisions]]", TIFR, June 2020 (virtual talk)
  * [[http://www.jthaler.net/talks/jthaler_2019_11_CaseWestern_QI.pdf|"Quantum Algorithms for Collider Physics"]], Case Western, November 2019 (informal talk)
  * [[http://www.jthaler.net/talks/jthaler_2019_10_Rice_Informal.pdf|"Data-Driven Approaches to Jet Quenching"]], Rice, October 2019 (informal talk)
  * [[http://www.jthaler.net/talks/jthaler_2019_06_Ljubljana_EMD.pdf|"The Space of Collider Events"]], Ljubljana, June 2019
  * [[http://www.jthaler.net/talks/jthaler_2019_04_SLAC_EMD.pdf|"The Space of Collider Events"]], SLAC, April 2019
  * [[http://www.jthaler.net/talks/jthaler_2019_04_UCSC_EMD.pdf|"The Space of Collider Events"]], U.C. Santa Cruz, April 2019
  * [[http://www.jthaler.net/talks/jthaler_2019_04_Google_Collision.pdf|"Collision Course: Particle Physics meets Machine Learning"]], Google X Tech Talk, April 2019
  * [[http://www.jthaler.net/talks/jthaler_2019_03_BU_EMD.pdf|"The Space of Collider Events"]], Boston U., March 2019
  * [[http://www.jthaler.net/talks/jthaler_2019_02_Brandeis_Collision.pdf|"Collision Course: Particle Physics as a Machine-Learning Testbed"]], Brandeis, February 2019
  * [[http://www.jthaler.net/talks/jthaler_2018_11_UMich_EFN.pdf|"Deep Sets for Particle Jets"]], U. Michigan, November 2018 
  * [[http://www.jthaler.net/talks/jthaler_2018_10_NYU_EFN.pdf|"Deep Sets for Particle Jets"]], New York U., October 2018 
  * [[http://www.jthaler.net/talks/jthaler_2018_10_PDT_Collision.pdf|"Collision Course: Particle Physics as a Machine-Learning Testbed"]], PDT Partners, October 2018
  * [[http://www.jthaler.net/talks/jthaler_2018_05_Cambridge_Jet_Topics.pdf|"On the Topic of Jets"]], U. Cambridge, May 2018
  * [[http://www.jthaler.net/talks/jthaler_2018_03_Bicocca_Jet_Topics.pdf|"On the Topic of Jets"]], Milano Bicocca, March 2018
  * [[http://www.jthaler.net/talks/jthaler_2018_03_Genoa_Jet_Topics.pdf|"On the Topic of Jets"]], Genova, March 2018
  * [[http://www.jthaler.net/talks/jthaler_2018_02_Carleton_Topics.pdf|"On the Topic of Jets"]], Carleton, February 2018
  * [[http://www.jthaler.net/talks/jthaler_2017_12_Yale_SysJets.pdf|"Towards Systematic Jet Dissection"]], Yale, December 2017
  * [[http://www.jthaler.net/talks/jthaler_2017_12_Yale_OpenData.pdf|"The Future is Open: Jet Substructure with CMS Public Data"]], Yale, December 2017
  * "Casimir Meets Poisson", U.C. Berkeley, April 2017
  * [[http://www.jthaler.net/talks/jthaler_2017_03_UTAustin_Seminar.pdf|"Casimir Meets Poisson"]], U. Texas, March 2017
  * "A New Angle on Jet Substructure", SUNY Stony Brook, October 2016
  * "A New Angle on Jet Substructure", Rutgers, October 2016
  * "A New Angle on Jet Substructure", Boston U., September 2016
  * "Probing the Core of QCD with Jet Substructure", Joint Experimental-Theoretical Physics Seminar, Fermilab, May 2016
  * "Probing the Core of QCD with Jet Substructure", Princeton, May 2016
  * "Probing the Core of QCD with Jet Substructure", CERN, March 2016
  * "Hidden Sectors and Dark Forces", Ohio State University, January 2016
  * "Unsafe but Calculable", University of Toronto, December 2015
  * "Lessons from DarkLight for Invisible Dark Photon Searches", NEXT Collaboration, December 2015 (remote talk)
  * "Minimal Supersymmetric Slow-roll Inflation", Stanford, November 2015
  * "Jet Substructure at a Future Hadron Collider", Fermilab VHEPP Forum, October 2015 (remote talk)
  * "What is Sudakov Safety?", U. Michigan, February 2015
  * "What is Sudakov Safety?", U. Minnesota, February 2015
  * "Jet Substructure and the Frontiers of QCD", Université Catholique de Louvain, January 2015
  * "(In)direct Detection of Boosted Dark Matter", Vrije Universiteit Brussel, January 2015
  * "Sudakov Safety", Caltech, November 2014
  * "(Non)perturbative QCD and Jet Substructure", UMass Amherst, October 2014
  * "(Non)perturbative QCD and Jet Substructure", Perimeter Institute, October 2014
  * "Anomaly Mediation from Unbroken Supergravity", U. Chicago, April 2014 
  * "Anomaly Mediation from Unbroken Supergravity", U.C. Irvine, January 2014 
  * "Jets Without Jets", Caltech, January 2014
  * "Jets Without Jets", U.C. Berkeley, December 2013 
  * "Jets Without Jets", Boston U., December 2013 
  * "(Non)perturbative QCD and Jet Substructure", U. Oregon, May 2013 
  * "The Shape of Jets to Come", U. Delaware, April 2013 
  * "(Non)perturbative QCD and Jet Substructure", Boston U., September 2012 
  * "The Two Faces of Anomaly Mediation", SLAC, April 2012 
  * "The Two Faces of Anomaly Mediation", Princeton, March 2012 
  * "The Two Faces of Anomaly Mediation", Rutgers, March 2012 
  * "The Two Faces of Anomaly Mediation", New York U., January 2012 
  * "Goldstini at the LHC", Columbia U., January 2012 
  * "Goldstini at the LHC", U. New Hampshire, November 2011 
  * "N-subjettiness", U. Maryland, October 2011 
  * "N-subjettiness", U. Michigan, October 2011 
  * "The Spectrum of Goldstini", U. Minnesota, June 2011 
  * "N-subjettiness", U.C. Davis, March 2011 
  * "N-subjettiness", U.C. Berkeley, March 2011 
  * "Aspects of Goldstini", Cornell, October 2010 
  * "Aspects of Goldstini", Boston U., October 2010 
  * "Aspects of Goldstini", Harvard, September 2010 
  * "Aspects of Goldstini", SLAC, June 2010 
  * "Goldstini", Yale University Particle Theory Seminar, April 2010 
  * "Goldstini", SUNY Stony Brook/Brookhaven National Laboratory Joint Theory Seminar, March 2010 
  * "Cosmic Signal from the Hidden Sector", U.C. Santa Cruz, November 2009 
  * "Dark Force Detection in Low Energy e-p Collisions", U.C. Davis, October 2009 
  * "Cosmic Signals from the Hidden Sector", Fermilab, October 2009 
  * "Cosmic Signals from the Hidden Sector", Argonne N.L., October 2009 
  * "Dark Matter through the Axion Portal", Johns Hopkins, May 2009 
  *  "Dark Matter through the Axion Portal", U. Maryland, May 2009 
  * "Collective Quartics and Dangerous Singlets in Little Higgs", SLAC, April 2009 
  * "Dark Matter through the Axion Portal", Rutgers, March 2009 
  * "Dark Matter through the Axion Portal", MIT, February 2009 
  * "Dark Matter through the Axion Portal", Cornell, November 2008 
  * "GenEvA: A New Framework for Event Generation", U.C. Davis, June 2008 
  * "GenEvA: A New Framework for Event Generation", Ohio State, May 2008 
  * "GenEvA: A New Framework for Event Generation", MIT, April 2008 
  * "GenEvA: A New Framework for Event Generation", U. Arizona, March 2008 
  * "GenEvA: A New Framework for Event Generation", U. Texas, March 2008 
  * "GenEvA: A New Framework for Event Generation", SLAC, February 2008
  * "GenEvA: A New Framework for Event Generation", Princeton, November 2007 
  * "GenEvA: A New Framework for Event Generation", Rutgers, November 2007 
  * "Particle Theory and Monte Carlo", Stanford, November 2007 
  * "Natural/Unnatural", U.C. San Diego, April 2007 
  * "Natural/Unnatural", U. Michigan, February 2007 
  * "Natural/Unnatural", Princeton, February 2007 
  * "Di-Higgs at Dimension Six", Weizmann I., January 2007 
  * "MARMOSET: Signal-Based Monte Carlo for the LHC", Neve Shalom, January 2007 
  * "Di-Higgs at Dimension Six", Technion, January 2007 
  * "Unified Frameworks for the LHC", U. Washington, December 2006 
  * "Di-Higgs at Dimension Six", SLAC, October 2006 
  * "Unified Frameworks for the LHC", U.C. Davis, October 2006 
  * "Unified Frameworks for the LHC", U.C. Irvine, October 2006 
  * "Supersymmetry and the LHC Inverse Problem", U. Chicago (CDF), March 2006 
  * "Supersymmetry and the LHC Inverse Problem", U. Minnesota, March 2006 
  * "Supersymmetry and the LHC Inverse Problem", Perimeter I., March 2006 
  * "Supersymmetry and the LHC Inverse Problem", Rutgers, December 2005 
  * "Supersymmetry and the LHC Inverse Problem", U. Pennsylvannia, December 2005 
  * "Supersymmetry and the LHC Inverse Problem", Princeton, November 2005 
  * "Supersymmetry and the LHC Inverse Problem", U.C. Berkeley, November 2005 
  * "Confronting a Degenerate MSSM at the LHC", Stanford, October 2005 
  * "Supersymmetry and the LHC Inverse Problem", Johns Hopkins, October 2005 
  * "The Degenerate MSSM", U. Texas, October 2005 
  * "Little Technicolor", Boston U., April 2005 
  * "Little Technicolor", New York U., March 2005 

### Additional Conferences/Workshops


  * Panelist, [[https://indico.cern.ch/event/1159913/|ML4Jets 2020]], //Rutgers, November 2022// (Advisory Board)
  * No Talk, [[https://www.simonsfoundation.org/event/mps-annual-meeting-2022/|2022 Mathematics and Physical Sciences Annual Meeting]], //Simons Foundation, October 2022//
  * Panelist, "Does the World need a new particle collider – and why?", European Committee for Future Accelerators, //Virtual to Hamburg, October 2022//
  * "[[http://www.jthaler.net/talks/jthaler_2022_08_GGI_Snowmass.pdf|Machine Learning for High Energy Physics]]", [[https://www.ggi.infn.it/showevent.pl?id=411|Machine Learning at GGI]], GGI, Aug 2022
  * No Talk, [[https://indico.fnal.gov/event/22915/|Summiting the Unknown: New Physics, New Opportunities, New Voices]], //U. Washington, Seattle, July 2022//
  * No Talk, Interplay of Fundamental Physics and Machine Learning, //Aspen Center for Physics, June 2022// (Organizer)
  * Panelist, "[[http://www.jthaler.net/talks/jthaler_2022_02_IAIFI_AAAI.pdf|USDA/NSF AI Institutes]]", [[https://aaai.org/Conferences/AAAI-22/|AAAI-22]], //Online, February 2022//
  * Panelist, "[[http://www.jthaler.net/talks/jthaler_2022_02_IAIFI_CACM.pdf|AI and Science]]", [[https://cacm.acm.org/magazines/2022/4/259397-communications-digital-initiative-and-its-first-digital-event/fulltext|CACM Digital Event]], //Online, February 2022//
  * Panelist, "The current limits of AI in science", OECD workshop: [[https://www.oecd.org/sti/inno/ai-productivity-of-science.htm|AI and the productivity of science]], //Online, November 2021//  
  * Convener, "[[https://indico.fnal.gov/event/44870/sessions/16380/|Collider Data Analysis Strategies]]", "[[https://indico.fnal.gov/event/44870/sessions/16258/|Advances in Event Generation and Detector Simulation]]", [[https://indico.cern.ch/e/CMSOpenDataForTheorists|Snowmass Community Planning Meeting]], //Online, October 2020//
  * "[[http://www.jthaler.net/talks/jthaler_2020_09_OpenData_WorkshopWelcome.pdf|Welcome]]", [[https://indico.cern.ch/e/CMSOpenDataForTheorists|CMS Open Data Workshop for Theorists]], //Online, September 2020//
  * No Talk, [[https://indico.cern.ch/event/775951/|BOOST 2020 Webinars]], //Online, July 2020//
  * No Talk, [[https://indico.desy.de/indico/event/25341/|Anomaly Detection Mini-Workshop]], //Online, July 2020//
  * No Talk, [[https://indico.cern.ch/event/809820/|ML4Jets 2020]], //NYU, January 2019// (Organizer)
  * [[http://www.jthaler.net/talks/jthaler_2019_08_USATLAS_ML.pdf|"Deep Learning (and Deep Thinking) in Collider Physics"]], [[https://indico.cern.ch/event/813845|US ATLAS Workshop]], //UMass Amherst, August 2019//
  * No Talk, [[https://indico.cern.ch/e/boost2019|Boost 2019]], //MIT, July 2019// (Organizer)
  * [[http://www.jthaler.net/talks/jthaler_2019_07_Voyages_ML.pdf|"Voyages into Machine Learning"]], [[https://indico.cern.ch/event/814878/|Voyages Beyond the Standard Model III]], //Zadar, Croatia, July 2019//
  * [[http://www.jthaler.net/talks/jthaler_2019_01_QuantISED_Poster.pdf|"Quantum Algorithms for Collider Physics"]] (Poster), [[https://www.orau.gov/qispi2018/|DOE Quantum Information Science Kick Off Meeting]], //Rockville, MD, January 2019//
  * No Talk, [[https://indico.cern.ch/event/750705/|Boosted Objects for New Physics Searches]], //Fermilab, November 2018//
  * No Talk, [[https://www.simonsfoundation.org/event/2018-mps-annual-meeting/|2018 Mathematics and Physical Sciences Annual Meeting]], //Simons Foundation, October 2018//
  * [[http://www.jthaler.net/talks/jthaler_2018_04_MIT_RecoML.pdf|"The Energy Flow Basis"]], [[https://indico.cern.ch/event/714134/|Reconstruction, Trigger, and Machine Learning for the HL-LHC]], //MIT, April 2018//
  * No Talk, [[http://www-personal.umich.edu/%7Espitzj/Spitz_group_at_UM/IsoDAR_workshop.html|IsoDAR Workshop]], //MIT, January 2018// 
  * No Talk, [[https://indico.cern.ch/event/690007/|Jet Physics Mini-Workshop]], //MIT, January 2018// 
  * [[http://www.jthaler.net/talks/jthaler_2017_10_Fermilab_OpenData.pdf |"The Future is Open:  Jet Substructure with CMS Public Data"]], [[https://indico.cern.ch/event/639314/|Reinterpretation Forum Workshop]], //Fermilab, October 2017// (Remote Talk)
  * No Talk, [[https://indico.cern.ch/event/579660/|Boost 2017]], //Buffalo, July 2017// 
  * [[http://www.jthaler.net/talks/jthaler_2017_06_LesHouches_JetIntro.pdf|"Jet Studies for Les Houches"]], [[http://www.jthaler.net/talks/jthaler_2017_06_LesHouches_JetSummary.pdf|"Report of the Les Houches Jet Physics Subgroup"]], Physics at TeV Colliders Workshop, //Les Houches, June 2017// (Jet Convener)
  * [[https://www.youtube.com/watch?v=QNmSNY8VenQ|"Confronting the Invisible Universe"]], Public Talk, //Aspen Center for Physics, March 2017//
  * "Aspects of Jets from First Principles", Jets @ LHC Discussion Meeting, //ICTS, Bengaluru, January 2017// (Remote Talk)
  * "Jet Substructure from Protons to Ions", Heavy Ions for 2020 Workshop, //MIT, October 2016//
  * No Talk, Aspen Center for Physics Workshop: "The LHC Awakens: A New Energy Frontier", //August 2016// (Organizer)
  * "Discussion of the ATLAS Diboson Excess", Gearing up for LHC13, //GGI, Florence, Fall 2015// (Organizer)
  * "Jet Studies for Les Houches", Physics at TeV Colliders Workshop, //Les Houches, June 2015// (Jet Convener)
  * "Lessons from Jet Substructure for Heavy Ions", ALICE Jet Workshop, //Yale, May 2015// (Remote Talk)
  * "The Case for Jet Substructure", International Workshop on Future Linear Colliders (LCWS14), //Belgrade, October 2014// (Remote Talk)
  * "Mutual Information and Quark/Gluon Discrimination", Boost 2014, //London, August 2014// (Advisory Committee)
  * No Talk, Debates on the Nature of Dark Matter, //Harvard, May 2014//
  * No Talk, Boston Jet Physics Workshop, //MIT, January 2014//    (Organizer)
  * "Unsafe but Calculable", Boost 2013, //Flagstaff, August 2013// (Advisory Committee)
  * "N-jettiness as a Jet Algorithm", Snowmass@Brookhaven, //Brookhaven, April 2013// (Remote Talk)
  * "Progress in Jet Substructure", The LHC Shows the Way, //Aspen Center for Physics, August 2012//
  * "Progress in N-subjettiness", Boost 2012, //Valencia, July 2012// (Advisory Committee)
  * No Talk, SEARCH 2012, //U. Maryland, March 2012//
  * "Goldstini", SUSY 2011, //Fermilab, August 2011//
  * "N-subjettiness", TH-LPCC Summer Institute on LHC Physics, //CERN, August 2011//  
  * No Talk, Year One of the LHC, //Aspen Center for Physics, July 2011// (Organizer)
  * "Big Questions in Particle Physics" (Pedagogical Lecture), "N-subjettiness", PANIC11, //MIT, July 2011// (Program Committee)
  * "N-subjettiness", Boost 2011, //PCTP, Princeton, May 2011//
  * No Talk, [[https://indico.cern.ch/event/103979/|New Data from the Energy Frontier]], //Aspen Center for Physics, February 2011// (Organizer)
  * No Talk, [[https://indico.cern.ch/event/113980/|Boston Jet Physics Workshop]], //Harvard, January 2011//    (Organizer)
  * "Introducing the DarkLight Experiment", Searching for a New Gauge Boson at JLab, //Jefferson Lab, September 2010// 
  * No Talk, [[http://www-ctp.mit.edu/lhc/|Implications of First LHC Data]], //MIT, August 2010// (Organizer)
  * No Talk, From Colliders to the Dark Sector, //Aspen Center for Physics, June 2010//  
  * "Search for New Light Bosons in Electron-Proton Collisions Using the JLab FEL", Dark Forces Workshop, //SLAC, September 2009//  
  * "Cosmic Signals from the Hidden Sector", BSM Institute, Physics at the LHC, //CERN, August 2009//  
  * No Talk, Beyond the Standard Model Physics at the Threshold, //Aspen Center for Physics, July 2009//  
  * "Variable Jet Sizes and Anti-kT", US ATLAS Hadronic Final State Forum, //SLAC, April 2009//  
  * "The NLO Cascade", SCET 2009, //MIT, March 2009// 
  * "Dark Matter through the Axion Portal", LHC and Dark Matter Workshop, //MCTP, Michigan, January 2009//  
  * "GenEvA: A New Framework for Event Generation", New Physics Beyond the Standard Model, //KITPC, Beijing, October 2008//  
  * "GenEvA: A New Framework for Event Generation", Beyond the Standard Model Signals in a QCD Environment, //Aspen Center for Physics, August 2008//  
  * "GenEvA: A New Framework for Event Generation", LHC from Data to Discovery, //LANL, Santa Fe, July 2008//  
  * "GenEvA: A New Framework for Event Generation", Vector Boson Plus Jets Production, //LBL, Berkeley, March 2008//  
  * "GenEvA: A New Framework for Event Generation", Physics of the Large Hadron Collider, //KITP, Santa Barbara, February 2008//  
  * No Talk, West Coast LHC Theory Network, //SLAC, January 2008// 
  * "GenEvA: A New Framework for Event Generation", LHC New Physics Signatures Workshop, //MCTP, Michigan, January 2008// 
  * No Talk, BSM Institute, New Physics and the LHC, //CERN, August 2007//  
  * "Good Things Come to Those Who Weight", Eötvös-Cornell BTSM Workshop, //Eötvös University, Budapest, June 2007// 
  * "MARMOSET", West Coast LHC Theory Network, //U.C. Irvine, May 2007// 
  * "MARMOSET", Physics at LHC from Experiment to Theory, //PCTP, Princeton, March 2007//  
  * "MARMOSET", West Coast LHC Theory Network, //U.C. Davis, December 2006// 
  * "Little M-theory", Joint Meeting of APS-DPF and JPS 2006, //Waikiki, Hawaii, October 2006//  
  * "Little M-theory", LHC Olympics III, //KITP, Santa Barbara, August 2006// 
  * "The Harvard Black Box", LHC Olympics II, //CERN, February 2006// 
  * "The Degenerate MSSM", LHC Olympics, //CERN, July 2005//
  * "Little Technicolor", "The Degenerate MSSM", SUSY 2005, //IPPP, Durham, July 2005//
  * "Universal Dynamics of Spontaneous Lorentz-Violation", Fundamental Symmetries and Fundamental Constants, //ICTP, Trieste, September 2004// 

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

{% for phd-thesis in site.data.cv_service.phd-theses %}
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

{% for phd-thesis in site.data.cv_service.external-phd-theses %}
  * **{{phd-thesis.name}}**, "{{phd-thesis.title | default: "TBA"}}" ({{phd-thesis.advisor}}), *{{phd-thesis.uni}}, {{phd-thesis.date | default: "in progress"}}*
{%- endfor %}

#### External Mentoring

{% for mentoring in site.data.cv_service.external-mentoring %}
  * **{{mentoring.name}}**, {{mentoring.program}}, *{{mentoring.uni}}, {{mentoring.date}}*
{%- endfor %}

#### Workshop/Conference Organization


  * General Member, Aspen Center for Physics (Summer 2020-Summer 2025)
    * Liason, Winter Workshop, "Theoretical Physics for Machine Learning" (Winter 2023)
    * Organizer, Summer Workshop, "Interplay of Fundamental Physics and Machine Learning" (Summer 2022)
    * Nominations Committee (Summer 2021; Chair, Summer 2022; Ex officio, Summer 2023)
    * Summer Program Committee (Summer 2020)
  * Topical Convener in [[https://snowmass21.org/theory/phenomenology|Collider Phenomenology]], [[https://snowmass21.org/theory/start|Snowmass Theory Frontier]] (July 2021)
  * Organizer, GGI Workshop: "[[https://agenda.infn.it/event/32043/|Machine Learning at GGI]]" (August/September 2022)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Online Workshop:  "[[https://indico.cern.ch/event/1037559/|Boost 2021]]" (August 2021)
  * Advisory Committee, Heidelberg Workshop:  "[[https://indico.cern.ch/event/980214/|ML4Jets]]" (July 2021)
  * Organizer, Fermilab Remote Workshop:  "[[https://indico.cern.ch/e/CMSOpenDataForTheorists|CMS Open Data for Theorists]]" (September 2020)
  * Advisory Committee and Ombuds Team (with Ayana Arce), Hamburg Workshop:  "[[https://indico.cern.ch/e/boost2020|Boost 2020]]" (July 2020)
  * Advisory Committee, Mainz Workshop:  "[[https://indico.mitp.uni-mainz.de/event/199/|Machine Learning for Particle Physics]]" (May 2020 → June 2021)
  * Advisory Committee, New York Workshop:  "[[https://indico.cern.ch/event/809820/|ML4Jets]]" (January 2020)
  * Local Organizing Committee, Boston Workshop:  "[[https://indico.cern.ch/e/boost2019|Boost 2019]]" (July 2019)
  * Advisory Committee, Paris Workshop:  "[[https://indico.cern.ch/e/boost2018|Boost 2018]]" (July 2018)
  * Local Organizing Committee, MIT Workshop: "[[https://physicsrisingstars.mit.edu/|Rising Stars in Physics]]" (April 2018)
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

  * International Scientific Advisory Board, [AI for Science and Science for AI (AISSAI) Center](https://www.cnrs.fr/en/artificial-intelligence-science-science-artificial-intelligence-aissai-center), French CNRS, *2022-present*
  * International Advisory Committee, Grant-in-Aid for Transformative Research Areas, JSPS/MEXT Japan, *2022-2026*
  * Member, [High Energy Physics Advisory Panel (HEPAP)](https://science.osti.gov/hep/hepap), *August 2021-March 2024*
  * ["The NSF AI Institute for Artificial Intelligence and Fundamental Interactions"](http://www.jthaler.net/talks/jthaler_2020_12_IAIFI_HEPAP_Overview.pdf), [High Energy Physics Advisory Panel](https://science.osti.gov/hep/hepap/Meetings/202012), *Dec 2020*
  * ["The High Energy Physics Landscape in 2019"](http://www.jthaler.net/talks/jthaler_2019_05_HEPAP.pdf), [High Energy Physics Advisory Panel](https://science.osti.gov/hep/hepap/Meetings/201905), *May 2019*
  * Science Advisory Board, USQCD Collaboration (Spring 2013-Fall 2016)
  * Sakurai Dissertation Award Selection Committee, American Physical Society (Fall 2016)
  * LHC Theory Initiative, Fellowship Selection Committee (Fall 2013-Fall 2014, Chair: Fall 2014)

#### Peer Review

  * [Journal of High Energy Physics](https://jhep.sissa.it/)
    * Editorial Board, *Fall 2019-present*
  * [SciPost Physics](https://scipost.org/SciPostPhys)
    * Editorial College, *Fall 2019-present*
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

## Outreach
 
  * ["Designing an AI Physicist"](https://cerncourier.com/a/designing-an-ai-physicist/), Opinion Viewpoint, *[CERN Courier, September-October 2021](https://cerncourier.com/wp-content/uploads/2021/08/CERNCourier2021SepOct-digitaledition.pdf#CCSepOct21-digital.indd%3A.17586%3A1070)*
  * ["Collision Course: Artificial Intelligence meets Fundamental Physics"](http://www.jthaler.net/talks/jthaler_2020_10_TommyFlowers_Keynote.pdf), Keynote Presentation, ["Tommy Flowers Network Conference"](http://tommyflowersnetwork.blogspot.com/2020/07/virtual-conference-lets-get-physical.html), *Virtual, October 2020*
  * ["Listening for Dark Matter from the Basement of Building 24"](https://physics.mit.edu/wp-content/uploads/2020/05/physicsatmit_19_winslow-thaler.pdf), coauthored with Lindley Winslow, Contribution to [Physics@MIT Journal](https://web.mit.edu/physics/news/physicsatmit/fall2019.html), *Fall 2019*
  * ["Slow and Steady"](https://rdcu.be/bMHQn), coauthored with Matthew Strassler, Correspondence, [Nature Physics 15:725 (2019)](https://doi.org/10.1038/s41567-019-0628-z).
  * ["Listening to the Invisible Universe"](http://www.jthaler.net/talks/jthaler_2019_04_FarCry.pdf), Program with [A Far Cry](https://afarcry.org/), [Open Rehearsal of Gravity](https://www.eventbrite.com/e/sold-out-a-far-cry-presents-sounds-of-the-universe-registration-58723801471#), *April 2019*
  * ["Guest Case Study 6:  Particle Collisions"](http://www.jthaler.net/cv/jthaler_frankel_picturing_science.pdf), Contribution to [Felice Frankel](https://www.felicefrankel.com/), [Picturing Science and Engineering](https://mitpress.mit.edu/books/picturing-science-and-engineering), *MIT Press, 2018*
  * ["The Future of Particle Physics is 'Open'"](https://cylindricalonion.web.cern.ch/blogs/future-particle-physics-open), Guest Blog Post, The Cylindrical Onion, *CMS Experiment, December 2017*
  * ["Confronting the Invisible Universe"](http://www.jthaler.net/talks/jthaler_2018_05_London_Dark_Matter.pdf), MIT Club of Great Britain Event, *London, May 2018*
  * ["Confronting the Invisible Universe"](https://www.youtube.com/watch?v=QNmSNY8VenQ), Public Talk, *Aspen Center for Physics, March 2017*
  * ["The Higgs Boson:  Triumph of the Standard Model"](http://vimeo.com/58392070), 24th Annual Kavli Frontiers of Science, *National Academy of Sciences, U.C. Irvine, November 2012*
  * Appearance in Documentary Film, "Particle Fever", 2013 
    * After film Q&A, BOOST 2015 Workshop Public Event, August 2015
    * After film Q&A, MIT Lecture Series Committee, September 2014
    * After film Q&A, Portsmouth Music Hall, May 2014
  * TheoryNet High School Physics Outreach
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

## Memberships

{% for membership in site.data.cv_service.memberships %}
  * **[{{membership.name}}]({{membership.url}})** 
{%- endfor %}


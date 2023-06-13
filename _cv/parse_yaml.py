import yaml,os

#################### bio file

bio_input = open("../_data/bio.yml","r")
bio_yaml = yaml.load(bio_input,Loader=yaml.BaseLoader)


########## awards file

awards_output = open("cv_awards.tex","w")
awards = bio_yaml['awards']
awards_output.write('\\bbl\n')

for award in awards:
  if int(award['priority']) >= 3 :
    awards_output.write('\\item '+award['name']+', \\textit{'+award['org']+', '+award['date'].replace('-','--')+'}\n')
    
awards_output.write('\\el\n')




#################### papers file

papers_input = open("../_data/papers.yml","r")
papers_yaml = yaml.load(papers_input,Loader=yaml.BaseLoader)


########## papers file

papers_output = open("cv_papers.tex","w")

papers = papers_yaml['papers']

papers_output.write('\\newcounter{jessecount}\n')
papers_output.write('\\setcounter{jessecount}{'+str(len(papers))+'}\n\n')
papers_output.write('\\begin{list}{[\\arabic{jessecount}]\\addtocounter{jessecount}{-1}}{\\leftmargin=3em \\itemsep=4pt}\n\n')

for paper in papers:
  papers_output.write('\\item\n')
  if 'made_phd' in paper:
    papers_output.write('*')
  if 'made_bs' in paper:
    papers_output.write('$\\dagger$')
  papers_output.write(' '+paper['authors'].replace('. ','.\ ')+',\n')
  papers_output.write('\\emph{'+paper['title']+'}')
  if 'journal' in paper:
    papers_output.write(',')
  papers_output.write('\n')
  if 'journal' in paper:
    papers_output.write(paper['journal'].replace('. ','.\ ')+'\n')
  papers_output.write('[arXiv:'+paper['arxiv']+'].\n\n')

papers_output.write('\end{list}\n')


#################### mentoring file

mentoring_input = open("../_data/mentoring.yml","r")
mentoring_yaml = yaml.load(mentoring_input,Loader=yaml.BaseLoader)

########## postdocs file

postdocs_output = open("cv_postdocs.tex","w")
postdocs = mentoring_yaml['postdocs']
postdocs_output.write('\\bbl\n\n')

for person in postdocs:
  postdocs_output.write('\\item ')
  postdocs_output.write(person['name']+', ')
  postdocs_output.write(person['at'][0]['title']+', ')
  postdocs_output.write('\\emph{'+person['at'][0]['dates'].replace('-','--')+'}\n')
  if len(person['at']) == 2:
    postdocs_output.write('\\\\ \\sh '+person['at'][1]['title']+', ')
    postdocs_output.write('\\emph{'+person['at'][1]['dates'].replace('-','--')+'}\n')
  if 'after' in person:
    postdocs_output.write('\\\\ \\sh After MIT: '+person['after'][0]['title']+', \\emph{'+person['after'][0]['org']+'}\n')
    if len(person['after']) > 1:
      postdocs_output.write('\\\\ \\sh Currently: '+person['after'][-1]['title']+', \\emph{'+person['after'][-1]['org']+'}\n')
  if 'awards' in person:
    for award in person['awards']:
      postdocs_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
  postdocs_output.write('\n')

postdocs_output.write('\\el\n')

########## phd_students file

phd_students_output = open("cv_phd_students.tex","w")
phd_students = mentoring_yaml['phd_students']
phd_students_output.write('\\bbl\n\n')

for person in phd_students:
  phd_students_output.write('\\item ')
  phd_students_output.write(person['name']+', \\emph{')
  if 'current' in person and person['current']:
      phd_students_output.write('anticipated ')
  phd_students_output.write('Ph.D.~'+person['date']+'}\n')
  if 'thesis' in person:
    phd_students_output.write('\\\\ \\sh Thesis: ``'+person['thesis']+'\'\'')
    if 'joint' in person:
      phd_students_output.write(' \emph{(jointly advised with '+person['joint']+')}')
    phd_students_output.write('\n')
  if 'after' in person:
    phd_students_output.write('\\\\ \\sh After MIT: '+person['after'][0]['title']+', \\emph{'+person['after'][0]['org']+'}\n')
    if len(person['after']) > 1:
      phd_students_output.write('\\\\ \\sh Currently: '+person['after'][-1]['title']+', \\emph{'+person['after'][-1]['org']+'}\n')
  if 'awards' in person:
    for award in person['awards']:
      phd_students_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
  phd_students_output.write('\n')

phd_students_output.write('\\el\n')

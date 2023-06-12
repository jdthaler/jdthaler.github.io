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
postdocs_output.write('\\bbl\n')

for postdoc in postdocs:
  postdocs_output.write('\\item\n')
  postdocs_output.write(postdoc['name']+',\n')
  postdocs_output.write(postdoc['at'][0]['title']+',\n')
  postdocs_output.write('\\emph{'+postdoc['at'][0]['dates'].replace('-','--')+'}\n')
  if len(postdoc['at']) == 2:
    postdocs_output.write('\\\\ \\sh '+postdoc['at'][1]['title']+',\n')
    postdocs_output.write('\\emph{'+postdoc['at'][1]['dates'].replace('-','--')+'}\n')
  if 'after' in postdoc:
    postdocs_output.write('\\\\ \\sh After MIT: '+postdoc['after'][0]['title']+', \\emph{'+postdoc['after'][0]['org']+'}\n')
    if len(postdoc['after']) > 1:
      postdocs_output.write('\\\\ \\sh Currently: '+postdoc['after'][-1]['title']+', \\emph{'+postdoc['after'][-1]['org']+'}\n')
  if 'awards' in postdoc:
    for award in postdoc['awards']:
      postdocs_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
  postdocs_output.write('\n')

postdocs_output.write('\\el\n')








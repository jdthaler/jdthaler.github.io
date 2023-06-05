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





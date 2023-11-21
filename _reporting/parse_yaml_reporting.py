import yaml,os

### Reporting Talks

talks_input = open("../_data/talks.yml","r")
talks_yaml = yaml.load(talks_input,Loader=yaml.BaseLoader)
talks_output = open("thaler_reporting_talks.bib","w")

reporting_list = ["December 2022", "January 2023", "February 2023", "March 2023", "April 2023", "May 2023", "June 2023", "July 2023", "August 2023", "September 2023", "October 2023", "November 2023"]

for month in reporting_list:
  for categories in talks_yaml:
    for talk in talks_yaml[categories]:
      if 'title' in talk:
        if talk['date'] == month:
        
          string = '@conference{ThalerTalk:'
          string += talk['date'].replace(' ','_')
          string += '_'
          string += talk['org'].replace(' ','_').replace(',','')
          string += ',\n'
          
          string += 'author = {Thaler, Jesse},\n'
          
          string += 'title = {'
          string += talk['title']
          string += '},\n'

          string += 'note = {'
          string += talk['event']
          string += ', '
          string += talk['org']
          string += '},\n'

          string += 'year = {('
          string += talk['date']
          string += ')}}\n\n'

          talks_output.write(string)
          

### Reporting Papers

papers_input = open("../_data/papers.yml","r")
papers_yaml = yaml.load(papers_input,Loader=yaml.BaseLoader)
papers_output = open("thaler_reporting_papers.tex","w")

arxiv_start = 2212.10659

for paper in papers_yaml['papers']:
  arxiv_renum = paper['arxiv'].replace('hep-ph/0','20.').replace('hep-th/0','20.')
  if float(arxiv_renum) >= 2212.10659:
    string = '\cite{'
    string += paper['inspire']
    string += '}\n'
    
    papers_output.write(string)

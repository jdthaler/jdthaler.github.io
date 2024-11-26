import yaml,os
import datetime
from dateutil import parser

### Reporting Talks

talks_input = open("../_data/talks.yml","r")
talks_yaml = yaml.load(talks_input,Loader=yaml.BaseLoader)
talks_output = open("thaler_reporting_talks.bib","w")

reporting_list = ["December 2023", "January 2024", "February 2024", "March 2024", "April 2024", "May 2024", "June 2024", "July 2024", "August 2024", "September 2024", "October 2024", "November 2024"]

talks_to_report = []

for month in reporting_list:
  for category in talks_yaml['categories']:
    if category['doe_report'] == "true":
      for talk in talks_yaml[category['key']]:
        if 'title' in talk:
          if parser.parse(talk['date']).strftime("%B %Y") == month:
            talks_to_report.append(talk)

talks_to_report.sort(key=lambda r: parser.parse(r['date']).strftime("%s"))

for talk in talks_to_report:
  string = '@conference{ThalerTalk:'
  string += talk['date'].replace(' ','_')
#  string += '_'
#  string += talk['org'].replace(' ','_').replace(',','')
  string += ',\n'
  
  string += 'author = {Thaler, Jesse},\n'
  
  string += 'title = {{'
  string += talk['title']
  string += '}},\n'

  string += 'note = {'
  string += talk['event']
  string += ', '
  string += talk['org']
  string += '},\n'

  string += 'year = {('
  string += parser.parse(talk['date']).strftime("%B %-e, %Y")
  string += ')}}\n\n'

  talks_output.write(string)
          

### Reporting Papers

papers_input = open("../_data/papers.yml","r")
papers_yaml = yaml.load(papers_input,Loader=yaml.BaseLoader)
papers_output = open("thaler_reporting_papers.tex","w")

papers_to_report = []

arxiv_start = 2311.07652

for paper in papers_yaml['papers']:
  arxiv_renum = paper['arxiv'].replace('hep-ph/0','20.').replace('hep-th/0','20.')
  if float(arxiv_renum) >= arxiv_start:
    papers_to_report.append(paper)
    
papers_to_report.sort(key=lambda r: r['arxiv'])

for paper in papers_to_report:
  string = '\\cite{'
  if 'inspire' in paper:
    string += paper['inspire']
  else:
    string += arxiv_renum
  string += '}\n'
  
  papers_output.write(string)

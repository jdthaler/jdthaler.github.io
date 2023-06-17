import yaml,os


#################### functions

# copying from https://www.geeksforgeeks.org/python-get-unique-values-list/
def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    
    # output
    return unique_list



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

########## meng_students file

meng_students_output = open("cv_meng_students.tex","w")
meng_students = mentoring_yaml['meng_students']
meng_students_output.write('\\bbl\n\n')

for person in meng_students:
  meng_students_output.write('\\item ')
  meng_students_output.write(person['name']+', \\emph{')
  if 'current' in person and person['current']:
      meng_students_output.write('anticipated ')
  meng_students_output.write('M.Eng.~'+person['date']+'}\n')
  if 'thesis' in person:
    meng_students_output.write('\\\\ \\sh Thesis: ``'+person['thesis']+'\'\'')
    if 'joint' in person:
      meng_students_output.write(' \emph{(jointly advised with '+person['joint']+')}')
    meng_students_output.write('\n')
  if 'after' in person:
    meng_students_output.write('\\\\ \\sh After MIT: '+person['after'][0]['title']+', \\emph{'+person['after'][0]['org']+'}\n')
    if len(person['after']) > 1:
      meng_students_output.write('\\\\ \\sh Currently: '+person['after'][-1]['title']+', \\emph{'+person['after'][-1]['org']+'}\n')
  if 'awards' in person:
    for award in person['awards']:
      meng_students_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
  meng_students_output.write('\n')

meng_students_output.write('\\el\n')


########## urop_students file

urop_students_output = open("cv_urop_students.tex","w")
urop_students = mentoring_yaml['bs_students']
urop_students_output.write('\\bbl\n\n')

for person in urop_students:
  if 'urop' in person:
    urop_students_output.write('\\item ')
    urop_students_output.write(person['name']+' \''+person['date'][2:]+': ')
    urop_students_output.write('\\emph{'+person['urop']+'}')
    if 'thesis' in person:
      urop_students_output.write(' (see below) \n')
    else:
      if 'deceased' in person:
        urop_students_output.write(' (deceased) \n')
      else:
        urop_students_output.write('\n')
      if 'after' in person:
        urop_students_output.write('\\\\ \\sh After MIT: '+person['after'][0]['title']+', \\emph{'+person['after'][0]['org']+'}\n')
        if len(person['after']) > 1:
          urop_students_output.write('\\\\ \\sh Currently: '+person['after'][-1]['title']+', \\emph{'+person['after'][-1]['org']+'}\n')
      if 'awards' in person:
        for award in person['awards']:
          urop_students_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
    urop_students_output.write('\n')

urop_students_output.write('\\el\n')

########## bs_students file

bs_students_output = open("cv_bs_students.tex","w")
bs_students = mentoring_yaml['bs_students']
bs_students_output.write('\\bbl\n\n')

for person in bs_students:
  if 'thesis' in person:
    bs_students_output.write('\\item ')
    bs_students_output.write(person['name']+', \\emph{')
    if 'current' in person and person['current']:
        bs_students_output.write('anticipated ')
    bs_students_output.write('B.S.~'+person['date']+'}\n')
    if 'thesis' in person:
      bs_students_output.write('\\\\ \\sh Thesis: ``'+person['thesis']+'\'\'')
      if 'joint' in person:
        bs_students_output.write(' \emph{(jointly advised with '+person['joint']+')}')
      bs_students_output.write('\n')
    if 'after' in person:
      bs_students_output.write('\\\\ \\sh After MIT: '+person['after'][0]['title']+', \\emph{'+person['after'][0]['org']+'}\n')
      if len(person['after']) > 1:
        bs_students_output.write('\\\\ \\sh Currently: '+person['after'][-1]['title']+', \\emph{'+person['after'][-1]['org']+'}\n')
    if 'awards' in person:
      for award in person['awards']:
        bs_students_output.write('\\\\ \\sh '+award['name']+', \\emph{'+award['org']+', '+award['date']+'}\n')
    bs_students_output.write('\n')

bs_students_output.write('\\el\n')

########## visitors file

visitors_output = open("cv_visitors.tex","w")
visitors = mentoring_yaml['visitors']
visitors_output.write('\\bbl\n\n')

for person in visitors:
  visitors_output.write('\\item ')
  visitors_output.write(person['name']+', '+person['program']+', ')
  visitors_output.write('\\emph{'+person['dates'].replace('-','--')+'}\n')
  if 'project' in person:
    visitors_output.write('\\\\ \\sh Project: ``'+person['project']+'\'\'\n')
  visitors_output.write('\\\\ \\sh Home Institution: \emph{'+person['home'])
  if 'home_advisor' in person:
    visitors_output.write(' ('+person['home_advisor']+')}\n')
  else:
    visitors_output.write('}\n')
  visitors_output.write('\n')
  
visitors_output.write('\\el\n')


#################### talks file

talks_input = open("../_data/talks.yml","r")
talks_yaml = yaml.load(talks_input,Loader=yaml.BaseLoader)

########## generic talk writing file

def write_talks(output_file_name,text_string):

  talk_output = open(output_file_name,"w")
  colloquia = talks_yaml[text_string]
  talk_output.write('\\bbl\n\n')

  # get names of talks
  talk_names = []
  for talk in colloquia:
    talk_names.append(talk['title'])
  unique_talk_names = unique(talk_names)

  for talk_name in unique_talk_names:
    list_with_name = []
    for talk in colloquia:
      if talk_name == talk['title']:
        list_with_name.append(talk)
    talk_output.write('\\item ')
    talk_output.write('``'+talk_name+'\'\'')
    if len(list_with_name) > 1:
      talk_output.write('\n')
    else:
      talk_output.write(', ')
    
    for talk in list_with_name:
      if len(list_with_name) > 1:
        talk_output.write('\\\\ \\sh ')
      
      talk_output.write(talk['event']+', \emph{'+talk['org']+', '+talk['date']+'}')
      if 'virtual' in talk and talk['virtual']:
        talk_output.write(' (virtual)\n')
      else:
        talk_output.write('\n')
        
    talk_output.write('\n')

  talk_output.write('\\el\n')


########## colloquia file

write_talks("cv_colloquia.tex",'colloquia')
write_talks("cv_public_lectures.tex",'public')
write_talks("cv_schools.tex",'schools')


#################### teaching file

teaching_input = open("../_data/teaching.yml","r")
teaching_yaml = yaml.load(teaching_input,Loader=yaml.BaseLoader)

########## courses file

courses_output = open("cv_courses.tex","w")
courses = teaching_yaml['courses']
courses_output.write('\\bbl\n')

for course in courses:
  courses_output.write('\\item ')
  courses_output.write(course['number']+' --- '+course['title']+'\n')
  for role in course['roles']:
    courses_output.write('\\\\ \\sh ' + role['name'] + ': \\emph{')
    for iteration in role['iterations']:
      courses_output.write(iteration['date'])
      if iteration != role['iterations'][-1]: courses_output.write(', ')
    courses_output.write('}\n')

courses_output.write('\\el\n')


#################### funding file

funding_input = open("../_data/funding.yml","r")
funding_yaml = yaml.load(funding_input,Loader=yaml.BaseLoader)

########## grants file

grants_output = open("cv_grants.tex","w")
grants = funding_yaml['grants']
grants_output.write('\\bbl\n')

for grant in grants:
    grants_output.write('\\item '+grant['name'])
    if 'collaborators' in grant:
      grants_output.write(' (with '+grant['collaborators']+'),')
    else:
      grants_output.write(', ')
    if 'title' in grant:
      grants_output.write('``'+grant['title']+'\'\', ')
    grants_output.write('\\textit{'+grant['org']+', '+grant['dates'].replace('-','--')+'}\n')
    if 'amount' in grant:
      grants_output.write('('+grant['amount'].replace('$','\\$').replace('€','\\euro')+')')
    grants_output.write('\n')

grants_output.write('\\el\n')



#################### service file

service_input = open("../_data/service.yml","r")
service_yaml = yaml.load(service_input,Loader=yaml.BaseLoader)


########## internal service

internal_service_output = open("cv_internal_service.tex","w")
service_roles = service_yaml['mit_faculty'] + service_yaml['mit_sdsc'] + service_yaml['mit_physics'] + service_yaml['mit_lns'] + service_yaml['mit_ctp'] + service_yaml['mit_misti']
internal_service_output.write('\\bbl\n')

for role in service_roles:
  internal_service_output.write('\\item '+ role['name'] + ', \\emph{' + role['dates'].replace('-','--')+'}\n')
  if 'details' in role:
    for detail in role['details']:
      internal_service_output.write('\\\\ \\sh ' + detail+ '\n')

internal_service_output.write('\\el\n')


#################### advising file

advising_input = open("../_data/advising.yml","r")
advising_yaml = yaml.load(advising_input,Loader=yaml.BaseLoader)

########## advising file

advising_output = open("cv_advising.tex","w")
advising_output.write('\\bbl\n\n')

##### phd_theses

phd_theses = advising_yaml['phd_theses']
advising_output.write('\\item MIT Physics Ph.D. Thesis Committees:\n')
for phd_thesis in phd_theses:
  advising_output.write('\\\\ \\sh ' + phd_thesis['name'] + ' \\textit{('+phd_thesis['advisor'].replace('&','\\&')+', ')
  if 'date' in phd_thesis:
    advising_output.write(phd_thesis['date'])
  else:
    advising_output.write('in progress')
  advising_output.write(')}\n')
advising_output.write('\n')

##### academic_advising

advising_roles = advising_yaml['academic_advising']
for role in advising_roles:
  advising_output.write('\\item '+ role['name'] + ', \\emph{' + role['dates'].replace('-','--')+'}\n')
  if 'details' in role:
    for detail in role['details']:
      advising_output.write('\\\\ \\sh ' + detail+ '\n')
advising_output.write('\n')

##### external_phd_theses

external_phd_theses = advising_yaml['external_phd_theses']
advising_output.write('\\item External Ph.D. Examiner:\n')
for phd_thesis in external_phd_theses:
  advising_output.write('\\\\ \\sh ' + phd_thesis['name'] + ' \\textit{('+phd_thesis['advisor'].replace('&','\\&')+', '+phd_thesis['org']+', ')
  if 'date' in phd_thesis:
    advising_output.write(phd_thesis['date'])
  else:
    advising_output.write('in progress')
  advising_output.write(')}\n')
advising_output.write('\n')

##### external_mentoring

external_mentoring = advising_yaml['external_mentoring']
advising_output.write('\\item External Mentoring:\n')
for role in external_mentoring:
  advising_output.write('\\\\ \\sh ' + role['name'] + ', '+role['program']+', \\emph{' + role['dates'].replace('-','--')+'}\n')
advising_output.write('\n')

advising_output.write('\\el\n')

from django.shortcuts import render

import pandas as pd

from .models import PersonalInfo, EducationalInfo, Project, Skill, Follow, Experience

# Create your views here.

def portfolio_homepage(request):
  personal_info_list = PersonalInfo.objects.all()
  educational_info_list = EducationalInfo.objects.all()
  follow_list = Follow.objects.all()
  experience_list = Experience.objects.all()
  #Dataframe for skills grouping based on skill types
  skill_df = pd.DataFrame.from_records(Skill.objects.all().values())
  skill_dict = {}
  if not skill_df.empty:
    data_by_skill = skill_df.groupby(by='skill_type')
    for index, value in data_by_skill:
      skill_dict[index] = zip(list(value.iloc[:].technology), list(value.iloc[:].expertise_level))
  #Dataframe for projects grouping based on project types
  project_df = pd.DataFrame.from_records(Project.objects.all().values())
  project_dict = {}
  if not project_df.empty:
    data_by_project = project_df.groupby(by='project_type')
    for index, value in project_dict:
      project_dict[index] = zip(list(value.iloc[:].title), list(value.iloc[:].role), list(value.iloc[:].description), list(value.iloc[:].technology_used))
  #Context variable to pass to the template
  context = {'personal_infos': personal_info_list, 'educational_infos': educational_info_list, 'follows': follow_list, 'experiences': experience_list, 'skill_dict': skill_dict}
  return render(request, 'about/portfolio_homepage.html', context)

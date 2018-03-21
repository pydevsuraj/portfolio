from django.contrib import admin

from .models import PersonalInfo, EducationalInfo, Project, Skill, Follow, Experience

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(EducationalInfo)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Follow)
admin.site.register(Experience)

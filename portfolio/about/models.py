from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
  name = models.CharField(max_length=50)
  email = models.EmailField()
  contact = models.BigIntegerField()
  address = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  description = models.TextField()
  quotation = models.CharField(max_length=100)
  short_description = models.CharField(max_length=100)


class EducationalInfo(models.Model):
  level = models.CharField(max_length=50)
  faculty = models.CharField(max_length=100, blank=True, null=True)
  institute = models.CharField(max_length=100)
  board = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  enrolled_year = models.IntegerField()
  passed_year = models.IntegerField()
  grade_obtained = models.CharField(max_length=100)
  division = models.CharField(max_length=30)


class Project(models.Model):
  TYPE_CHOICES = [
    ('personal', 'Personal Project'),
    ('academic', 'Academic Project'),
    ('commercial', 'Commercial Project'),
  ]
  project_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
  title = models.CharField(max_length=100)
  role = models.TextField()
  description = models.TextField()
  technology_used = models.TextField()


class Skill(models.Model):
  SKILL_TYPE_CHOICES = [
    ('technical', 'Technical Skills'),
    ('database', 'Database'),
    ('vcs', 'Versioning Tools'),
    ('other', 'Other Tools'),
  ]
  skill_type = models.CharField(max_length=50, choices=SKILL_TYPE_CHOICES)
  technology = models.CharField(max_length=100)
  expertise_level = models.CharField(max_length=100)


class Follow(models.Model):
  github = models.URLField()
  linkedin = models.URLField()
  facebook = models.URLField()


class Experience(models.Model):
  company = models.CharField(max_length=100)
  position = models.CharField(max_length=50)
  role = models.TextField()
  start_date = models.CharField(max_length=30)
  end_date = models.CharField(max_length=30)
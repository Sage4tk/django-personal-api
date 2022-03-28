from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)
    github_link = models.CharField(max_length=255)
    technology = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField('date published')
    picture = models.FileField(upload_to='media/')
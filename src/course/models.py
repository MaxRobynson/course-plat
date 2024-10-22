from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    #acces = models.Choices()
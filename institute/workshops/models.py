from __future__ import unicode_literals

from django.db import models


#We can add category, but lets keep it simple
class Topic(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateField()


class Student(models.Model):
    name = models.CharField(max_length=90)
    lastname = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)


class Session(models.Model):
    name = models.CharField(max_length=90)
    topic = models.OneToOneField(Topic) #una unica relacion
    date = models.DateTimeField("Date and time")
    students = models.ManyToManyField(Student) # De una a muchas relaciones


# Create your models here.

from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64, unique=True)
    year_at_university = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    name = models.CharField(max_length=64, unique=True)
    lecturer = models.CharField(max_length=64)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

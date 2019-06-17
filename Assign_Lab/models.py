from django.db import models
from Add_Lab.models import *
from User_details.models import *


class IIYear(models.Model):
    Lab = models.ForeignKey(Lab2ndYEar, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='II_year_Lab_set')
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'II Year'


class IIIYear(models.Model):
    Lab = models.ForeignKey(Lab3rdYEar, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='III_Year_Teacher_set')
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'III Year'


class IVYear(models.Model):
    Lab = models.ForeignKey(Lab4thYEar, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(SignUp, on_delete=models.CASCADE, related_name='IV_Year_Teacher_set')
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'IV Year'



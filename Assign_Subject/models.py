
from django.db import models
from Add_Subject.models import *
from User_details.models import *


class IIYear(models.Model):
    Subject = models.ForeignKey(Subject2ndYEar, on_delete=models.CASCADE)
    Faculty = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'II Year'


class IIIYear(models.Model):
    Subject = models.ForeignKey(Subject3rdYEar, on_delete=models.CASCADE)
    Faculty = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'III Year'


class IVYear(models.Model):
    Subject = models.ForeignKey(Subject4thYEar, on_delete=models.CASCADE)
    Faculty = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    Lecture = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'IV Year'


from django.db import models


class Lab2ndYEar(models.Model):
    lab_name = models.CharField(max_length=50)
    lab_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'II year'

    def __str__(self):
        return self.lab_name


class Lab3rdYEar(models.Model):
    lab_name = models.CharField(max_length=50)
    lab_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'III year'

    def __str__(self):
        return self.lab_name


class Lab4thYEar(models.Model):
    lab_name = models.CharField(max_length=50)
    lab_code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'IV year'

    def __str__(self):
        return self.lab_name
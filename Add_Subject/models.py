from django.db import models


class Subject2ndYEar(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'II year'

    def __str__(self):
        return self.Name


class Subject3rdYEar(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'III year'

    def __str__(self):
        return self.Name


class Subject4thYEar(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'IV year'

    def __str__(self):
        return self.Name
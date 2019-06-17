from django.db import models


class DailyActivity(models.Model):
    year = models.CharField(max_length=10)
    sub = models.CharField(max_length=50)
    lecture = models.CharField(max_length=50)
    summary = models.TextField()
    faculty = models.CharField(max_length=50)
    Date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s' % self.year

from django.db import models


class Report(models.Model):
    Title = models.CharField(max_length=50)
    report = models.TextField()
    sender = models.CharField(max_length=50, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.Title

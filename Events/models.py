from django.db import models


class AddEvent(models.Model):
    Image = models.ImageField(upload_to='Event_Images', blank='true')
    Title = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return '%s' % self.Title


class UpcomingEvent(models.Model):
    description = models.TextField(blank='true')

    def __str__(self):
        return '%s' % self.description
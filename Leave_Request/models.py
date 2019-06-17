from django.db import models
from django.urls import reverse


class LeaveRequest(models.Model):
    Time = models.DateTimeField(auto_now=True)
    Sender_mail = models.EmailField()
    Sender = models.CharField(max_length=50)
    Application = models.TextField(max_length=5000)

    def __str__(self):
        return '%s' % self.Sender

    def get_absolute_url(self):
        return reverse('accept', kwargs={'id': self.id})

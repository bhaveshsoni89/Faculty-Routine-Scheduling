from django.db import models


class SignUp(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    experience = models.IntegerField()
    designation = models.CharField(max_length=30)
    profile = models.FileField(upload_to='Profile_image/', blank='true')

    def __str__(self):
        return '%s' % self.name


from django import forms


class SignForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    confirm = forms.CharField(max_length=30)
    contact = forms.IntegerField()
    dob = forms.DateField()
    gender = forms.CharField(max_length=30)
    qualification = forms.CharField(max_length=30)
    experience = forms.IntegerField()
    designation = forms.CharField(max_length=30)
    profile = forms.FileField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    comments = forms.CharField(max_length=200)
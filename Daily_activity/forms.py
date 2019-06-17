from django import forms


class DailyForm(forms.Form):
    year = forms.CharField(max_length=10)
    sub = forms.CharField(max_length=50)
    lecture = forms.CharField(max_length=50)
    summary = forms.CharField(max_length=100)
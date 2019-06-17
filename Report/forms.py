from django import forms


class ReportForm(forms.Form):
    Title = forms.CharField(max_length=50)
    report = forms.CharField(max_length=1000)
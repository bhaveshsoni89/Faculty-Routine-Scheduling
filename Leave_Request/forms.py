from django import forms


class LeaveForm(forms.Form):
    leave = forms.CharField(max_length=500)
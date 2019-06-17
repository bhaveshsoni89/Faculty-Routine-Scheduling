from django import forms


class SmsForm(forms.Form):
    sendto = forms.CharField(max_length=15)
    message = forms.Textarea()
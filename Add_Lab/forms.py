from django import forms


class LabForm2(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']


class LabForm3(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']


class LabForm4(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']
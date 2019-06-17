from django import forms


class SubjectForm2(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']


class SubjectForm3(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']


class SubjectForm4(forms.ModelForm):
    class Meta:
        fields = ['Name', 'Code']
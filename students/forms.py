from dataclasses import field
from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "ism",
            "famila",
            "yosh",
            "teacher"
        )

class StudentForm(forms.Form):
    ism = forms.CharField(max_length=15)
    famila = forms.CharField(max_length=15)
    yosh = forms.IntegerField(min_value=0)

 
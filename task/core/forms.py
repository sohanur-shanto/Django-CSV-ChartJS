from django import forms
from .models import *


class CsvModelForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name', )
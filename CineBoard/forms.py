from django import forms
from . import models


class MovieForm(forms.ModelForm):
    class Meta:
        model = models.Movie
        fields = '__all__'

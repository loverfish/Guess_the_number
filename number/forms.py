from django import forms

from .models import Number


class InputForm(forms.Form):
    number = forms.IntegerField()

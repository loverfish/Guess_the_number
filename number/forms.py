from django import forms

from .models import Number


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['digits_quantity']
        labels = {
            'digits_quantity': 'Enter the number of digits'
        }
        widgets = {'digits_quantity': forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество цифр',
            }
        )}


class InputForm(forms.Form):
    number = forms.IntegerField(
        label='Input the number',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите число',
        })
    )

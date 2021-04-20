from django import forms
from django.core.exceptions import ValidationError

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

    def clean_digits_quantity(self):
        new_digits_quantity = self.cleaned_data['digits_quantity']
        if new_digits_quantity not in range(1, 19):
            raise ValidationError('Введите количество цифр в диапозоне от 1 до 18')
        return new_digits_quantity


class InputForm(forms.Form):
    number = forms.IntegerField(
        label='Input the number',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите число',
        })
    )

    def clean_number(self):
        len_start_number = len(str(Number.objects.last().numb))
        new_number = str(self.cleaned_data['number'])
        if len(new_number) != len_start_number:
            raise ValidationError('Введите число из {} цифр'.format(len_start_number))
        return new_number

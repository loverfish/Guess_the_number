from django.shortcuts import render, redirect

from .forms import InputForm, NumberForm
from .models import Number
from .utils import create_number, compare_number


def start_game(request):
    form = NumberForm
    if request.method == 'POST':
        bound_form = NumberForm(request.POST)
        if bound_form.is_valid():
            digits_quantity = int(request.POST['digits_quantity'])
            Number.objects.create(numb=create_number(digits_quantity))
            return redirect('guess')
        form = bound_form
    return render(request, 'number/start_game.html', {'form': form})


def guess(request):
    start_number = str(Number.objects.last().numb)
    context = {
        'form': InputForm,
        'len': len(start_number),
    }
    if request.method == 'POST':
        bound_form = InputForm(request.POST)
        if bound_form.is_valid():
            input_number = request.POST['number']
            right_place, correct_digit = compare_number(input_number, start_number)
            if right_place == context['len']:
                return render(request, 'number/finish.html')
            context.update({
                'response': True,
                'right_place': right_place,
                'correct_digit': correct_digit,
            })
        context['form'] = bound_form

    return render(request, 'number/guess.html', {'context': context})


def about(request):
    return render(request, 'number/about.html')

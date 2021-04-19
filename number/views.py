from django.shortcuts import render, redirect

from .forms import InputForm, NumberForm
from .models import Number
from .utils import create_number, compare_number


def start_game(request):
    form = NumberForm
    if request.method == 'POST':
        Number.objects.create(numb=create_number())
        return redirect('guess')
    return render(request, 'number/start_game.html', {'form': form})


def guess(request):
    number = Number.objects.last().numb
    context = {
        'form': InputForm,
        'number': number,
        'len': len(str(number)),
    }
    if request.method == 'POST':
        input_number = request.POST['number']
        right_place, correct_digit = compare_number(input_number)
        if right_place == 5:
            return render(request, 'number/finish.html')
        context['response'] = 1
        context['right_place'] = right_place
        context['correct_digit'] = correct_digit
    return render(request, 'number/guess.html', {'context': context})


def about(request):
    return render(request, 'number/about.html')

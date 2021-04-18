import random

from .views import *


def create_number():
    return random.randint(10000, 99999)


def compare_number(numb):
    numb = str(numb)
    start_value = str(Number.objects.last().numb)
    right_place, correct_digit = 0, 0
    for i in range(len(str(numb))):
        if numb[i] == start_value[i]:
            right_place += 1
        if numb[i] in start_value and numb[:i].count(numb[i]) < start_value.count(numb[i]):
            correct_digit += 1
    return right_place, correct_digit

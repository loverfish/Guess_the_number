import random

from .views import *


def create_number(x=5):
    return random.randint(10**(x-1), 10**x - 1)


def compare_number(input_value, start_value):
    right_place, correct_digit = 0, 0
    for i in range(len(input_value)):
        if input_value[i] == start_value[i]:
            right_place += 1
        if input_value[i] in start_value and input_value[:i].count(input_value[i]) < start_value.count(input_value[i]):
            correct_digit += 1
    return right_place, correct_digit

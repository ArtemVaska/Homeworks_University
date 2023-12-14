"""
Написать программу на Python3, которая сначала запрашивает положительное число-основание системы счисления,
затем два числа в системе счисления с этим основанием, и потом четвертое число-основание системы счисления,
в которой надо вывести результат.
В ходе выполнения программа возвращает результат сложения двух чисел в требуемой системе счисления.
Нельзя использовать для перевода функцию int().
"""

import string


DIGITS = string.digits + 'ABCDEF'


def convert_to_decimal(number: str, base: int) -> int:
    result = 0
    for i, digit in enumerate(number):
        result += DIGITS.index(digit) * (base ** (len(number)-i-1))
    return result


def convert_from_decimal(number: int, base: int) -> str:
    result = ''
    while number:
        result += DIGITS[number % base]
        number //= base
    return result[::-1]


def addition(base_1: int, number_1: str, number_2: str, base_2: int) -> str:
    sum_value = convert_to_decimal(number_1.upper(), base_1) + convert_to_decimal(number_2.upper(), base_1)
    return convert_from_decimal(sum_value, base_2)


print(addition(2, '1001', '1111', 16))

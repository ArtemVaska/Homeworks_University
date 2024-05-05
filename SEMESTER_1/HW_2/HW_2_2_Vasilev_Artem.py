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
    """
    Конвертирует число из заданной системы счисления в десятичную.

    :param number: число в заданной системе счисления
    :param base: основание системы счисления заданного числа
    :return: число в десятичной системе счисления
    """
    result = 0
    for i, digit in enumerate(number):
        result += DIGITS.index(digit) * (base ** (len(number)-i-1))
    return result


def convert_from_decimal(number: int, base: int) -> str:
    """
    Конвертирует число из десятичной системы счисления в заданную.

    :param number: число в десятичсной системе счисления
    :param base: основание системы счисления, в которую нужно конвертировать
    :return: число в заданной системе счисления
    """
    result = ''
    while number:
        result += DIGITS[number % base]
        number //= base
    return result[::-1]


def addition(base_1: int, number_1: str, number_2: str, base_2: int) -> str:
    """
    Суммирует числа в заданной системе счисления и переводит в другую заданную систему счисления.

    :param base_1: изначальное основание системы счисления
    :param number_1: первое число из изначальной системы счисления
    :param number_2: второе число из изначальной системы счисления
    :param base_2: основание системы счисления, в которую нужно осуществить перевод после суммы
    :return: сумма двух чисел из заданной системы счисления в другой заданной системе счисления
    """
    sum_value = convert_to_decimal(number_1.upper(), base_1) + convert_to_decimal(number_2.upper(), base_1)
    return convert_from_decimal(sum_value, base_2)


print(addition(2, '1001', '1111', 16))  # 18
print(addition(16, '1E', 'A', 2))  # 101000

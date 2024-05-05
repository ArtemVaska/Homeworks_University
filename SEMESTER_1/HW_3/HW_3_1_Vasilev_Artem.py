"""
1. Переписать вычисление n-ного члена последовательности Фибоначчи с помощью рекурсии.
"""


def recursive_fibonacci(n):
    """
    Вычисляет n-й член последовательности Фибоначчи, используя рекурсивный подход.

    :param n: порядковый номер члена последовательности Фибоначчи
    :return: n-й член последовательности Фибоначчи
    """
    if n == 0 or n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


print(recursive_fibonacci(13))  # 377

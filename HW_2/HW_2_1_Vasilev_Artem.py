"""
Используя наборы символов из пакета string написать функцию, которая получает на вход строку и возвращает строку,
в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы.
Использовать функции стандартной библиотеки upper() и find() нельзя.

Добавить к предыдущему заданию функцию с преобразованием всех символов в прописные
и функцию с отражением (все заглавные становятся прописными и наоборот), минимально дублируя код.
Использовать функции стандартной библиотеки lower() и find() нельзя.
"""

import string


def string_upper(s: str) -> str:
    """
    Возвращает строку, в которой все буквы латинского алфавита из исходной строки преобразованы в заглавные символы.

    :param s: исходная строка
    :return: преобразованная строка
    """
    return s.translate(str.maketrans(string.ascii_lowercase, string.ascii_uppercase))


def string_lower(s: str) -> str:
    """
    Возвращает строку, в которой все буквы латинского алфавита из исходной строки преобразованы в прописные символы.

    :param s: исходная строка
    :return: преобразованная строка
    """
    return s.translate(str.maketrans(string.ascii_uppercase, string.ascii_lowercase))


def string_swapcase(s: str) -> str:
    """
    Возвращает строку, в которой все заглавные буквы латинского алфавита становятся прописными и наоборот.

    :param s: исходная строка
    :return: преобразованная строка
    """
    return s.translate(str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                     string.ascii_uppercase + string.ascii_lowercase))


print(string_upper('abcde'))  # ABCDE
print(string_lower('ABCDE'))  # abcde
print(string_swapcase('AbCdE'))  # aBcDe

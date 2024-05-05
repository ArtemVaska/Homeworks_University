# 1. Пользователь вводит число N, программа возвращает N-ный член последовательности Фибоначчи.
# Числа Фиббоначи: первые два члена 0 и 1. Каждый следующий член -- сумма двух предыдущих.

fib_list = [0, 1]
N = int(input('Enter the Fibonacci number index: '))

if N == 1:
    print(fib_list[0])
elif N == 2:
    print(fib_list[1])
else:
    i = 2
    while i < N:
        fib_list.append(fib_list[i-2] + fib_list[i-1])
        i += 1
    print(fib_list[-1])

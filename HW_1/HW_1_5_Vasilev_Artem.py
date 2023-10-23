# 5. Программа запрашивает число, а затем выводит квадрат из *, где длина стороны равна данному числу.

N = int(input('Enter a number: '))

side = '*' * N
for i in range(N):
    print(side)
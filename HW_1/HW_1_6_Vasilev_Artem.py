# 6. Программа запрашивает два числа, а затем выводит прямоугольник из *, где длины сторон равны данным числам.

a, b = (int(i) for i in input('Enter length and height separated by spaces: ').split())

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

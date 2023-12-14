# 4. Программа находит наибольший общий делитель для двух введенных чисел.

a, b = (int(i) for i in input('Enter 2 numbers separated by spaces: ').split())

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print('GCD is', a + b)

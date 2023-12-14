# 7. Программа запрашивает два числа и выводит на экран прямоугольник, в котором змейкой по вертикали записаны числа, начиная с 1.

a, b = (int(i) for i in input('Enter length and height separated by spaces: ').split())
values = []
ind = -1

for i in range(1, b+1):
    values.append([i])
    mult = 1
    ind += 1
    for j in range(1, a):
        values[ind].append(i + b * mult)
        mult += 1

for value in values:
    print(*value)

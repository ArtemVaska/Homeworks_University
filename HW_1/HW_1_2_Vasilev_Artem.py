#2. Пользователь вводит число, программа проверяет, является ли оно простым.

def is_prime(N):
    for divider in range(2, round(N/2) + 1):
        if N % divider == 0:
            return False
    return True

N = int(input('Enter a number to check: '))

if is_prime(N):
    print('The number is prime')
else:
    print('The number is NOT prime')
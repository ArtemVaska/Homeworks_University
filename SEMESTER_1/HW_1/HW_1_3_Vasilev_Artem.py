# 3. Программа возвращает простые делители введенного числа или сообщает, что оно простое.

def is_prime(N):
    for divider in range(2, round(N/2) + 1):
        if N % divider == 0:
            return False
    return True

N = int(input('Enter a number to analyse: '))

if is_prime(N):
    print('The number is prime')
else:
    prime_div_list = []
    for divider in range(2, round(N/2) + 1):
        if N % divider == 0:
            if is_prime(divider):
                prime_div_list.append(divider)
    print('The number is NOT prime. There are next prime dividers for it: ', *prime_div_list)

# Напишите функцию-генератор, которая генерирует бесконечную последовательность
# чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число,
# стотысячное число
from sys import set_int_max_str_digits

set_int_max_str_digits(1000000)


def fibonacci_sequence(n=1000000):
    f1 = 0
    f2 = 1
    num = 1
    while num < n:
        if num == 1:
            yield f1
        elif num == 2:
            yield f2
        else:
            sum_fib = f1 + f2
            yield sum_fib
            f1 = f2
            f2 = sum_fib
        num += 1


count = 1
for number in fibonacci_sequence(1000000):
    if count in {5, 200, 1000, 100000}:
        print(f'Fibonacci number {count} is {number}')
    count += 1

# Напишите программу: Есть функция которая делает одну из арифметических операций с
# переданными ей числами (числа и операция передаются в аргументы функции).
# Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение
def what_sign(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif (first < 0 and second >= 0) or (first >= 0 and second < 0):
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@what_sign
def calc(one, two, operation):
    if operation == '+':
        return one + two
    elif operation == '-':
        return one - two
    elif operation == '/':
        return one / two
    elif operation == '*':
        return one * two


num_1, num_2 = map(int, input('Enter 2 numbers: ').split())
result = calc(num_1, num_2, None)
print("Result:", result)

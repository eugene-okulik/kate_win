# Допустим, какая-то программа возвращает результат своей работы в таком виде:
#
# результат операции: 42
#
# результат операции: 514
#
# результат работы программы: 9
#
# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.

str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'

# ind_1 = str_1.index(':') + 2
# print(int(str_1[ind_1:]) + 10)
#
# ind_2 = str_2.index(':') + 2
# print(int(str_2[ind_2:]) + 10)
#
# ind_3 = str_3.index(':') + 2
# print(int(str_3[ind_3:]) + 10)


def result_plus_ten(str):
    ind = str.index(':') + 2
    print(int(str[ind:]) + 10)


result_plus_ten(str_1)
result_plus_ten(str_2)
result_plus_ten(str_3)

# Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary.
# А bonus пусть назначается рандомом.
#
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
#
# Примеры результатов:
#
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'
from random import randrange, choice

salary_with_bonus = 0
salary = int(input('Enter your salary: '))
bonus = choice([True, False])

salary_with_bonus = salary + randrange(1, 4000) if bonus else salary

print(f"{salary}, {bonus}, '${salary_with_bonus}'")

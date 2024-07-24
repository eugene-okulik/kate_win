# Есть такой список:
# temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
#                 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# Будем считать жарким всё, что выше 28.
#
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.
from statistics import mean

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
                23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
hot_days = list(hot_days)
print(hot_days)
print(f'Highest temperature: {max(hot_days)}')
print(f'Lowest temperature: {min(hot_days)}')
print(f'Average temperature: {round(mean(hot_days))}')
print(f'Average temperature: {round(sum(hot_days)/len(hot_days))}')

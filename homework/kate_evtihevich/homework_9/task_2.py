# Дана такая дата: "Jan 15, 2023 - 12:05:33"
#
# Преобразуйте эту дату в питоновский формат, после этого:
#
# 1. Распечатайте полное название месяца из этой даты
#
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"
import datetime

some_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(some_date, '%b %d, %Y - %X')
print(python_date.strftime('%B'))

human_date = python_date.strftime('%d.%m.%Y, %I:%M')
print(human_date)

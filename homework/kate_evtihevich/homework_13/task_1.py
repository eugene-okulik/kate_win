# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: (
# homework/eugene_okulik/hw_13/data.txt)
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
# находит в нём даты и делает с этими датами то, что после них написано.
# Опирайтесь на то, что структура каждой строки одинакова: сначала идет номер, потом дата,
# потом дефис и после него текст. У вас должен получиться код, который находит даты и
# для даты под номером один в коде должно быть реализовано то действие, которое написано
# в файле после этой даты. Ну и так далее для каждой даты.
# data.txt
# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже.
# Должно получиться 2023-12-04 20:34:13.212967
# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата
import os
import datetime
base_path = os.path.dirname(__file__)

homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')


def read_file():
    with open(file_path, encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        parts = data_line.split(' - ')
        number = int(parts[0][:1])
        date_str = parts[0][3:]
        action = parts[1]
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if number == 1:
            print(date_obj + datetime.timedelta(days=7))
        elif number == 2:
            print(date_obj.strftime('%A'))
        elif number == 3:
            print((datetime.datetime.now() - date_obj).days)

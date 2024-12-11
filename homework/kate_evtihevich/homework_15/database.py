"""
Создайте в базе данных полный набор информации о студенте, заполнив все таблички
1. Создайте студента (student)
2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их
3. Создайте группу (group) и определите своего студента туда
4. Создайте несколько учебных предметов (subjects)
5. Создайте по два занятия для каждого предмета (lessons)
6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий
Получите информацию из базы данных:
1. Все оценки студента
2. Все книги, которые находятся у студента
3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
"""

import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)
insert_query_1 = "INSERT INTO students (name, second_name) VALUES ('Artem', 'Yanush')"
cursor.execute(insert_query_1)
student_id = cursor.lastrowid

insert_query_2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query_2, [
        ('Children of Underground', student_id),
        ('Children of Captain Grant', student_id)
    ]
)

insert_query_3 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query_3, ('5G', '01-09-2024', '31-05-2024'))
gr_id = cursor.lastrowid

update_query = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_query, (gr_id, student_id))

insert_query_4 = "INSERT INTO subjets (title) VALUES (%s)"
cursor.executemany(insert_query_4, [('Mathematics',), ('English',), ('Labor',)])
math_id = cursor.lastrowid
eng_id = cursor.lastrowid + 1
labor_id = cursor.lastrowid + 2
print(math_id, eng_id, labor_id)

insert_query_5 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_values = [
    ('Multiplication laws', math_id),
    ('Equations', math_id),
    ('Tenses in English', eng_id),
    ('Subjunctive mood', eng_id),
    ('Work with a jigsaw', labor_id),
    ('Handmade Christmas tree', labor_id)
]
cursor.executemany(insert_query_5, lesson_values)
mult_id = cursor.lastrowid
equations_id = cursor.lastrowid + 1
tenses_id = cursor.lastrowid + 2
subjunctive_id = cursor.lastrowid + 3
jigsaw_id = cursor.lastrowid + 4
tree_id = cursor.lastrowid + 5
print(mult_id, equations_id, tenses_id, subjunctive_id, jigsaw_id, tree_id)

insert_query_6 = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_values = [
    ('Excellent', mult_id, student_id),
    ('A*', equations_id, student_id),
    ('A', tenses_id, student_id),
    ('B', subjunctive_id, student_id),
    ('C', jigsaw_id, student_id),
    ('D', tree_id, student_id)
]
cursor.executemany(insert_query_6, marks_values)

db.commit()

select_query_1 = '''
SELECT s.name, s.second_name, m.value
FROM students s
JOIN marks m
ON s.id = m.student_id
WHERE s.id = %s
'''

cursor.execute(select_query_1, (student_id,))
print(cursor.fetchall())

select_query_2 = '''
SELECT s.name, s.second_name, b.title
FROM students s 
JOIN books b 
ON s.id = b.taken_by_student_id 
WHERE s.id = %s
'''

cursor.execute(select_query_2, (student_id,))
print(cursor.fetchall())

select_query_3 = '''
SELECT  
s.name, 
s.second_name, 
g.title AS group_title, 
b.title AS book_title, 
m.value AS mark, 
l.title AS lesson_title, 
s2.title AS subject_title 
FROM students s
JOIN `groups` g 
ON s.group_id = g.id
JOIN books b 
ON s.id = b.taken_by_student_id 
JOIN marks m
ON s.id = m.student_id
JOIN lessons l
ON m.lesson_id = l.id 
JOIN subjets s2
ON l.subject_id = s2.id 
WHERE s.id = %s
'''
cursor.execute(select_query_3, (student_id,))
print(cursor.fetchall())

db.close()

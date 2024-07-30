# Библиотека
# Первый класс
# Создайте класс book с атрибутами:
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага
# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников.
# В нем будут дополнительные атрибуты:
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной.
# class - зарезервированное слово), наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9
class Book:
    material = 'paper'
    text = True

    def __init__(self, title, author, pages, ISBN, is_reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.is_reserved = is_reserved

    def read(self):
        print('Enjoy reading')

    def reserve(self):
        self.is_reserved = True

    def info(self):
        print(f'Title: {self.title}, Author: {self.author}, pages: {self.pages}, '
              f'material: {self.material}, reserved') if self.is_reserved else (
            print(f'Title: {self.title}, Author: {self.author}, pages: {self.pages}, material: {self.material}'))


dostoevsky_idiot = Book('Idiot', 'Dostoevsky',  500, 1234567)
verne_captain = Book("Captain Grants Children", 'Verne', 607, '4803020000-069')
tolkien_hobbit = Book("The Hobbit", 'Tolkien', 351, '5-8352-0009-9')
nosov_dunno = Book('Dunno on the moon', 'Nosov', 432, 9785389176713)
lewis_narnia = Book('Chronicles of Narnia', 'Lewis', 907, '978-5-699-92300-7')

dostoevsky_idiot.read()
dostoevsky_idiot.reserve()
dostoevsky_idiot.info()
nosov_dunno.info()


class TextBook(Book):
    def __init__(self, title, author, pages, ISBN, subject, grade, is_tasks):
        super().__init__(title, author, pages, ISBN)
        self.subject = subject
        self.grade = grade
        self.is_tasks = is_tasks

    def read(self):
        print('read attentively, do tasks')

    def info(self):
        if self.is_reserved:
            print(f'Title: {self.title}, Author: {self.author}, pages: {self.pages}, '
                  f'subject: {self.subject}, grade: {self.grade}, reserved')
        else:
            print(f'Title: {self.title}, Author: {self.author}, pages: {self.pages}, '
                  f'subject: {self.subject}, grade: {self.grade}')


algebra_9_ivanov = TextBook('Algebra', 'Ivanov', 200, 322223,
                            'Mathematics', 9, True)

history_5_prohorov = TextBook('Ancient world history', 'Prohorov', 140,
                              '978-985-03-3085-7', 'History', 5, True)

biology_11_dashkov = TextBook('Biology', 'Dashkov', 305,
                              '978-985-03-3616-3', 'Biology', 11, False)

biology_11_dashkov.read()

history_5_prohorov.reserve()
algebra_9_ivanov.info()
history_5_prohorov.info()
biology_11_dashkov.info()

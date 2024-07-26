# Создайте универсальный декоратор, который можно будет применить к любой функции.
# Декоратор должен делать следующее: он должен распечатывать слово "finished"
# после выполнения декорированной функции.
# В результате работы будет такое:
#
# print me
# finished
def finish_me(func):

    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')

# Создать декоратор, который сможет обработать такой код:
#
# @repeat_me(count=2)
# def example(text):
#     print(text)
#
# example('print me')
#
def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=5)
def example(text):
    print(text)


example('print me')

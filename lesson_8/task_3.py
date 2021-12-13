from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for i in args:
            print(f'{func.__name__} ({i}: {type(i)})')
            return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        return f'{i ** 3}'


# Решил расписать декоратор в зависимости о того какие аргументы подаются при вызове
if __name__ == '__main__':
    print(calc_cube(5))

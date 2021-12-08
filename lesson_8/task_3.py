from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        gen_kwargs = [f'{func.__name__}({i}: {type(i)})' for i in kwargs.values()]
        gen_args = [f'{func.__name__}({i}: {type(i)})' for i in args]
        if len(kwargs) and len(args) > 0:  # если подаются  args и kwargs
            while gen_kwargs:
                gen_args.append(gen_kwargs[0])
                del gen_kwargs[0]
            print(*gen_args,  sep=', ')
        elif len(kwargs) > 0:  # если подаётся kwargs
            print(*gen_kwargs, sep=', ')
        elif len(args) > 0:  # если подаётся args
            print(*gen_args, sep=', ')

    return wrapper


@type_logger
def calc_cube(*args):
    for i in args:
        print(f'{i ** 3}')


# Решил расписать декоратор в зависимости о того какие аргументы подаются при вызове
if __name__ == '__main__':
    calc_cube(5, 6, f=7, d=8)
    calc_cube(a=5, b=6, с=7, f=8)
    calc_cube(5, 6, 7, 8)

# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
# ...
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
# return x ** 3
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
# ...
# raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?
def val_checker(func):

    def _val_checker(args):
        nonlocal func

        def wrapper(*args, **kwargs):
            print(func)
            try:
                valid_args = list(map(func, args))
                print(valid_args)
            except ValueError as e:
                print(f'{e}: {args} < 0')
        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(5)

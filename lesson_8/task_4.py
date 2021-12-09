def val_checker(func):  # декорирующая функция с аргументом лямбда функции

    def _val_checker(calk):  # функция с аргументом основной функции
        nonlocal func

        def wrapper(*x, **kwargs):  # фунция с аргументом (который передан основной функции)
            valid_x = func(*x)  # проверка валидности входных данных
            if valid_x:
                calk(*x)
            else:
                raise ValueError(f'ValueError : wrong val {x[0]}')
        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return print(x ** 3)


if __name__ == '__main__':
    calc_cube(5)
    calc_cube(-5)
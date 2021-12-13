def val_checker(callback):  # декорирующая функция с аргументом лямбда функции

    def _val_checker(calk):  # функция с аргументом основной функции

        def wrapper(*x):  # фунция с аргументом (который передан основной функции)
            valid_x = callback(*x)  # проверка валидности входных данных
            if valid_x:
                return calk(*x)
            else:
                raise ValueError(f'ValueError : wrong val ')
        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(-5))

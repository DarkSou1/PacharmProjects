"""
Написать функцию, которая принимает в качетсве аргументов имена сотрудников
и возвращает словать, в котором ключи - первые буквы имён, а значения
- списки содержащие имена, начинающиеся с соответсвующей буквы.
"""


def thesaurus(*args):
    """

    :param args: Принимает имена сотрудников
    :return: Возвращает словарь где первая буква имени ключ словаря
    """
    worker = {}
    for name in args:
        f_letter = name[0]
        if f_letter not in worker:
            worker.setdefault(f_letter, [])
            worker[f_letter].append(name)
    print(worker)


thesaurus('Мирон', 'Петр', 'Илья', 'Иван', 'Мария')

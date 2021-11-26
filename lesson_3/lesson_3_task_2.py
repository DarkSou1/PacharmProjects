"""
Реализовать задачу 1, корректную работу с числительными, которые начинаются
с заглавной буквы  - результат тоже должен быть с заглавной буквы
"""


def num_translate_adv(num):
    """
    Переводит числа от 1 до 10
    :param num: параметр для перевода
    :return: значение с заглавной буквы
    """
    translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                      'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                      'nine': 'девять', 'ten': 'десять'
                      }
    if num.istitle():
        num = num.lower()
        val = translate_dict[num]
        print(val.capitalize())
    else:
        return None


num_translate_adv('One')
num_translate_adv('Two')
num_translate_adv('Three')
num_translate_adv('Four')
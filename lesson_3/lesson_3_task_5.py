from random import choice
import random


def get_jokes(amout, flag=0):
    """
    Генерирует рандомные шутки!
    :param flag:
    :param amout: количество шуток, которое должно быть
    :print: выводит шутки
    """
    nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
    adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
    adjectives = ['веселый', 'яркий', 'зелёный', 'утопичный', 'мягкий']
    if flag == 1:
        for jokes in range(1, amout + 1):
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            rdm_jokes = f'{nouns.pop()} {adverbs.pop()} {adjectives.pop()}'
            print(rdm_jokes)
    else:
        for jokes in range(1, amout + 1):
            rdm_jokes = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
            print(rdm_jokes)


get_jokes(5, 1)


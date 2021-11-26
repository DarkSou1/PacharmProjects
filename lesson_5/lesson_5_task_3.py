names = ['Иван', 'Анастасия', 'Петр', 'Сергей',
         'Дмитрий', 'Борис', 'Елена'
         ]
klss = ['9А', '7В', '9Б',
        '10Б', '9А'
        ]


def len_lists(x, y):
    for i in range(0, len(x)):
        if len(x) > len(y):
            y.append('None')
    return


len_lists(names, klss)
generator = (x for x in zip(names, klss))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))
print(next(generator), type(generator))

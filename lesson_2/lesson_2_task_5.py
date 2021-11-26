cost_list = [48.56, 59.52, 187.0, 12.15, 15.12,
             99.99, 21.32, 158.0, 136.13, 13.21
             ]
print(f'Исходный список: Область памяти {id(cost_list)}')
print('-' * 50)
cost_list.sort()
cost_list_s = sorted(cost_list, reverse=True)


def sort_list(list):
    cost = 0
    while cost < len(list):
        item = str(list[cost])  # приведение к строке взятие цифр после запятой
        item = item[item.index('.'):]  # обрезка точки
        item = item.split('.')[1]  # присвоение цифр посл точки
        if item.isdigit():  # проверка на число, и приведение к двум знакам (при 0)
            item = int(item)
            item = f'{item:02d}'
        else:
            break
        mod_item = int(list[cost])  # целая часть
        new_costs = f'{mod_item} руб {item} коп' # объединение в форматированную строку (рубли и копейки)
        list[cost: cost + 1] = [new_costs] # замена элементов списка in place
        cost += 1
    print(f'Изменённый список {",".join(list)}, область памяти {id(list)}')
    print('-' * 50)
    return list


sort_list(cost_list)
sort_list(cost_list_s)

print(f'Максимальные значения: {",".join(cost_list_s[:5])}')


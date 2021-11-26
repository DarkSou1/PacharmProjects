import sys

some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'ID исходного списка {id(some_list)} Количество занимаемой памяти {sys.getsizeof(some_list)}')
print(some_list)
index = 0
list_2 = []


def quotes_in_item(index):
    index = ['"', index, '"']
    index = ''.join(index)
    return index


for index in some_list:
    if (index[0] == '-' or index[0] == '+') and index[1:].isdigit():
        int_index = int(index)
        index = index[0] + f'{int_index:02d}'
        list_2.append(quotes_in_item(index))
    elif index.isdigit():
        a = int(index)
        index = f'{a:02d}'
        list_2.append(quotes_in_item(index))
    else:
        list_2.append(index)

print(f'ID нового списка {id(list_2)} Количество занимаемой памяти {sys.getsizeof(list_2)}')
print(list_2)
format_string = ' '.join(list_2)
print(f'Отформатированная строка :{format_string}')
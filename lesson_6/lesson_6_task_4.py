import json


def read_lines(file_path, mutable=False):
    with open(file_path, 'r', encoding='utf-8') as file:
        for out_line in file:
            if mutable:
                # Использую множества т.к. хобби в одной строке не могут повтор и порядок не важен
                yield list(out_line.rstrip().split(','))
            else:
                # Использую кортежи т.к. порядок важен
                yield str(out_line.rstrip().split(','))
        else:
            # Маркер что это конец файла - я бы использовал try
            yield 'end_file'


def save_result(input_dict, file_path):
    with open(file_path, 'w') as f:
        result_s    
        json.dump(input_dict, f)


def main():
    path_user = input('Введите путь к файлу пользователей: ')
    path_hobby = input('Введите путь к файлу хобби: ')
    path_result = input('Введите путь к файлу результатов: ')

    result_dict = {}

    file_user = read_lines(path_user)
    file_hobby = read_lines(path_hobby, mutable=True)

    item_hobby = next(file_hobby)
    for item_user in file_user:
        if item_user == 'end_file':
            # Пользуюсь тем что это последняя итерация - не выхожу через break для выполнение условия else у цикла
            continue

        if item_hobby == 'end_file':
            # Исчерпание файла хобби
            item_hobby = None
        # Блок формирования единого словаря
        result_dict[item_user] = item_hobby
        if item_hobby:
            # Получаем следующее множество хобби (если сюда не зашли файл с хобби исчерпан)
            item_hobby = next(file_hobby)
        # --------------------------------
    else:
        # сюда приходим если отработали весь файл пользователей без ошибки
        save_result(result_dict, path_result)
        print('[*] - файл со словарём записан')
        print(result_dict)


# --------------------------------------------------------------------------------
if __name__ == '__main__':
    exit(main())
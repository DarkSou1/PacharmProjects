import os
from collections import defaultdict
import json
'''
Нужно создать словарь в котором кортеж из количества файлов и списка расширений
'''

def create_dict_files(root_dir):
    test_dict = defaultdict(list)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_size = os.stat(os.path.join(root, file)).st_size
            ext = file.split('.')[-1]
            range_size = 10 ** len(str(file_size))
            test_dict[range_size].append(ext)
    return result_dict(test_dict)


def result_dict(args):
    tuple_dict = {}
    for range_size, ext in sorted(args.items()):
        list_ext = set(ext)
        tuple_dict[range_size] = (len(ext), list(list_ext))
    return tuple_dict


def create_json_file(path_file, result):
    with open(path_file, 'w', encoding='utf-8') as f:
        json.dump(result, f)


if __name__ == '__main__':
    root_dir = input('Какую папку будем просматривать?: ')
    foler_name = root_dir.split(os.sep)[-1]
    result_json_file = os.path.join(root_dir, foler_name + 'result.json')
    create_dict_files(root_dir)
    create_json_file(result_json_file, create_dict_files(root_dir))

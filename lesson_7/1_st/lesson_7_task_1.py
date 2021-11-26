# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
# |--settings
# |--mainapp
# |--adminapp
# |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
# лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?
import os


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            list_dirs = [line.rstrip() for line in f]
            create_dirs(list_dirs)
    except FileNotFoundError as e:
        print(e)


def create_dirs(args):
    """
    Receives and processes a list to create a folder hierarchy
    :param args: list_dirs
    :return: Directory
    """
    root_dir = args[0]
    args = args[1:]
    try:
        for dir in args:
            if not os.path.exists(os.path.join(root_dir, dir)):
                os.makedirs(os.path.join(root_dir, dir))
            else:
                raise FileExistsError
    except FileExistsError as e:
        print(e)


if __name__ == '__main__':
    import sys
    exit(read_file(sys.argv[1]))

# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
# {
# 100: 15,
# 1000: 3,
# 10000: 7,
# 100000: 2
# }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
root_dir = r'C:\Users\Артём\Desktop\Курсы_python\01_Basic_Python\lesson_007\some_data\some_data'
files_size = [100, 1000, 5000, 10000]
size_dict = {}
try:
    for i in files_size:
        small_files = [item.name
                       for item in os.scandir(root_dir)
                       if i < item.stat().st_size < files_size[1]]
        files_size = files_size[1:]
        size_dict[i] = len(small_files)
except IndexError as e:
    pass
finally:
    print(size_dict)

# print(small_files == small_files_2)


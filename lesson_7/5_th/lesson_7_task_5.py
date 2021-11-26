# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>]), например:
# {
# 100: (15, ['txt']),
# 1000: (3, ['py', 'txt']),
# 10000: (7, ['html', 'css']),
# 100000: (2, ['png', 'jpg'])
# }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
import os

size_stats = {}
for item in os.scandir(r'C:\Users\Артём\PycharmProjects'):
    if item.is_file():
        size = item.stat().st_size
        threshold = 10 ** len(str(size))
        ext = item.name.split('.')[-1]
        try:
            size_stats[threshold][0] += 1
            ext_list = size_stats[threshold][1]
            print(size_stats)
            if ext in ext_list:
                pass
            else:
                ext_list.append(ext)
        except (KeyError, IndexError):
            size_stats[threshold] = [1, [ext]]
print(size_stats)

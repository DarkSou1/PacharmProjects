# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
# расположены в родительских папках (они играют роль пространств имён); предусмотреть
# возможные исключительные ситуации; это реальная задача, которая решена, например, во
# фреймворке django.
import os
import shutil

root_dir = r'C:\Users\Артём\PycharmProjects\lesson_7\2_nd\my_project'
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            dir_name = os.path.join('templates', os.path.basename(root))
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            shutil.copyfile(os.path.join(root, file), os.path.join(dir_name, file))

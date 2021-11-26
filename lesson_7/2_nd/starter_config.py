import os
from pathlib import Path

with open('config.yaml', 'r', encoding='utf-8') as f:
    root_folder = Path.cwd()
    nest_level = 0
    for line in f:
        process_line = line.strip(': -\n\r')
        if line.endswith(':\n'):
            if line.index('-') == nest_level:
                root_folder = root_folder.joinpath(process_line)
            elif line.index('-') > nest_level:
                root_folder = root_folder.joinpath(process_line)
            elif line.index('-') < nest_level:
                root_folder = Path(root_folder).parents[0]
                root_folder = root_folder.joinpath(process_line)
            os.mkdir(root_folder)
        else:
            file_name = root_folder.joinpath(process_line)
            if not os.path.exists(file_name):
                open(file_name, 'w').close()
        nest_level = line.index('-')

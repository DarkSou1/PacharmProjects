import json
from itertools import zip_longest


def file_reader():
    """
    This funtction read files from files
    :return: two lists (user_list, hobby_list)
    """
    with open('Users', 'r', encoding='utf-8') as f:
        users_list = [x.replace(',', '').replace('\n', '') for x in f]
    with open('Hobby', 'r', encoding='utf-8') as f:
        hobby_list = [x.replace('\n', '') for x in f]
    if len(users_list) < len(hobby_list):
        exit(1)
    else:
        file_dict = dict(zip_longest(users_list, hobby_list))
    with open('users_hobby.txt', 'w', encoding='utf-8') as f:
        file_dict_str = json.dumps(file_dict)
        f.write(file_dict_str)


file_reader()

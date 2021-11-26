import json

import requests


def request(*args):
    """
    This function are scraping text from url
    and split lines
    :param args: file with logs in test format
    :return: list with lines arguments
    """
    with open('logs.txt', 'w', encoding='UTF-8') as f:
        f.write(*args)
    with open('logs.txt', 'r', encoding='UTF-8') as f:
        list_logs = []
        for line in f:
            line = line.split(' ')
            remote_addr = line[0]
            request_type = line[5].strip('"')
            requested_resourse = line[6]
            new_tuple = (remote_addr, request_type, requested_resourse)
            list_logs.append(new_tuple)
        print(list_logs)


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
logs_text = response.text
request(logs_text)
"""
with open('ngixn_logs.txt', 'w', encoding='utf-8') as f:
    list_log_str = json.dumps(request(logs_text))  # переводим в json формат, для уменьшения объёма памяти
    f.write(list_log_str)
# правда после того как мы всё переделали в json возникла проблема,
# tuple стал list и я пока не знаю как с этим разобраться
"""

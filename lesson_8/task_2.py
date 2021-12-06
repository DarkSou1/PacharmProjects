# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
# урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# ) для получения информации вида: (<remote_addr>, <request_datetime>,
# <request_type>, <requested_resource>, <response_code>, <response_size>),
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
# /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
import re
import json
import requests
import os


def logs_create(file_name, url):
    """
    Create file with logs from url_adress
    :param args: file_name
    :return: None
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        response = requests.get(url)
        logs_text = response.text.split('\n')
        gen_line = [logs_text[line] for line in
                    range(len(logs_text))]  # списковое включение для создания файла
        f.write(json.dumps(gen_line))


def re_parser(arg):
    """
    Parse strings from file with module "re"
    :param arg: file_name
    :return: tuple
    """
    with open(arg, 'r', encoding='utf-8') as f:
        gen_line = f.read()
        gen_line = json.loads(gen_line)
        RE_ADDR = re.compile(r'(?:[\d+[\.]+\d{2,4}[\.]+\d+[\.]+\d)')
        for item in gen_line:
            print(RE_ADDR.findall(item))


if __name__ == '__main__':
    url_logs = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    file_name = 'logs.json'
    if not os.path.exists(file_name):  # проверка на наличие файла в директории запуска скрипта
        logs_create(file_name, url_logs)
    re_parser(file_name)

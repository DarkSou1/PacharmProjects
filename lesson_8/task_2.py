import json
import os
import re
import requests


def logs_create(file_name, url):
    """
    Create file with logs from url_adress
    :param file_name: file_name
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
        for item in gen_line:
            try:
                RE_RESPONSE_SIZE = re.search(r'(\d{3}\s+\d)', item)
                RE_ADDR = re.search(r'(?:[\d{1,4}+[.]+\d{1,4}[.]+\d{1,4}[.]+\d{1,4})', item)
                RE_DATETIME = re.search(r'(\d{2}/\w+/\w+:\w{2,}:\w{2,}:\w{2,}\s\+\w+)', item)
                RE_REQUEST_TYPE = re.search(r'([A-Z]{3})+[\s]', item)
                RE_RESOURSE = re.search(r'(/+\w+/+\w+_\d+)', item)
                tuple_response = (RE_ADDR.group(0), RE_DATETIME.group(0), RE_REQUEST_TYPE.group(0),
                                  RE_RESOURSE.group(0), RE_RESPONSE_SIZE.group(0))
                print(tuple_response)
            except:  # перехватывает не валидные логи и создаёт отдельный файл для просмотра
                with open('non_valide.json', 'a', encoding='utf-8') as f:
                    non_valid_list = []
                    non_valid_list.append(item)
                    f.writelines(json.dumps(non_valid_list))


if __name__ == '__main__':
    url_logs = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    file_name = 'logs.json'
    if not os.path.exists(file_name):  # проверка на наличие файла в директории запуска скрипта
        logs_create(file_name, url_logs)
    re_parser(file_name)

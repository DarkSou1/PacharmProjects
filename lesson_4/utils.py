import requests
from bs4 import BeautifulSoup
from datetime import date


def str_to_date(date_server):
    """
    Convert string to date format
    :return: Value in date
    """
    date_server = date_server.split('.')  # convert string to list
    date_server = date(int(date_server[2]), int(date_server[1]), int(date_server[0]))
    return date_server


def ratio():
    """
    Calculation of the ratio of the currency to one ruble
    :return: value for one ruble
    """
    ratio_list = []
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    amount = soup.find_all('nominal')
    value = soup.find_all('value')
    amount_list = []
    value_list = []
    for amount in amount:
        amount_list.append(amount.text)
    for value in value:
        value_fl = float(value.text.replace(',', '.'))
        value_list.append(value_fl)
    for i in range(0, len(value_list)):
        summa = value_list[i] / int(amount_list[i])
        summa = format(summa, '.2f')
        ratio_list.append(summa)
    return ratio_list


def currensy_rates(key):
    """
    Вызывает значение валюты с сайта и возвращает его отношение к рублю
    :return: валюта
    """
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    charcode = soup.find_all('charcode')
    date_server = soup.valcurs['date']
    charcode_list = []
    ratio()
    for charcode in charcode:
        charcode_list.append(charcode.text)
    result_dict = dict(zip(charcode_list, ratio()))
    if key.isalpha():
        key = key.upper()
    if key in result_dict.keys():
        print(f'Валюта {key} по отношению к рублю {result_dict[key]} на {str_to_date(date_server)}')
    elif key not in result_dict.keys():
        return print('Нет такой валюты')

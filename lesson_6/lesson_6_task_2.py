import requests
from collections import Counter

def spammers_list(*args):
    with open(*args, 'r', encoding='utf-8') as f:
        spammers_id = []
        for line in f:
            line = line.split(' ')
            spammer = line[0]
            spammers_id.append(spammer)
    return spammers_id


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
response = requests.get(url)
logs = response.text
with open('task_2.txt', 'w', encoding='utf-8') as f:
    f.write(logs)
    result = spammers_list('task_2.txt')
    result_dict = dict((i, result.count(i)) for i in result)
    max_val = max(result_dict.values())
    result_dict = {k: v for k, v in result_dict.items() if v == max_val}
    print(result_dict)

import re  # импортируем бибилиотеку регулярных выражений


def email_parse(email_adress):
    result_dict = {}  # результирующий словарь
    RE_EMAIL = re.compile(r'^([\w\.]+@)+([\w-]+)+(\.+[\w-]{2,4})$')
    if RE_EMAIL.match(email_adress) is not None:
        email_split = email_adress.split('@')
        result_dict['username'] = email_split[0]
        result_dict['domain'] = email_split[1]
        print(result_dict)
    else:
        raise ValueError('not found')


email_parse('fordfocus2goga@gmail.com')
email_parse('someone@gmail.com')
email_parse('fordfocus2goga@gmailcom')  # здесь выведет ValueError

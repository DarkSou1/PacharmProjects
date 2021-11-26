def num_translate(number):
    translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
                      'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
                      'nine': 'девять', 'ten': 'десять'
                      }
    if number in translate_dict:
        print(translate_dict[number])
    else:
        return None


num_translate('one')
num_translate('two')
num_translate('three')
num_translate('four')
num_translate('eleven')

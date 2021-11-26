

def thesaurus(*args):
    worker = {}
    for name in args:
        f_letter = name[0]
        worker.setdefault(f_letter, [])
        worker[f_letter].append(name)
    return worker


def thesaurus_adv(*args):
    worker = {}
    for i in args:
        last_name = i.split()[-1]
        worker.setdefault(last_name[0], [])
        worker[last_name[0]].append(i)

    result_dict = {}
    for key, value in worker.items():
        result_dict[key] = thesaurus(*value)
    return result_dict

print(thesaurus_adv('Мария Иванова', 'Пётр Ильин',
              'Иван Васильев', 'Илья Кудряшов',
              'Мирон Васечкин', 'Игорь Пупкин'))
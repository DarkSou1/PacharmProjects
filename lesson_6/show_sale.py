import csv


def read_sales(*argv):
    with open('bakery.csv', 'r', encoding='utf_8', newline='') as f:
        count_num = int(argv[0][1])
        for line, sale in enumerate(f):
            if line >= count_num - 1:
                print(sale)


def all_read():
    with open('bakery.csv', 'r', encoding='utf_8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def range_read(args):
    with open('bakery.csv', 'r', encoding='utf_8', newline='') as f:
        min_count = int(args[1])
        max_count = int(args[2])
        for line, sale in enumerate(f):
            if min_count - 1 <= line < max_count:
                print(sale)


def main(arg):
    print(arg)
    if len(arg) == 2:
        read_sales(arg)
    elif len(arg) == 1:
        all_read()
    elif len(arg) == 3:
        range_read(arg)


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))

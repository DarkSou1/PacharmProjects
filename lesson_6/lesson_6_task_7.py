import csv


def change_sale(*args):
    with open('bakery.csv', 'r+', encoding="utf_8", newline='') as f:
        for line, sale in enumerate(f):
            if line == 0:
                print(sale)

change_sale()
"""
def main(args):
    print(args)
    change_sale(args)


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
"""
from utils import currensy_rates


def main(argv):
    res = currensy_rates(argv)


if __name__ == '__main__':
    import sys

    exit(main(sys.argv[1]))

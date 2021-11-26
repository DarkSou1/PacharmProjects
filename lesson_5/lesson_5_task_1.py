#1)Написать генератор нечётных чисел от 1 до n(включительно), используя ключевое слово yield, например:
def odd_nums(num):
    for i in range(1, num + 1, 2):
        yield i


odd_num_15 = odd_nums(15)
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))
print(next(odd_num_15))

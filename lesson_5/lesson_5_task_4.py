# Представлен список чисел.Необходимо вывести те его элементы, значения которых больше предыдущего, например:
from time import perf_counter
numbers = [300, 2, 12, 44, 1, 1, 4,
           10, 7, 1, 78, 123, 55
           ]
start = perf_counter()
result = [numbers[i + 1] for i in range(len(numbers)-1) if numbers[i] < numbers[i + 1]]
finish = perf_counter()
time_f = finish - start
print(result, time_f, type(result))
start = perf_counter()
result = (numbers[i + 1] for i in range(len(numbers)-1) if numbers[i] < numbers[i + 1])
finish = perf_counter()
time_f = finish - start
print(*result, time_f, type(result))
# Представлен список чисел.
# Определить элементы списка,
# не имеющие повторений.
# Сформировать из этих элементов список с
# сохранением порядка их следования
# в исходном списке, например:
src = [2, 2, 2, 4, 7, 23, 14,
       44, 3, 2, 10, 7, 4, 11
       ]
result = (i for i in src if src.count(i) == 1)
print(*result)
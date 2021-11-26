#Рещить первую задачу, только без ключевого слова yield
x = (x for x in range(1, 15, 2))
print(next(x), type(x))
print(next(x), type(x))
print(next(x), type(x))

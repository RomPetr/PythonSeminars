"""
Задача 1: В списке хранятся числа. Нужно выбрать только четные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
"""
#--------------------------------------
# работа функции MAP
'''list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)'''
#--------------------------------------
# Задача 2: С клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

'''data = '15 150 45 67 3 18 97'
print(data)
#data = data.split()
#print(data)
data = list(map(int, data.split()))
print(data)'''

# работа функции FILTER
'''data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)'''

# В итоге Задача 1 преобразуется в следующий вид:
'''data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x**2), res))
print(res)'''
#--------------------------------------
# Функция ZIP
'''users = ['user1', 'user2', 'user3', 'user4']
ids = [1, 2, 3, 4]
data = list(zip(users, ids)) #Создает кортежи из элементов обоих (нескольких) списков
print(data)'''
#--------------------------------------
# Функция ENUMERATE
# Применяется к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных
'''data = list(enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго']))
print(data)'''


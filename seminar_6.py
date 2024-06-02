from functools import reduce
"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод:             Вывод:
7                 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1  (каждое число вводится с новой строки)

lst_1 = [3, 1, 3, 4, 2, 4, 12]
lst_2 = [4, 15, 43, 1, 15, 1]
# lst = list(map(int, input("Введите элементы через пробел ").split()))

# традиционный итератор с функцией append
res = []

for elem in lst_1:
    if elem not in lst_2:
        res.append(elem)
print(res)

# list comprehension
print([elem for elem in lst_1 if elem not in lst_2])
# lambda function
print(*list(filter(lambda x: x not in lst_2, lst_1)))

#--------------------------------------
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:        Ввод:
5            5
1 2 3 4 5    1 5 1 5 1
Вывод:       Вывод:
0            2

n = [1, 5, 1, 5, 1]
count = 0
for i in range(1, len(n) - 1):
    if n[i] > n[i-1] and n[i] > n[i+1]:
        count += 1
print(count)

#--------------------------------------
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных строках.
Ввод:       Вывод:
1 2 3 2 3   2

# Решение студента
my_list = [1, 2, 3, 2, 3, 3, 3, 3]
temp_dict = {}
count_pairs = 0
for item in my_list:
    if item not in temp_dict.keys():
        temp_dict[item] = 1
    else:
        count = temp_dict[item]
        temp_dict[item] = count + 1
for item in temp_dict.keys():
    if temp_dict[item] >= 2:
        count_pairs += 1
print(count_pairs)

# Решение в группе
nums = [1, 2, 3, 2, 3, 3, 3, 3]
my_set = set(nums)
res = []
for item in my_set:
    res.append(nums.count(item) // 2)
print(sum(res))
# List comprehension (Лист компрехэншен)
print(sum([nums.count(item) // 2 for item in set(nums)]))
"""

# Вставка про MAP, FILTER, REDUCE
# map
# Возьмем список. Умножим элементы на 2 и вычтем 10
def process_number(num):
    squared = num ** 2
    subtracted = squared - 10
    return subtracted

numbers = [1, 2, 3, 4, 5]
new_numbers = list(map(process_number, numbers))

print(new_numbers)
#--------------------------------------

# filter
# Возьмем из списка элементы больше 5
def greater_than_five(num):
    return num > 5

numbers = [2, 7, 1, 8, 4, 5]
result = list(filter(greater_than_five, numbers))

print(*result)
#--------------------------------------

# reduce
# Сложем все элементы списка. Умножем все элементы списка
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers, 0)
print(result)
# 15

result = reduce(multiply, numbers, 1)
print(result)
#--------------------------------------
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

Задача №45. Решение в группах
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 10^5.
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. 
Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую пару не дает).
Ввод:     Вывод:
300       220 284
"""
# Решение в группе
def get_sum(n):
    my_sum = 1
    for el in range(2, n // 2 + 1):
        if n % el == 0:
            my_sum += el
    return my_sum

def get_friendlies(k):
    lst = []
    for n in range(1, k + 1):
        if n not in lst:
            m = get_sum(n)
            if n == get_sum(m) and n != m:
                lst.append(n)
                lst.append(m)
    return lst

print(get_friendlies(10000))

# Решение Азера
def sum_of_divisors(n):
    divisors_sum = 1
    for i in range(2, n // 2 + 1): # Если число больше половины, то оно по дефолту не делитель
        if n % i == 0:
            divisors_sum += 1
    return divisors_sum

k = 10000

# Начинаем с 220, т.к. минимальная пара дружественных чисел начинается с 220
for i in range(220, k + 1):
    j = sum_of_divisors(i)
    # Условие i != j для того, чтобы исключить равные между собой значения
    # Условие i < j для того, чтобы исключить одинаковые пары
    # Условие j <= k для того, чтобы не противоречить условиям задачи
    if sum_of_divisors(j) == i and i != j and i < j and j <= k:
        print(f"{i} {j}")

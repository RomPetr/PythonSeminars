"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6

# first variant
list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(list_1)))

# second variant
list_2 = []
for el in list_1:
    if el not in list_2:
        list_2.append(el)
print(len(list_2))
#--------------------------------------
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]

array = [1, 2, 3, 4, 5]
k = 3
# print(array[k-1:] + array[:k-1])
for _ in range(k):
    last = array.pop()
    array.insert(0, last)
print(array)
"""
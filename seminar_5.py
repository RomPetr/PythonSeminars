"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21 (0 1 1 2 3 5 8 13 21)
Задание необходимо решать через рекурсию

# Решение без рекурсии
n = 7
fibo_p, fibo_n = 0, 1
for _ in range(n):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(fibo_n)

# Решение с рекурсией
def func(n, fibo_p=0, fibo_n=1):
    if n == 0:
        return fibo_n
    return func(n-1, fibo_n, fibo_p + fibo_n)
print(func(n))

#--------------------------------------
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

scores = [1, 3, 3, 3, 4]

def change_scores(scores, index=0, max_score=max(scores), min_score=min(scores)):
    if index < len(scores):
        if scores[index] == max_score:
            scores[index] = min_score
        change_scores(scores, index + 1)
    return scores
print(*change_scores(scores))

#--------------------------------------
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""
# Без рекурсии
def func_1(n):
    for el in range(2, n):
        if n % el == 0:
            return "no"
    return "yes"
print(func_1(5))

def func_2(n, el=2):
    if el < n:
        if n % el == 0:
            return "no"
        return func_2(n, el+1)
    return "yes"
print(func_2(6))
"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()

data = "a a a b c a a d c d d".split()
res = {}
for item in data:
    if item not in res:
        print(item, end=" ")
    else:
        print(f"{item}_{res[item]}", end=" ")
    res[item] = res.get(item, 0) + 1

#--------------------------------------

Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
"""
# Короткое решение
data = """She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells""".lower().split()
print(len(list(set(data))))

# Решение через цикл
input_str = """She sells sea shells on the sea shore The shells
            that she sells are sea shells I'm sure.So if she sells sea
            shells on the sea shore I'm sure that the shells are sea shore shells""".split()
temp = set()
count = 0
for item in input_str:
    count += 1
    temp = set(item.lower())
print(len(temp))
print(count)
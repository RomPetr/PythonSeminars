"""
FINAL_TASK
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

"""

# import pandas as pd
from pandas import DataFrame, unique
import random

# Генерация исходного списка lst
lst = ['robot'] * 10  # заполняем список элементами в кол-ве 10 шт
lst += ['human'] * 10  # добавляем в список еще 10 элементов
""" проверка заполнености списка """
# print(lst)

random.shuffle(lst)  # перемешиваем элементы списока на месте в случайном порядке
""" выводим результат применения метода .shuffle() """
print("\nShuffled list:")
print(lst)

data = DataFrame({'whoAmI': lst})  # создаем pandas DataFrame

# Вывод исходного DataFrame
print("\nInitial DataFrame:")
print(data.head(len(lst)))

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

"""Проверка полученных уникальных значений """
print("\nUnique values:")
print(f"{unique_values}\n")

# Создаем DataFrame для one-hot кодирования
one_hot_df = DataFrame()

# Заполняем one-hot DataFrame
for value in unique_values:
    one_hot_df[value] = (data['whoAmI'] == value).astype(int)  # метод .astype(int) преобразует объекты в тип int64
    """ проверка """
    # print(one_hot_df[value])

# Вывод one-hot DataFrame
print("\nOne-hot DataFrame:")
print(one_hot_df.head(len(lst)))

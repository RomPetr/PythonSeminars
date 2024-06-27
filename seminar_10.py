"""from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

data = read_csv("california_housing_test.csv")


# Задача №1. Решение в группах
# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
#--------------------------------------

#1. Изобразите отношение households к population с помощью точечного графика

def first():
    scatterplot(data=data, x='households', y='population')
    show()

# first()

#2. Визуализировать longitude по отношения к median_house_value, используя линейный график

def second():
    relplot(data=data, x='longitude', y='median_house_value', kind='line')
    show()

# second()

# 3. Представить гистограмму по housing_median_age

def third():
    histplot(data=data, x='housing_median_age')
    show()

# third()

# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age

def fourth():
    histplot(data=data, x='median_house_value', hue='housing_median_age')
    show()

fourth()
"""

"""
Задача №2. Решение в группах

Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap (тепловая диаграмма)
● Использовать 2-3 гистограммы
Чтобы подключить датасет с пингвинами, воспользуйтесь данным скриптом:
penguins = sns.load_dataset("penguins")
pe
#--------------------------------------

from seaborn import load_dataset, scatterplot, PairGrid, heatmap
from matplotlib.pyplot import show
from matplotlib import pyplot

penguins = load_dataset('penguins')

# 1. Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика

def f_1():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g")
    show()

# f_1()

# 2. Применить доп измерение в точечных графиках, используя аргументы hue, size, stile

def f_2():
    scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g", hue="sex", size="island", style="island")
    show()

# f_2()

#3. Использовать PairGrid с типом графика на ваш выбор

def f_3():
    x_vars = ["body_mass_g", "bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
    y_vars = ['sex']
    pg = PairGrid(data=penguins, x_vars=x_vars, y_vars=y_vars, hue='species')
    pg.map(scatterplot)
    show()

# f_3()

# 4. Изобразить Heatmap (тепловая диаграмма)

def f_4():
    data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
    heatmap(data)
    pyplot.xlabel('Остров', size=14)
    pyplot.ylabel('Вид пингвинов', size=14)
    show()

#f_4()

# 5. Использовать 2-3 гистограммы

def f_5():
    penguins['bill_depth_mm'].hist(bins=8)
    show()

f_5()

"""

"""
Задача №3. Решение в группах
Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.

high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
#--------------------------------------


from pandas import read_csv

penguins = read_csv('penguins.csv')

penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'
penguins.loc[(penguins['bill_length_mm'] > 35 & penguins['bill_length_mm'] < 42), 'height_group'] = 'middle'
penguins.loc[penguins['bill_length_mm'] > 34, 'height_group'] = 'high'
penguins.to_csv('penguins.csv', index=False)
"""

"""
Задача №4. Решение в группах

Изобразить гистограмму по flipper_length_mm
с оттенком height_group. Сделать анализ


from seaborn import histplot
from pandas import read_csv
from matplotlib.pyplot import show

penguins = read_csv('penguins.csv')

histplot(penguins, x='flipper_length_mm', hue='height_group')
show()
"""

"""
HW 1
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


"""

import pandas as pd
import random

# Генерация исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Вывод исходного DataFrame
print("Original DataFrame:")
print(data.head())

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание DataFrame для one-hot кодирования
one_hot_df = pd.DataFrame()

"""
# Заполнение one-hot DataFrame
for value in unique_values:
    one_hot_df[value] = (data['whoAmI'] == value).astype(int)

# Вывод one-hot DataFrame
print("\nOne-hot DataFrame:")
print(one_hot_df.head())
"""
# Для кодировки категориальных данных можно использовать метод pandas get_dummies
# print(pd.get_dummies(data['Type 1']))
from pandas import read_csv
from seaborn import scatterplot, relplot, histplot
from matplotlib.pyplot import show
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

data = read_csv("california_housing_test.csv")

"""
# Задача №1. Решение в группах
# 1. Изобразите отношение households к population с помощью точечного графика
# 2. Визуализировать longitude по отношения к median_house_value, используя линейный график
# 3. Представить гистограмму по housing_median_age
# 4. Изобразить гистограмму по median_house_value с оттенком housing_median_age
"""

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
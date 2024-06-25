from pandas import read_csv
from seaborn import scatterplot
from matplotlib.pyplot import show

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

first()
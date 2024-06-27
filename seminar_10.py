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
Задача № 3. Решение в группах
Создать новый столбец в таблице с пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

"""


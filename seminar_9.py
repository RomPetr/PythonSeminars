"""
from pandas import read_csv
data = read_csv('california_housing_test.csv')
"""

"""
Задача №57. Решение в группах
Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы


#1 print (data)
#2 print(data.shape)
#3 print(data.dtypes)
# print(data.info())
print(data.describe())
"""

"""
Следующая задача №2
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000


# 1. Проверить есть ли в файле пустые значения
# print(data.isnull())
# print(data.isnull().sum())

# 2. Показать median_house_value где median_income < 2
print(data[data['median_income'] < 2]['median_house_value'])
print(data[data['median_income'] < 2]['median_house_value'].shape) # сколько всего таких строк

# 3. Показать данные в первых 2 столбцах
print(data[['longitude', 'latitude']]) # заранее знаем столбцы
print(data.iloc[:, :2]) # не знаем столбцы 

# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)])
"""

"""
Следующая задача №3
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value


# 1. Определить какое максимальное и минимальное значение median_house_value
print(data['median_house_value'].max(), data['median_house_value'].min())

# 2. Показать максимальное median_house_value, где median_income = 3.1250
print(data[data['median_income'] == 3.1250]['median_house_value'].max())

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
print(data[data['median_house_value'] == data['median_house_value'].min()]['population'].max())
"""

# HW 1
"""
Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 
(population) и сохранить ее в переменную avg. Используйте модуль pandas.


import pandas as pd

# Загрузка данных из файла
df = pd.read_csv('california_housing_test.csv')

filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]
avg = filtered_df['median_house_value'].mean()
print(avg)
"""

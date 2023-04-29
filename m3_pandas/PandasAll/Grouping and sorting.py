'''ГРУППИРОВКА И СОРТИРОВКА'''
import pandas as pd
import numpy as np

df = pd.read_csv('GoogleApps.csv')
'''Все значения Size сортируем ПО УБЫВАНИЮ (ascending=False), затем выводим их с названием приложения'''
size_sorted = df.sort_values('Size',ascending=False)[['App', 'Size']]
print(size_sorted)

print(100*'=')

print(df.groupby(['Size'])['Price'].mean()) #Вывести среднюю цену Price для разных размеров приложений Size

print(100*'*')

print(df.groupby(['Size'])['Price'].agg(['mean', 'min', 'max'])) #agg() - агрегатор. Применяет несколько функций

print(100*'#')

# Сгруппировать данные по категории ('Category') и целевой аудитории ('Content Rating'),
# посчитать максимальное количество отзывов ('Reviews') в каждой группе.
# Сравнить результаты для категорий 'EDUCATION', 'FAMILY' и 'GAME':
temp = df.pivot_table(index='Content Rating', columns='Category', values='Reviews', aggfunc='max')
print(temp[['EDUCATION', 'FAMILY', 'GAME']])
#pivot_table() - создание сводной таблицы
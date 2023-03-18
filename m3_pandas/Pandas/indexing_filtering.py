'''ИНДЕКСАЦИЯ И ФИЛЬТРАЦИЯ'''

import pandas as pd
import numpy as np


df = pd.DataFrame({
'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine','Kazakhstan'],
'population': [17.04, 143.5, 9.5, 45.5, 232.12],
'square': [2724902, 17125191, 207600, 603628, 35445]
}, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])

print(df["country"]) #df.country - получить значение только определённого столбца

print('\n', '*' * 5, '\n')

print(df[["country", "square"]]) #cписок с названиями столбцов, которые хотим посмотреть

print('\n', '*' * 5, '\n')

'''Доступ к строкам по индексу возможен несколькими способами:

 *   .loc - (работа с метками) используется для доступа к значению по строковой метке (индексу) (by row & column index label)
 *   .iloc - (работа с числ. знач.) используется для доступа по числовому значению (начиная от 0) (by row & column number)
 
 .at и .iat анаологичны, но можут получать только одно значение за раз
 
 ix - устарел'''

print(df.loc['KZ']) # at

print('\n', '#' * 5, '\n')

print(df.loc[['KZ'], ['square']]) # строка с меткой KZ, столбец с меткой square

print('\n', '#' * 5, '\n')

print(df.iloc[1]) # 1 строка, все стобцы , iat

print('\n', '$' * 5, '\n')

print(df.iloc[1, 1]) # 1 строка и 1 столбец

print('\n', '%' * 5, '\n')

'''СРЕЗЫ'''

print(df.iloc[1, 1:3]) # строка с индексом 1, все столбцы от 1 до 3 (не включительно)

print('\n', '*' * 5, '\n')

print(df.iloc[1:3, 1:3]) # c 1 по 3 строки и c 1 по 3 столбец

print('\n', '*' * 5, '\n')

print(df.loc[['KZ', 'RU'], 'square']) # по индексу и интересующим колонкам

print('\n', '*' * 5, '\n')

print(df.loc['RU':'UA', :]) #СРЕЗЫ РАБОТАЮТ И НА МЕТКАХ - все строки от метки RU до UA со всеми столбцами

print('\n', '#' * 50, '\n')

'''Фильтрация: получить все страны с населением больше 30:'''

print(df[df.population > 30], '\n')

print('*' * 10, '\n')

print(df[df.population > 30][['country', 'square']]) #вывести столбцы только country и square (комбинирование условий)

''' вывод:
       country    square
RU      Russia  17125191
UA     Ukraine    603628
KZ  Kazakhstan     35445
'''

print('\n', '*' * 10, '\n')

'''создаём столбец Density (плотность населения) так, чтобы он был равен столбцу population / square * 1000000'''
df['Density'] = df['population'] / df['square'] * 1000000
print(df, '\n')

print('\n', '-' * 10, '\n')

'''Стандартные операции: суммы, ср. значения, макс. значения по всем'''
print(df.sum(), '\n\n', df.mean(), '\n\n', df.max())

print('\n', '+' * 10, '\n')

print(df['square'].mean()) #ср. знач. по столбцу "площадь"

print('\n', '=' * 10, '\n')

'''УДАЛЕНИЕ СТОЛБЦА'''
print(df.drop(['square'], axis=1))
#axis=0 - направление строк, 1 - столбец


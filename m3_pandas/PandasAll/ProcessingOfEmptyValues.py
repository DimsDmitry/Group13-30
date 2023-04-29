'''ОБРАБОТКА ПУСТЫХ ЗНАЧЕНИЙ'''

import pandas as pd
import numpy as np


df = pd.DataFrame({
                'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine','Kazakhstan'],
                'population': [17.04, 143.5, 9.5, 45.5, 232.12],
                'square': [2724902, 17125191, 207600, 603628, 35445]
                }, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])
print(df)


df = pd.read_csv('GoogleApps.csv')
print(df.head(10))

print(100*'#')

'''Для определения NaNзначений панды использует либо .isna()или .isnull(). 
Эти NaN значения унаследованы от того , что панды построены на вершине NumPy, в то время как имена двух функций
происходят из DataFrames АиРа, чья структура и функциональность панд пытались имитировать.
NaN из numpy, null из БД. isna() для NaN, isnull() для null
'''
print(df.isna()[1000:]) #узнать все NaN значения от 1000 строки и ниже. False - значит строка не пустая

print(100*'#')

print(df.iloc[10])  #Метод iloc() - вывести всю строку под определённым индексом. Здесь - 1000

print(100*'=')

print(len(df))

df2 = df.dropna() #axis=1 выкидываем все стобцы с null values, axis=0 - строки

print(len(df2)) #было и осталось 7352, пустых столбцов не было

df = df.fillna(df['Size'].mean()) #это значение будет подставлено в пропуски в Size. В данном случае значение -
#средний возраст из всех строк
print(df.iloc[1000])



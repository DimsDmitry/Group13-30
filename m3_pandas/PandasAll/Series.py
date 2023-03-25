import pandas as pd
import numpy as np


data1 = ['PandasAll', 'Pygame', 'Numpy', 11]
print(pd.Series(data1, index=['первый', 'второй', 'третий', 'пятый']))

# Выводит индексы и строки

'''series - одномерный массив с метками. Структура данных, содержащая элементы и их индексы.
Можно создать его из списка, затем передав в series,
или создать сразу передав в метод:'''

print('#' * 100)

data2 = pd.Series(['PandasAll', 'PyQt5'])
print(data2)

'''По умолчанию индексы от нуля, можно задать свои:'''

data3 = pd.Series([3, 4, 'kivy', 2.34, [1, 2, 3], {1: 2, '1': ' 2'}], index=['один', 'два', 'три', 2, 1.22, [10, 5]])
print(data3)

print('#' * 10)

'''Все индексы внутри одной Series принадлежат к одному типу данных.
Все данные в одной Series принадлежат к одному типу данных, если передать вразнобой - будет object.
Тип данных индексов и данных в одной Series могут как различаться, так и совпадать.
'''


'''создание series можно упростить, используя словари, где К-З - это индекс-данные'''

n = {'a': 1, 'b': 2, 'c': 3}
print(pd.Series(n))

print('0' * 10)

'''series можно заполнять рандомно'''
s = pd.Series(np.random.randn(6), index=['p', 'q', 'r', 'n', 't', 'v'])
print(s)

'''методы полностью повторяют NDArray, из NumPy'''
print(s.dtype)  # тип данных
print(s.shape)  # форма (6 элементов одной строкой)
print(s.ndim)  # размерность (одномерный массив)
print(s.size)  # кол-во элементов

'''превратить Series в Array numpy - массив'''
s.to_numpy()
print(s)

'''Индексы и выборка'''
print(s, '\n')

print(s[0], '\n')

print(s[1:5], '\n')

print(s[s > 0], '\n')
## сложные условия:
print(s[(s > 0) & (s < 1)], '\n')

print(s['t'], '\n')

print(s[['r', 't']])

'''синус, косинус и т.д.'''
print(np.sin(s), '\n')
print(np.abs(s), '\n')
print(np.tan(s), '\n')

print('*' * 100)

'''Добавление и удаление'''
s['algo'] = 1000
print(s)
s.drop(labels=['p', 'algo']) # можно обращаться по labels, index, axis (оси) и т. д.

print(s.sum(), '\n') #сумма
print(s.mean(), '\n') #сред
print(s.max()) #макс

print('#' * 100)

'''Операции - сложение, умножение и т.д.'''
print(s + s) #сложение элементов
print(s * s)
print(s ** 2)

print(s.astype(np.int16)) #приводит все элементы к указанному типу

print('-' * 100)
file = pd.read_csv('GoogleApps.csv', nrows=1) #читаем файл, 1 строку (не считая 1 с заголовками)
print(file)

'''Другие возможные варианты файлов:'''
# pd.read_excel('file.xlsx')
# pd.to_excel('dir/myDataFrame.xlsx', sheet_name='Sheet1')
# df.to_json(filename)
#
# xlsx = pd.ExcelFile('file.xls')
# df = pd.read_excel(xlsx, 'Sheet1')
# pd.read_json(json_string)
# pd.read_html(url)
# pd.read_clipboard()

''' Возможно читать и сохранять данные даже в SQL-таблице:

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
pd.read_sql("SELECT * FROM my_table;", engine)
pd.read_sql_table('my_table', engine)
pd.read_sql_query("SELECT * FROM my_table;", engine)

pd.to_sql('myDf', engine)'''
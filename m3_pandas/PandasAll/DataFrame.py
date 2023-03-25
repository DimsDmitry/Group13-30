import pandas as pd
import numpy as np



'''DataFrame - структура данных, содержащая наборы элементов и их индексы.
Создание так же из списка, как и в series'''
data = [[4, 7, 10], [5, 8, 11], [6, 9, 12]]
df = pd.DataFrame(data)
print(df)


print('*' * 100)
'''именование индексов и столбцов (по умолчанию они идут от 0)'''
df = pd.DataFrame(data, index=['a', 'b', 'c'], columns=['X', 'Y', 'Z'])
print(df)

'''создание DF из словарей. Ключи - столбцы, метки строк (индексы) от 0 также, если их не задать.'''

data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df)

print('-' * 10)

df = pd.DataFrame(data, index=[2, 4, 1, 9])
print(df)

print('=' * 100)

'''разделение записей, например через запятую. Header=None - автоматическая нумерация столбцов'''
df = pd.read_csv('GoogleApps.csv', sep=',', header=None, nrows=10)
print(df)

print('=' * 100)

n = 7
print(df.head(n)) #показать первые n столбцов. По умолчанию = 5
print('/' * 100 + '\n')
print(df.tail(n)) #показать n строк с конца, аналогично 5
print('/' * 100 + '\n')
print(df.info()) #вся статистика по столбцам: память, количество, тип данных и т.д.

print('=' * 100)

print(df.describe()) #статистика по столбцу - уникальные элем-ты и т.д.

print(df.shape, '\n') #форма - (10, 12)
print('=' * 10)
print(df.ndim, '\n') #размерность объекта - 2мерный массив
print('=' * 10)
print(df.size, '\n') #кол-во элем
print('=' * 10)
print(df.index,'  ', df.columns, '\n')
print('=' * 10)
print(df.count()) #Number of non-NA values

print('\n', '*' * 10, '\n')

print(df.value_counts()) #подсчитывает количество уникальных значений признака в столбце.
# Метод возвращает объект Series, содержащий уникальные значения признаков
# и количество строк в DataFrame с каждым значением.

print('\n', '#' * 100, '\n')

df = pd.read_csv('GoogleApps.csv', sep=',', nrows=10)
print(df["App"].value_counts(1))

print('\n', '*' * 10, '\n')

'''date_range() Возвращает диапазон равномерно расположенных временных точек (где разница между любыми двумя соседними точками
 определяется заданной частотой), так что все они удовлетворяют start <[=] x <[=] end, где первая и последняя являются,
соответственно, первой и последней временными точкамив том диапазоне, который находится на границе'''
df.index = pd.date_range('1900/1/30', periods=df.shape[0])
'''в качестве индекса назначаем дату с 1900/1/30' и с увеличением на 1 день'''
print(df)

print('\n', '*' * 10, '\n')

print(df['Category'].nunique()) # сколько значений

print('\n', '$' * 10, '\n')

print(df['App'].unique()) # уникальные значения

print('\n', '^' * 10, '\n')

df = pd.DataFrame({
                'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine','Kazakhstan'],
                'population': [17.04, 143.5, 9.5, 45.5, 232.12],
                'square': [2724902, 17125191, 207600, 603628, 35445]
                }, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])
print(df)

print('\n', '=' * 5, '\n')

print(df["country"].nunique(), ' ', df["country"].unique())

print('\n', '=' * 5, '\n')

print(df["country"].value_counts()) #кол-во значений

print('\n', '*' * 5, '\n')

print(df['country'].apply(lambda x: x.upper())) # применяет функцию для выбранных столбцов или всех
#все страны сдали с верхним индексом

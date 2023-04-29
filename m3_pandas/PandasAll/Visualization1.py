'''ВИЗУАЛИЗАЦИЯ. Для работы требуется установить библиотеку matplotlib'''
import pandas as pd
import matplotlib.pyplot as plt

'''Метод plot() Используется для построения диаграмм на основе 
количественных данных. 
Применяется как к объектам Series, так и к DataFrame.
show() - показать'''


s = pd.Series(data=[10, 5, 15, 20, 10], index=[1, 2, 3, 4, 5])
s.plot()
plt.show()


'''Метод plot() может строить диаграммы разных видов. Вид диаграммы можно задать 
с помощью параметра kind. Он принимает значения:
'hist' - гистограмма
'box' - ящик с усами
'scatter' - диаграма рассеивания
'pie' - круговая диаграмма
'bar' - вертикальная столбчатая диаграмма
'barh' - горизонтальная столбчатая диаграмма
'line' - линейный график
'''


df = pd.read_csv('GoogleApps.csv')
df['Size'].plot(kind='hist')
plt.show()

# Изменить количество столбцов:

df['Size'].plot(kind='hist', bins=5)
plt.show()

df[df['Type'] == 'Paid']['Price'].plot(kind='box')
plt.show()

df.plot(x='Rating', y='Installs', kind='scatter')
plt.show()

# круговая диаграмма
df['Content Rating'].value_counts().plot(kind='pie')
plt.show()
df['Category'].value_counts().plot(kind='pie')
plt.show()

# столбчатая диаграмма
df['Category'].value_counts().plot(kind='bar')
plt.show()

'''Параметр figsize позволяет задать ширину и высоту диаграммы.
Если параметр не указан, то размер по умолчанию (6.4, 4.8).
grid - сетка'''

df['Category'].value_counts().plot(kind='barh', figsize=(8, 5), grid=True)
plt.show()
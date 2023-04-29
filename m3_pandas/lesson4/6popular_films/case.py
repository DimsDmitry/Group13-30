# место для твоего кода
import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv')

print(df.info())

print('*' * 100)

print(df[df['Rating'] >= 8.5].value_counts())


'''Вывод 1 - фильмы с жанром "драма" наиболее популярны
Вывод 2 - популярнее всего фильмы Кристофера Нолана'''

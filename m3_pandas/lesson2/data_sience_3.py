import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
print(df['Category'].value_counts())

# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
count_category = df['Content Rating'].value_counts()
print('Соотношение:', round(count_category['Teen'] / count_category['Everyone 10+'], 2))

# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений?
# Ответ запиши с точностью до сотых.
temp = df.groupby(by='Type')['Rating'].mean()
print(temp['Paid'])

# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
print(round(temp['Paid'] - temp['Free'], 2))

print('#' * 100, '\n')
# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
minus = df.groupby(by='Category')['Size'].agg(['min', 'max'])
print(round(minus, 2))

print(10 * '-')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
result = df[df['Rating'] > 4.5]['Category'].value_counts()
print(result['FINANCE'])

print(10 * '=')

# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
result = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(result['Free'] / result['Paid'])


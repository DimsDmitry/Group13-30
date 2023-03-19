import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
print(df[df['Type'] == 'Paid']['Price'].min())

print('*' * 100, '\n')
# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())


# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?


# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?


# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?


# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?

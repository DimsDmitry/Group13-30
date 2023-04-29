'''ОБЪЕДИНЕНИЕ И КОМБИНАЦИИ'''
import pandas as pd
import numpy as np

df = pd.read_csv('GoogleApps.csv')
# добавляет строки df1 в конец df2
df = df.append(df)

# добавляет столбцы  df1 в конец df2
df = pd.concat([df, df], axis=1)

# получаем датафрейм, который добавился сам в себя и увеличился в 2 раза:
print(df)

df.join(df, on='PassengerID',how='inner', lsuffix='_left', rsuffix='_right')
# SQL-style - объединяет столбцы df1 и df2 по виду связывания (join): 'left', 'right', 'outer', 'inner'

# pd.merge(df1, df2,how='left', on='x1')
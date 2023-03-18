'''ОБРАБОТКА ПУСТЫХ ЗНАЧЕНИЙ'''

import pandas as pd
import numpy as np


df = pd.DataFrame({
                'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine','Kazakhstan'],
                'population': [17.04, 143.5, 9.5, 45.5, 232.12],
                'square': [2724902, 17125191, 207600, 603628, 35445]
                }, index=['KZ', 'RU', 'BY', 'UA', 'KZ'])


df = pd.read_csv('GoogleApps.csv')
print(df.head(10))
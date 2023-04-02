import pandas as pd
import numpy as np


df = pd.read_csv('GoogleApps.csv', sep=',', nrows=10)
print(df.groupby(by='Content Rating')['Size'].mean())

print('*' * 100)

print(df.groupby(by='Content Rating')['Size'].agg(['min', 'max']))
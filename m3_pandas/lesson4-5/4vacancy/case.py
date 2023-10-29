#место для твоего кода
import pandas as pd
df = pd.read_csv('DataAnalyst.csv')
print(df[pd.isnull(df['Type'])].iloc[0])
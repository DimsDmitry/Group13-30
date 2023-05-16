import pandas as pd
import matplotlib.pyplot as plt


def set_lit(lit):
    try:
        lit = str(lit[:-1])
        lit = lit.replace(',', '')
        lit = lit.replace("'", '')
        return int(lit)
    except:
        return 0


def set_gdp(gdp):
    try:
        return int(gdp)
    except:
        return 0


df = pd.read_csv('countries of the world.csv')


df['Literacy (%)'] = df['Literacy (%)'].apply(set_lit)
df['GDP ($ per capita)'] = df['GDP ($ per capita)'].apply(set_gdp)

df['Literacy (%)'].value_counts().plot(kind='barh', grid=True)
plt.show()

print(df['GDP ($ per capita)'].value_counts())

df.plot(x='Region', y='Literacy (%)', kind='hist')
plt.show()


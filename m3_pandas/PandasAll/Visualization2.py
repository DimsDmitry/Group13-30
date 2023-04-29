import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('GoogleApps.csv')
d = df.pivot_table(index='Content Rating', columns='Type',
                   values='Installs', aggfunc='mean')

# subplots - постройка графиков друг под другом
d.plot(kind='barh', subplots=True)
plt.show()

# совмещение графиков:
d.plot(kind='barh', grid=True)
plt.show()
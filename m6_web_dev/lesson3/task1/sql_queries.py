import sqlite3
conn = sqlite3.connect('Artistc.db')
cursor = conn.cursor()

# Вопрос 1. Информация о скольких художниках представлена в базе данных? 
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Художников в базе:', len(data))

# Вопрос 2. Сколько женщин (Female) в базе?
cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
data = cursor.fetchall()
print('Женщин в базе:', len(data))

# Вопрос 3. Сколько человек в базе данных родились до 1900 года?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print('Родились до 1900 года:', len(data))

# Вопрос 4*. Как зовут самого пожилого художника?
cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900 order by "Birth Year"')
data = cursor.fetchall()
print('Самый старший:', data[0][1])

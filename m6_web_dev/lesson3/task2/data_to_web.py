# -*- coding: utf-8 -*-
""" Программа использует flask и запускает веб-сервер.
При запросе к этому серверу он возвращает текст "Привет, Мир!" """
from flask import Flask
import sqlite3


def index():
    # Устанавливаем соединение с БД, отправляем запрос
    conn = sqlite3.connect('Artistc.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE  "Birth Year" = (?)', [year])
    data = cursor.fetchall()

    # Рассмотрим несколько вариантов при обработке запроса.
    # Вариант 1 - в базе нет данных о художниках, родившихся в указанный год
    if len(data) == 0:
        return f'В базе нет данных о художниках, родившихся в {str(year)} году'
    # Вариант 2 - художник, родившийся в указанный год, только один
    elif len(data) == 1:
        return f'В {str(year)} году родился(-ась) {data[0][0]}'
    # Вариант 3 - художников, родившихся в указанный год, несколько
    else:
        result = f'<h3>Список художников, родившихся в {str(year)} году:</h3><ol>'
        for person in data:
            result += '<li>' + person[0] + '</li>'
        result += '</ol>'
        return result


# Создаём объект веб-приложения:
year = int(input('Введите год рождения художника:'))
app = Flask(__name__)

app.add_url_rule('/', 'index', index)  # создаёт правило для URL

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()

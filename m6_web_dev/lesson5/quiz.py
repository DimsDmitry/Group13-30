from random import randint

from flask import Flask, session
from db_scripts import *


def index():
    max_quiz = 3
    session['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return '<a href="/test">Тест</a>'


def test():
    result = get_question_after(session['last_question'], session['quiz'])
    session['last_question'] = result[0]
    string = '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'
    return string


def result():
    return 'Здесь должен быть результат'


# создаём объект веб-приложения
app = Flask(__name__)
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/result'

# ключ шифрования
app.config['SECRET_KEY'] = 'secret_key'


if __name__ == '__main__':
    app.run()
from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after

quiz = 0
last_question = 0

def index():
   global quiz, last_question
   max_quiz = 3
   # или если ученик написал get_quiz_count(), то можно её импортировать и указать:
   # max_quiz = get_quiz_count[0]
   quiz = randint(1, max_quiz)
   # или если ученик написал get_random_quiz_id(), то можно её импортировать и указать:
   # session['quiz'] = get_random_quiz_id()

   last_question = 0
   return '<a href="/test">Тест</a>'

def test():
   global last_question
   result = get_question_after(last_question, quiz)
   if result is None or len(result) == 0:
           return redirect(url_for('result'))

   else:
       last_question = result[0]
       # если мы научили базу возвращать Row или dict, то надо писать не result[0], а result['id']
       return '<h1>' + str(quiz) + '<br>' + str(result) + '</h1>'

def result():
   return "that's all folks!"


# Создаём объект веб-приложения:
app = Flask(__name__)
app.add_url_rule('/', 'index', index)   # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test) # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result) # создаёт правило для URL '/test'

if __name__ == '__main__':
   # Запускаем веб-серaвер:
   app.run()
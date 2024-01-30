from flask import *
from db_scripts import *

from random import randint


def start_quiz(quiz_id):
    # создаёт нужные значения в словаре session
    session['quiz'] = quiz_id
    session['last_question'] = 0


def end_quiz():
    session.clear()


def quiz_form():
    # получает список викторин из БД, выводит их как выпадающий список
    text1 = '''
    <html><body><h2>Выберите викторину:</h2><form method="post" action="index"><select name="quiz">
    '''
    text2 = '''
    <p><input type="submit" value="Выбрать"></p>
    '''
    text3 = '''</select>''' + text2 + '''</form></body></html>'''
    options = ''' '''
    q_list = get_quizes()
    for id, name in q_list:
        text = ('''<option value="''' + str(id) + '''">''' + str(name) + '''</option>''')
        options = options + text
    return text1 + options + text3


def index():
    # если пришли GET-запросом, выбираем викторины, если POST - запомнить викторину и перейти на вопросы
    if request.method == 'GET':
        # сбрасываем id викторины и показываем форму выбора
        start_quiz(-1)
        return quiz_form()
    else:
        # получаем данные в запросе, используем их
        quest_id = request.form.get('quiz')
        start_quiz(quest_id)
        return redirect(url_for('test'))


def test():
    # возвращает страницу вопроса
    # если пользователь сразу без выбора викторины пошёл на адрес /test:
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        result = get_question_after(session['last_question'], session['quiz'])
        if result is None or len(result) == 0:
            return redirect(url_for('result'))
        else:
            session['last_question'] = result[0]
            string = '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'
            return string


def result():
    end_quiz()
    return 'Это всё!'


# создаём объект веб-приложения
app = Flask(__name__)
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/index', 'index', index, methods=['post', 'get'])
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/result'

# ключ шифрования
app.config['SECRET_KEY'] = 'secret_key'

if __name__ == '__main__':
    app.run()

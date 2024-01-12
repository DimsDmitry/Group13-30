import sqlite3

db_name = 'quiz.sqlite'
conn = None
cursor = None


def open_db():
    # открывает соединение с БД, создаёт объект cursor
    # для выполнения SQL-запросов
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    # закрывает соединение с БД, освобождает курсор
    cursor.close()
    conn.commit()


def do(query):
    # сделать запрос
    cursor.execute(query)
    conn.commit()


def create():
    # создаёт таблицы и связывает их в формате "один ко многим"
    open_db()
    cursor.execute('PRAGMA foreign_keys=on')

    do('''CREATE TABLE IF NOT EXISTS quiz
        (id INTEGER PRIMARY KEY, name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id))''')

    close()


def clear_db():
    # удаляет все таблицы
    open_db()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()


def add_questions():
    # добавляем вопросы в БД
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Чему равно число Пи?', 'Примерно 3.14', '3', '0', 'Ровно 3.14'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Аэростат', 'Кит'),
        ('Сколько секунд в километре?', 'Нисколько', '60', '100', 'Мало'),
        ('Кто автор 3-го закона Ньютона?', 'Ньютон', 'Конфуций', 'Пифагор', 'Архимед'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Левой', 'Правой', 'Кружкой'),
        ('Что не имеет длины, глубины, ширины, высоты, но можно измерить?', 'Время', 'Воздух', 'Вода', 'Глупость')
    ]
    open_db()
    cursor.executemany(
        '''INSERT INTO question (question, answer, wrong1, wrong2 , wrong3) VALUES (?, ?, ?, ?, ?)''',
        questions
    )
    conn.commit()
    close()


def add_quiz():
    quizes = [
        'Своя игра',
        'Кто хочет стать миллионером?',
        'Самый умный'
    ]
    open_db()
    cursor.executemany(
        '''INSERT INTO quiz (name) VALUES (?)''',
        quizes
    )
    conn.commit()
    close()


def show(table):
    # отобразить содержимое конкретной таблицы
    query = 'SELECT * FROM ' + table
    open_db()
    cursor.execute(query)
    print(cursor.fetchall())
    close()


def show_tables():
    # показать содержимое всех таблиц
    show('question')
    show('quiz')
    show('quiz_content')


def add_links():
    # добавляет связь между вопросом и викториной, к которой он относится
    open_db()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = 'INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)'
    answer = input('Добавить связь (y/n)?')
    while answer != 'n':
        quiz_id = int(input('id викторины:'))
        question_id = int(input('id вопроса:'))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input('Добавить связь (y/n)?')
    close()


# def get_question_after(question_id=0, quiz_id=1):
#
#
# def main():
#
#
# if __name__ == "__main__":
#     main()
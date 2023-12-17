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

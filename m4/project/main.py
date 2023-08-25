import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import sklearn

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Открытие CSV файла по пути
df = pd.read_csv('train.csv')
print(df.info())

# Убираем пропуски
df.dropna(inplace = True)
print(df.info())


# данные которые не рассматриваются - их убираем
# life_main, people_main, city, last_seen, occupation_name
df = df.drop(['life_main', 'people_main', 'city', 'last_seen', 'occupation_name'], axis=1)


# Замена текстовых данных числовыми - 
# это нужно сделать, тк модели машинного обучения не работают с текстом (это математические алгоритмы)

# Схема перевода текстовых данных в числовые
    # 1. Смотрим, какие вообще есть данные, чтобы понять, как перевести их в числа:
    # print("bdate -", df.bdate.unique())

    # 2. пишем функцию замены
    # def change_...(row):
        # ...
        # return row

    # 3. применяем функцию замены
    # df = df.apply(change_bdate, axis = 1)


print("bdate -", df.bdate.unique())  
# '23.4.1990', '03.05' ...
def change_bdate(row):
    # с датами работать будем так - берем год и вычитаем его из текущего года, 
#    рез-т переводим в int ('23.4.1990' -> '1990' -> 2023 - 1990 -> 33, заменяем исходную дату на 33)
    bdate = row['bdate'].split('.')
    if len(bdate) == 3:
        row['bdate'] = 2023 - int(bdate[2])
    else:
        row['bdate'] = np.nan
    return row
df = df.apply(change_bdate, axis = 1)
# Заполняем пропуски медианой
df['bdate'] = df['bdate'].fillna(df['bdate'].median())


print("education_form -", df.education_form.unique()) 
# ['Full-time' 'Distance Learning' 'Part-time']
def change_edu_form(row):
    # Замена формы образования кодовым числом
    row = row.replace('Full-time', 2)
    row = row.replace('Distance Learning', 1)
    row = row.replace('Part-time', 0)
    return row
df = df.apply(change_edu_form, axis = 1)


print("education_status -", df.education_status.unique()) 
# ['Student (Specialist)' 'Alumnus (Specialist)' 'PhD' ...
def change_edu_status(row):
    # заменяем уровень образования на числовой код по мере возрастания
    row = row.replace('Undergraduate applicant', 0)
    row = row.replace("Student (Bachelor's)", 1)
    row = row.replace("Alumnus (Bachelor's)", 2)
    row = row.replace('Student (Specialist)', 3)
    row = row.replace('Alumnus (Specialist)', 4)
    row = row.replace("Student (Master's)", 5)
    row = row.replace("Alumnus (Master's)", 6)
    row = row.replace('Candidate of Sciences', 7)
    row = row.replace('PhD', 8)
    return row
df = df.apply(change_edu_status, axis = 1)


print("langs -", df.langs.unique()) 
# ['Русский;English' 'Русский' 'False' 'Русский;Саха тыла']
def change_langs(row):
    # будем брать кол-во известных клиенту языков
    n_langs = 0
    langs = row["langs"]
    if type(langs) is not int:
        if langs[0] != 'False':
            langs = row["langs"].split(';')
            n_langs = len(langs)
        row["langs"] = n_langs
    return row
df = df.apply(change_langs, axis = 1)


print("occupation_type -", df.occupation_type.unique()) 
# ['university' 'work']
def change_occup_type(row):
    # меняем тип занятости на кодовое значение
    row = row.replace('university', 0)
    row = row.replace('work', 1)
    return row
df = df.apply(change_occup_type, axis = 1)


print("career_start -", df.career_start.unique()) 
# '1996', '2004' ...
def change_career_start(row):
    # та же схема что и с датой рождения (текущий год - год начала карьеры)
    start = 0 
    if row['career_start'] != 'False':
        start = 2023 - int(row['career_start'])
    row['career_start'] = start
    return row
df = df.apply(change_career_start, axis = 1)


print("career_end -", df.career_end.unique()) 
# '1996', '2004', 'False' ...
def change_career_end(row):
    # та же схема что и с датой рождения (текущий год - год начала карьеры)
    # 'False' просто меняем на 0, карьера не окончена
    end = 0 
    if row['career_end'] != 'False':
        end = 2023 - int(row['career_end'])
    row['career_end'] = end
    return row
df = df.apply(change_career_end, axis = 1)


print(df.info())


# Тестовый набор данных (для проверки модели)
df_test = pd.read_csv('test.csv')

# Из основного датасета убираем данные, которые будет предсказывать наша модель
df_x = df.drop('result', axis=1)
df.info()

# Сохраняем предсказываемые значения для дальнейшего рассчета ошибки
y = df['result']
x = df_x

# Разбиваем выборку на тестовую и тренировочную (на тренировочной обучаем, на тестовой проверяем)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, stratify = y)

# приводим все данные к единому масштабу, например:
# (возраст был от 18 до 65, стал от 0 до 1)
# (доход был от 15000 до 300000, стал от 0 до 1)
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
# Это нужно, чтобы определенные данные не давали непомерно больший вклад чем остальные 
# (доход больше влияет на ответ, чем возраст, тк разброс больше)

from tensorflow.keras.models import Sequential
import tensorflow as tf

# Заготовка для нейросети
model = Sequential()

from tensorflow.keras.layers import Dense

# Добавляем входной слой нейросетки, units - кол-во нейронов, здесь 15 для того чтобы 
# нейросеть обрабатывала 15 столбцов из датасета.
model.add(Dense(units = 15, activation = 'relu'))
# Внутренний слой, на котором нейросеть будет улавливать закономерности
model.add(Dense(units = 64, activation = 'relu'))
# Выходной слой из одного нейрона, который олицетворяет предсказанное значение (0 - не купил курс, 1 - купил курс)
model.add(Dense(units = 1, activation = 'sigmoid'))

# Готовим модель к обучению
model.compile(loss = 'mean_squared_error',
               optimizer=tf.keras.optimizers.SGD(
                  learning_rate=0.01, momentum=0.9, nesterov=True),
                  metrics = ['accuracy'])

# Обучаем модель сто раз пачками по 32 записи
model.fit(x_train,y_train, epochs = 100, batch_size = 32)

# Предсказываем результат с помощью нейросети по всей таблице
res = model.predict(x_train)

# берем первое предсказание для первой записи из всей таблицы (0.99)
print(res[0])

# берем истинное значение из первой таблицы, нейросеть предсказывает неплохо! (1)
print(y_train[0])

# пробуем узнать значение ошибки и точности нашей нейросети, 
# ошибки примерно 10%, точность 86%, т.е. 86 правильных ответов из 100
print(model.evaluate(x_train, y_train))

# Пробуем предсказать с помощью KNN
classifier = KNeighborsClassifier(n_neighbors = 19)
parametrs = {'n_neighbors': range(3, 302, 2)}

classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

# Матрица с результатами модели
print(confusion_matrix(y_test, y_pred))
# [[652  66]
#  [195 585]]

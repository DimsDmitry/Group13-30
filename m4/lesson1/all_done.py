import pandas as pd


# Шаг 1. Загрузка и очистка данных
df = pd.read_csv('titanic.csv')
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df['Embarked'].fillna('S', inplace=True)
df.drop('Embarked', axis=1, inplace=True)


age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()


def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3
    return row['Age']


df['Age'] = df.apply(fill_age, axis = 1)


def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0


df['Sex'] = df['Sex'].apply(fill_sex)


def is_alone(row):
    if row['SibSp'] + row['Parch'] == 0:
        return 1
    return 0


df['Alone'] = df.apply(is_alone, axis=1)
alone_tab = df.pivot_table(values='Age', columns='Alone', index='Survived', aggfunc='count')
print(alone_tab)
'''Среди пассажиров, которые были не одни, распределение выживших и погибших близко к соотношению 1:1 (175 и 179).
Среди пассажиров-одиночек погибших в 2 раза больше, чем выживших.
Вывод: Об одиноких пассажирах некому было позаботиться, в то время как члены семей помогали друг другу спасаться'''


# Шаг 2. Создание модели
from sklearn.model_selection import train_test_split
# Функция для разбиения исходного набора данных на выборки для обучения и тестирования модели.
from sklearn.preprocessing import StandardScaler
# Класс для стандартизации показателей.
from sklearn.neighbors import KNeighborsClassifier
# Класс для создания и обучения модели.
from sklearn.metrics import confusion_matrix, accuracy_score
# Функции для оценки точности модели

# Отделим целевую переменную от остальных данных
X = df.drop('Survived', axis=1)
print(X)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# train_test_split разбивает данные случайным образом на обучающие и тестовые


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
# Метод fit() подбирает признаки из набора обучающих данных


y_pred = classifier.predict(X_test)
print('Процент правильно предсказанных исходов:', accuracy_score(y_test, y_pred) * 100)
print('Confusion matrix:')
print(confusion_matrix(y_test, y_pred))

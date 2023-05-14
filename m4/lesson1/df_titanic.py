import pandas as pd


df = pd.read_csv('titanic.csv')
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)


age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()
print(age_1, age_2, age_3, sep='\n')


def fill_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3


df['Age'] = df.apply(fill_age, axis=1)


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
surv_table = df.pivot_table(values='Age', columns='Alone', index='Survived', aggfunc='count')
print(surv_table)


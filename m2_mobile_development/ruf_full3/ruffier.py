''' Модуль для расчёта результатов пробы Руфье.


Сумма измерений пульса в трёх попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту.
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд,
и приводим результат к ударам в минуту умножением на 4:
   S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10.


Индекс Руфье
   IR = (S - 200) / 10
оценивается по таблице в соответствии с возрастом:
       7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.    6.4 и менее    4.9 и менее       3.4 и менее         1.9 и менее               0.4 и менее
хор.    6.5 - 11.9     5 - 10.4          3.5 - 8.9           2 - 7.4                   0.5 - 5.9
удовл.  12 - 16.9      10.5 - 15.4       9 - 13.9            7.5 - 12.4                6 - 10.9
слабый  17 - 20.9      15.5 - 19.4       14 - 17.9           12.5 - 16.4               11 - 14.9
неуд.   21 и более     19.5 и более      18 и более          16.5 и более              15 и более


для всех возрастов результат "неуд" отстоит от "слабого" на 4,
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5


поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат


'''
# здесь задаются строки, с помощью которых изложен результат:
txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = []
txt_res.append('''низкая.
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная.
Обратитесь к врачу!''')
txt_res.append('''средняя.
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')


def ruffier_index(P1, P2, P3):
    ''' возвращает значение индекса по трем показателям пульса для сверки с таблицей'''
    return (4 * (P1 + P2 + P3) - 200) / 10


def neud_level(age):
    ''' варианты с возрастом меньше 7 и взрослым надо обрабатывать отдельно,
    здесь подбираем уровень "неуд" только внутри таблицы:
    в возрасте 7 лет "неуд" - это индекс 21, дальше каждые 2 года он понижается на 1.5 до значения 15 в 15-16 лет '''
    norm_age = (min(age, 15) - 7) // 2  # каждые 2 года разницы от 7 лет превращаются в единицу - вплоть до 15 лет
    result = 21 - norm_age * 1.5  # умножаем каждые 2 года разницы на 1.5, так распределены уровни в таблице
    return result


def ruffier_result(r_index, level):
    ''' функция получает индекс Руфье и интерпретирует его,
    возвращает уровень готовности: число от 0 до 4
    (чем выше уровень готовности, тем лучше).  '''
    if r_index >= level:
        return 0
    level = level - 4  # это не будет выполняться, если мы уже вернули ответ "неуд"
    if r_index >= level:
        return 1
    level = level - 5  # аналогично, попадаем сюда, если уровень как минимум "уд"
    if r_index >= level:
        return 2
    level = level - 5.5  # следующий уровень
    if r_index >= level:
        return 3
    return 4  # здесь оказались, если индекс меньше всех промежуточных уровней, т.е. тестируемый крут.


def test(P1, P2, P3, age):
    ''' эту функцию можно использовать снаружи модуля для подсчётов индекса Руфье.
    Возвращает готовые тексты, которые остаётся нарисовать в нужном месте
    Использует для текстов константы, заданные в начале этого модуля. '''
    if age < 7:
        return (txt_index + "0", txt_nodata)  # тайна сия не для теста сего
    else:
        ruff_index = ruffier_index(P1, P2, P3)  # расчет
        result = txt_res[ruffier_result(ruff_index, neud_level(
            age))]  # интерпретация, перевод числового уровня подготовки в текстовые данные
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res
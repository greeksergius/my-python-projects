#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################
###           СОРТИРОВЩИК ВОПРОСОВ ПО КЛЮЧЕВЫМ СЛОВАМ             ###
#####################################################################
# ВЕРСИЯ от 16.01.24

# Импорт необходимых библиотек
import re
import csv
# создаем список
questions = []
# читаем csv файл с вопросами
# ПОДРОБНО О МОДУЛЕ РЕГУЛЯРОК ДЛЯ ПАЙТОНА
# https://pythonru.com/osnovy/modul-re-dlja-reguljarnyh-vyrazhenij-v-python

### СОРТИРОВКА ПО ОДНОМУ КЛЮЧЕВОМУ
def onekeyword(keywordvalue):
    with open("questions.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель как новая строка","
        file_reader = csv.reader(r_file, delimiter="\n")
        # Считывание данных из CSV файла и осуществляем добавление в массив
        for row in file_reader:
          questions.extend(row)
    # создаем пустую переменную str
    totalinfo = ''
    #text = str('Уважаемый Владимир Владимирович, хочу спросить почему заключённых, которые отправились в зону СВО, через 6 месяцев отправляют домой на совсем и снимают судимость, а мой мобилизованный супруг, законопослушный гражданин в зоне СВО без срочно, чем он хуже заключённых?').lower()
    searchkeyword = str(keywordvalue).lower()
    totalinfo += '\n================================================================\nСОРТИРОВКА ПО КЛЮЧЕВОМУ СЛОВУ: ' + searchkeyword.upper() + "\n================================================================\n\n"
    count = 0
    for word in questions:
        # применяем поиск по регулярному выражению в во всем предложении по ключевому слова с переводом текста в нижний регистр
        # конец \b - строгое соотвтетсвие ключевому слову
        result = re.findall(r'\b' + searchkeyword + r'\b', word.lower())
        # меняем точку с запятой из csv на тире с пробелами
        word = word.replace(';', ' - ')
        # ищем вхождения и добавляем в общую переменную
        if searchkeyword in result:
          totalinfo += "ВОПРОС: " + word
          totalinfo += "\n \n"
          # объявляем счетчик
          count = count + 1
    totalinfo += "\nВСЕГО ВОПРОСОВ: " + str(count) + "\n"

    print(totalinfo)

    # создаем файл obrabotkaquest.txt
    f = open('obrabotkaquest.txt','a+')
    # пишем в него вывод переменной totalinfo и закрываем работу с файлом
    f.write(totalinfo)
    f.write("\n================================================================\n\n")
    f.close()

### СОРТИРОВКА ПО МАССИВУ КЛЮЧЕВЫХ
def multikeyword(tiplekeywords):
    with open("questions.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель как новая строка","
        file_reader = csv.reader(r_file, delimiter="\n")
        # Считывание данных из CSV файла и осуществляем добавление в массив
        for row in file_reader:
          questions.extend(row)
    # создаем пустую переменную str
    totalinfo = ''
    #text = str('Уважаемый Владимир Владимирович, хочу спросить почему заключённых, которые отправились в зону СВО, через 6 месяцев отправляют домой на совсем и снимают судимость, а мой мобилизованный супруг, законопослушный гражданин в зоне СВО без срочно, чем он хуже заключённых?').lower()
    searchkeyword = tiplekeywords

    count = 0
    for keyword in searchkeyword:
        totalinfo += '\n================================================================\nСОРТИРОВКА ПО КЛЮЧЕВОМУ СЛОВУ: ' + keyword.upper() + "\n================================================================\n\n"
        for word in questions:
            # применяем поиск по регулярному выражению в во всем предложении по ключевому слова с переводом текста в нижний регистр
            result = re.findall(r'\b' + keyword.lower() + r'', word.lower())
            # меняем точку с запятой из csv на тире с пробелами
            word = word.replace(';', ' - ')
            # ищем вхождения и добавляем в общую переменную
            if keyword.lower() in result:
              totalinfo += "ВОПРОС: " + word
              totalinfo += "\n \n"
              # объявляем счетчик
              count = count + 1
    totalinfo += "\nВСЕГО ВОПРОСОВ: " + str(count) + "\n"

    print(totalinfo)

    # создаем файл obrabotkaquest.txt
    f = open('obrabotkaquest.txt','a+')
    # пишем в него вывод переменной totalinfo и закрываем работу с файлом
    f.write(totalinfo)
    f.write("\n================================================================\n\n")
    f.close()



##################          НЕ СООРТИРОВАННЫЙ СПИСОК ВОПРОСОВ            ###########################

### ПРОГОН ПО РЕГУЛЯРКЕ С МНОЖЕСТВОМ КЛЮЧЕВЫХ СЛОВ БЕЗ  КОНКРЕТНЫХ ОКОНЧАНИЙ
def nosortmulti(tiplekeywords):
    with open("questions.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель как новая строка","
        file_reader = csv.reader(r_file, delimiter="\n")
        # Считывание данных из CSV файла и осуществляем добавление в массив
        for row in file_reader:
          questions.extend(row)
    # создаем пустую переменную str

    newlistvopros = ['']
    nosortopros = ['']
    count = 0

    for key in tiplekeywords:

        for vopros in questions:
            result = re.findall(r'\b' + key.lower() + r'', vopros.lower())
            if key in result:
                #print(vopros)
                #newlistvopros.append(vopros)

                # удаляем вопрос из общего списка вопросов и вовзращаемся к итерации
                questions.remove(vopros)
                count = count + 1

    # Создаем список SET  с уникальными значениями и вносим его в ту же переменную, после чего возвращаем.
    newlistvopros = set(newlistvopros)

    return questions

###### ПРОГОН ПО КЛЮЧЕВЫМ СЛВОАМ НА СТРОГОЕ СООТВЕТСТВИЕ. Используется с return от первой обработки
def nosortsingle(singletiplekeywords, newlistvoprosenter):
    savefromfile = ''
    newlistvopros = ['']
    voproscheck = ''
    count = 0
    voprosarray = newlistvoprosenter
    for key in tiplekeywords:

        for vopros in questions:
            result = re.findall(r'\b' + key.lower() + r'\b', vopros.lower())
            if key in result:
                #print(vopros)
                newlistvopros.append(vopros)
                # удаляем вопрос из общего списка вопросов и вовзращаемся к итерации
                questions.remove(vopros)

    #  Создаем список SET  с уникальными значениями и вносим его в ту же переменную
    newlistvopros = set(questions)

    # обрабатываем в цикле фильтрованный список сетом, добавляем в переменную savefromfile вопросы для последующей записи их в текстовый файл
    /*for wordcomplete in newlistvopros:
        count = count + 1
        # заменяем точку с запятой из данных на тире
        wordcomplete = wordcomplete.replace(';', ' - ')
        savefromfile += 'ВОПРОС: ' + str(count) + "\n" + wordcomplete + "\n\n"

    # создаем файл obrabotkaquest.txt
    print(len(newlistvopros))
    f = open('obrabotkanosort.txt', 'a+')
    # пишем в него вывод переменной savefromfile и закрываем работу с файлом
    f.write(savefromfile)
    f.close()

    # Возвращаем обработанные данные
    return newlistvopros*/



tiplekeywords = ['фронт','военнослужащи','ранен','больниц','врач','выплат','тариф','отоплени','жкх','отоплени','горячая вода','газ','дороги','электричеств','отоплени','теплотрасс','школ','пособи', 'университет','учител','ЕГЭ','ОГЭ','экзамен','Авиа','многодетн','пенси','капитал','детские пособи','Авиаци','цен']
singletiplekeywords = ['СВО','фронт','военнослужащий','ранение','больница','выплаты','пенсии','тарифы','жкх','дороги','электричество','теплотрасса','ЕГЭ','ОГЭ','экзамены','Мат капитал','детские пособия','цены', 'отопление']

# Вызываем обработку с ключевыми слвоами без явных окочнаний (на не строгое соответствие) и добавляем в переменную sortmultiquestion вызов функции nosortmulti с ключевыми слвоами из списка tiplekeywords
sortmultiquestion = nosortmulti(tiplekeywords)
# Добавляем в переменную ретурн функции nosortsingle (строгого исключения по ключевым словам) с входными данными списка клюевы singletiplekeywords и вторым входным элементом - ретурн с переменной sortmultiquestion (первая обработка на нестрогие)
totalvopros = nosortsingle(singletiplekeywords,sortmultiquestion)
print(totalvopros)
print(len(totalvopros))


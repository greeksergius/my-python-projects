#!/usr/bin/python
# -*- coding: utf-8 -*-

#####################################################################
###       РАНДОМАЙЗЕР ВАРИАНТОВ ЗАДАНИЙ НА ЭКЗАМЕН ПО ОСИС        ###
#####################################################################
# ВЕРСИЯ от 04.12.23

# Импорт необходимых библиотек
import random as rm
import csv
#fio_list = ["Иван", "Моря", "Андрюська", "Хрюська", "Баска", "Деребаска"]
#number_var = ["1", "2", "3", "4", "5", "6"]
#print(rm.sample(fio_list, 3))
#print("Вывод случайного целого числа ", rm.randrange(1,20))

# создаем список
fio_list = []
# читаем csv файл fiogroups.csv со списком ФИО
with open("fiogroups.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель как новая строка","
    file_reader = csv.reader(r_file, delimiter = "\n")
    # Считывание данных из CSV файла и осуществляем добавление в массив
    for row in file_reader:
      fio_list.extend(row)
#print(fio_list)
# создаем пустую переменную str
totalinfo = ''

groupscheck = ['КИСП-9-21(1)', 'КИСП-9-21(2)', 'КИСП-9-21(3)', 'КИБ-22','КИСП-22(1)', 'КИСП-22(2)', 'КИСП-22(3)']

for student in fio_list:
    if student in groupscheck:
        print("\n==============================================================")
        totalinfo += "\n==============================================================\n"
        print("Группа:",student)
        totalinfo += "Группа: "+student+"\n"
        print("==============================================================\n")
        totalinfo += "==============================================================\n"
    #rando = rm.randint(1, 3)
    else:
        print("Студент: ", student, "- Номер варианта:", rm.randrange(1,19) )
        listreduce = f"Студент:  {student} - Номер варианта: {rm.randrange(1,19)}"
        # добавляем в переменную totalinfo каждый вывод конкотинации цикла (listreduce) с новой строки
        totalinfo += (str(listreduce)) + "\n"

print("\nСтудент счастлифчик: ", rm.choice(fio_list))
totalinfo += "\nСтудент счастлифчик: " + str(rm.choice(fio_list))

# создаем файл variantsresponse.txt
f = open('variantsresponse.txt','a+')
# пишем в него вывод переменной totalinfo и закрываем работу с файлом
f.write(totalinfo)
f.write("\n================================================================\n\n")
f.close()

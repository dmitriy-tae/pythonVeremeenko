print('\n\nПРАКТИЧЕСКОЕ ЗАДАНИЕ № 1 **************')
print('Программный файл с построчными данными от пользователя\n')

numStr = 1
f = open(r'1.txt', 'w+', encoding='utf-8')
while True:
    print('Напишите содержимое', numStr, 'строки, или нажмите Enter, если хотите закончить: ')
    i = input('_: ')
    numStr = numStr + 1
    print(i, file=f)
    if i == '':
        break
f = open(r'1.txt', 'r', encoding='utf-8')
for i in f:
    print(i, end='')
f.close()




print('\nПРАКТИЧЕСКОЕ ЗАДАНИЕ № 2 **************')
print('Подсчёт строк и слов в каждой строке созданного файла\n')

f = open(r'2.txt', 'r', encoding='utf-8')
numL = 0 # number of lines
for i in f:
    numL = numL + 1
f.seek(0)
numL_2 = 0
while numL_2 < numL:
    text = f.readline()
    result = len(text.split())
    numL_2 = numL_2 + 1
    print('В строке документа №', numL_2, 'содержится', str(result), 'слово(а)')
f.close()
print('\nКоличество строк в документе = ', numL, '\n')



print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ № 3 **************')
print('Анализ окладов сотрудников\n')
f = open(r'3.txt', 'r', encoding='utf-8')
numL = 0 # number of lines
for i in f:
    numL = numL + 1
f.seek(0)
numL_2 = 0
totIncome = 0
print('Список сотрудников с доходом менее 20 000:\n')
while numL_2 < numL:
    text = f.readline()
    spl = text.split()
    salary = spl[1]
    salary_1 = float(salary)
    totIncome = totIncome + salary_1
    surname = spl[0]
    if salary_1 < 20000:
        print(surname, salary_1)
    numL_2 = numL_2 + 1

f.close()
u = totIncome / numL
t = int(u)
print('\nСредняя величина дохода сотрудников =', t, '\n')




print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ № 4 **************')
print('Прочитать файл, заменить английские числительные на русские и записать в новый файл. \n')

file_r = open(r'4.txt', 'r', encoding='utf-8')
file_w = open(r'5.txt', 'w', encoding='utf-8')
NumDict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
numL = 0 # number of lines
for i in file_r:
    numL = numL + 1
file_r.seek(0)
print('\nВ новом файле 5.txt были созданы следующие строки:')
numL_2 = 0
while numL_2 < numL:
    text = file_r.readline()
    spl = text.split()
    part_1 = spl[0] # part of the text 1
    part_2 = spl[1]
    part_3 = spl[2]
    print(NumDict[part_1], part_2, part_3)
    print(NumDict[part_1], part_2, part_3, file=file_w)
    numL_2 = numL_2 + 1
file_r.close()
file_w.close()



print('\n\nПРАКТИЧЕСКОЕ ЗАДАНИЕ № 5 **************')
print('Запись чисел в файл и подсчет их суммы\n')
f = open(r'6.txt', 'w+', encoding='utf-8')
lineNum = input('Запишите через пробел любые числа: ')
print(lineNum, file=f)
print('В файл 6.txt записана следующая строка чисел:', lineNum)
spl = lineNum.split()
len_1 = len(spl)
len_2 = 0
totalSum = 0
while len_2 < len_1:
    n = spl[len_2]
    everyNum = float(n)
    totalSum = totalSum + everyNum
    len_2 = len_2 + 1
totalSum_2 = int(totalSum)
print('Сумма всех записанных в файл чисел равна:', totalSum_2)



print('\n\nПРАКТИЧЕСКОЕ ЗАДЕНИЕ № 6 **************')
print('Сформировать словарь, содержащий название предмета и общее количество занятий по нему\n')
clSch = open(r'7.txt', 'r', encoding='utf-8')
numL = 0
for i in clSch:
    numL = numL + 1
clSch.seek(0)
numL_2 = 0
totIncome = 0
import re
scones = {}
while numL_2 < numL:
    text = clSch.readline()
    spl = text.split()
    spl = re.split('[()]|:|[а-я]|[А-Я]|—|[.]|\n', text)
    length = len(spl)
    length_2 = 0
    sum = 0
    while length_2 < length:
        try:
            el = int(spl[length_2])
            sum = sum + el
        except ValueError:
            ""
        length_2 = length_2 + 1
    spl = text.split(':')
    part_1 = spl[0]
    numL_2 = numL_2 + 1
    scones[part_1] = sum
print(scones)



print('\n\nПРАКТИЧЕСКОЕ ЗАДЕНИЕ № 7 **************')
print('Расчет прибыли компаний, создание списка словарей и сохранение списка в json-объекте\n')

report = open(r'8.txt', 'r', encoding='utf-8')
numL = 0
for i in report:
    numL = numL + 1
report.seek(0)
numL_2 = 0
totProfit = 0
numProfitComp = 0
dict_1 = {}
dict_2 = {}
while numL_2 < numL:
    text = report.readline()
    spl = text.split()
    company = spl[0]
    legalForm = spl[1]
    income = spl[2]
    сosts = spl[3]
    incomeInt = int(income)
    сostsInt = int(сosts)
    profit = incomeInt - сostsInt
    print(legalForm, company, '| прибыль =', profit)
    # dic_1 = {company: profit}
    # print(dic_1)
    dict_1[company] = profit
    numL_2 = numL_2 + 1
    if profit >= 0:
        totProfit = totProfit + profit
        numProfitComp = numProfitComp + 1
report.close()
u = totProfit / numProfitComp
t = int(u)
print('\nСредняя прибыль =', t, '\n')
dict_2['average_profit'] = t
myList = [dict_1, dict_2]
print(myList)

import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(myList, f)
print('Создан файл data.json, который содержит аналогичные верхней строке списка данные')
print('Конец домашнего задания')
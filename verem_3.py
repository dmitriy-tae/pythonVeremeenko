#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №1
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №1')
def div():
    a = int(input('Введите 1-ый аргумент (любое число): '))
    while True:
        b = int(input('Введите 2-ой аргумент (любое число): '))
        if b == 0:
            print('Нельзя вводить ноль!')
        if b != 0:
            break
    res = a / b
    print('Результат деления первого аргумента на второй ', res)
div()
print('\n'
      '')

#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №2
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №2')
def print_info(name, surname, yearBirth, sity, email, phone):
    print(f'Name: {name}, surname: {surname}, year of birth: {yearBirth}, city of residence: {sity}, email: {email}, phone: {phone}.')
a = 'Dmitrii'
b = 'Veremeenko'
c = '1976'
d = 'Moscow'
e = 'dmitriy-tae@yandex.ru'
f = '+7(925)924-43-28'
print_info(a, b, c, d, e, f)
print('\n'
      '')

#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №3
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №3')
def my_func(var_1, var_2, var_3):
    minimum = min(var_1, var_2, var_3)
    print('Сумма наибольших двух из введенных вами чисел равна =', var_1 + var_2 + var_3 - minimum)
a, b, c = input('Введите 3 числа через пробел: ').split()
a = int(a)
b = int(b)
c = int(c)
my_func(a, b, c)
print('\n'
      '')

#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №4
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №4')
def expon():
    while True:
        j = int(input('Введите любое число больше нуля: '))
        if j <= 0:
            print('Нельзя вводить число меньше или равное нулю!')
        if j > 0:
            break
    while True:
        n = int(input('Введите любое целое (не дробное) отрицательное (со знаком минус) число: '))
        if n >= 0:
            print('Нельзя вводить число, большее или равное нулю!')
        if n < 0:
            break
    sc = abs(n)
    res_1 = 1
    while sc > 0:
        res_1 = res_1 * (1/j)
        sc = sc-1
    print('Сложный вариант решения: ', j, 'в степени', n, '=', round(res_1, 3))
    print('Простой вариант решения: ', round(j ** n, 3))
expon()
print('\n'
      '')

#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №5
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №5')
def f1():
    summa = 0
    while True:
        print('Чтобы остановить прибавление чисел, стоящих после буквы z, ведите букву z вместо любого числа')
        li = input("Введите числа через пробел: ").split()
        a = 0
        b = 1
        c = len(li) - 1
        for el in li:
            if li[a] != "z":
                li[a] = int(li[a])
                summa = summa + li[a]
                a = a + 1
            if a > c:
                break
        print('Сумма всех введенных ранее чисел','=', summa)
        if a <=c:
            break
f1()
print('End')
print('\n'
      '')

#  ПРАКТИЧЕСКОЕ ЗАДАНИЕ №6
print('ПРАКТИЧЕСКОЕ ЗАДАНИЕ №6')
def int_func():
    li = input('Введите через пробел любые слова, написанные маленькими буквами: ').split()
    a = 0
    b = 1
    c = len(li) - 1
    for el in li:
        word = li[a]
        print(word.title())
        a = a + 1
        if a > c:
            break
int_func()
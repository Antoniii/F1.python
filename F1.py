# coding: utf8
# - для восприятия кириллицы

#import __hello__


#raw_input("Press any key to exit") # оставляет экран
#после непосредственного запуска до нажатия клавиши

'''
# Определить текущую версию питона

import sys
print sys.version_info
'''

'''
n = 10**10
print(1+1, 0**0, (1.0+1.0/n)**n)
'''

"""

# решение квадратных уравнений a*x**2+b*x+c=0
import math


a = 1
b = 0
c = -1

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2.0*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2.0*a)

print(x1, x2) # выводит корни уравнения 
#print(x2)



# функция для решения квадратного уравнения
def printRoots(a,b,c):
    
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2.0*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2.0*a)
    
    print(x1, x2)

printRoots(1,2,-8)
printRoots(1,0,-1)

"""

"""
# функция рассчёта расстояния между 2 точками в пространстве
import math

def distance(x1,x2,x3,y1,y2,y3):

    d = math.sqrt((x1-y1)**2 + (x2-y2)**2 + (x3-y3)**2)

    print(d)

distance(1,1,1,2,3,5)

"""

"""
import math

def printRoots(a,b,c):
    adress1 = a
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2.0*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2.0*a)
    adress2 = a
    print(x1, x2)

adress1 = 'test1'
adress2 = 'test2'

printRoots(1,2,-8)
print(id(adress1), id(adress2))

# id() - возвращает адреса объекта в памяти
"""


"""
# Поток выполнения

def f1():
    print "f1() begins"
    print "Hello world"
    print "f1() ends"

def f3():
    print "f3() begins"
    f2()
    print "f3() ends"

def f2():
    print "f2() begins"
    f1()
    print "f2() ends"

print "Main program begins"
f3()
print "Main programs ends" 
print # печатает пустую строку

def f1():
    print "f1() begins"
    print "Hello world"
    #a = 1/0
    print "f1() ends"

def f2():
    print "f2() begins"
    f1()
    print "f2() ends"

def f3():
    print "f3() begins"
    f2()
    print "f3() ends"

print "Main program begins"
f3()
print "Main programs ends" 
"""

"""
# Возвращение результата

def getSum(x,y):
    z = x + y
    return z # команда для возвращения результата работы
    # функции в подпрограмму для дальнейшей обработки 

print getSum(1, 4)


def printRoots(a,b,c):
    
    import math
    
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2.0*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2.0*a)
    
    return x1, x2 # можно вернуть несколько значений одновременно

print printRoots(1,2,-8)
"""

"""
# Выполнеение по условию


def printRoots(a,b,c):
    
    import math

    D = b**2 - 4*a*c

    if D < 0:
        return None, None # None - встроенная константа для пустоты
    
    x1 = (-b + math.sqrt(D))/(2.0*a)
    x2 = (-b - math.sqrt(D))/(2.0*a)
    
    return x1, x2 # можно вернуть несколько значений одновременно

print printRoots(3,2,1)



# Сравнение двух чисел

def compare(x,y):

    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

print compare(0.5,-1)
"""

"""
# Ввод данных с клавиатуры

a1 = input("Give me your first fucking coefficient, nigga ") 
b1 = input("Second ") # для ввода чисел
c1 = input("Next, bitch ")

def printRoots(a,b,c):
    
    import math

    D = b**2 - 4*a*c

    if D < 0:
        return None, None # None - встроенная константа для пустоты
    
    x1 = (-b + math.sqrt(D))/(2.0*a)
    x2 = (-b - math.sqrt(D))/(2.0*a)
    
    return x1, x2 

print printRoots(a1,b1,c1)


name_user = raw_input("What you name, guy? ") # для ввода текста

print 'Nice to meet you, ', name_user
"""

"""
# Разветвленные условные операторы

def compare(x,y):

    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1
    else:
        return 'WTF?'

print compare(0.5,-1)


# Пустое слово

def f1(): # эта функция ничего не делает
    pass
# поток выполнения, заглянув в неё, переходит к выполнению
# следующей инструкции
"""


"""
# Вложенные условные операторы

def cut_number1(x):
    if x < -5:
        print "x isn't between -5 and 5"
    else:
        if x < 5:
            print "x is between -5 and 5"
        else:
            print "x isn't between -5 and 5"

cut_number1(2)
    

def cut_number2(y):
    if -5 < y < 5:
        print "y is between -5 and 5"
    else:
        print "y isn't between -5 and 5"

cut_number2(-7)
"""


"""
# Рекурсия

def fact(n):
    if n < 0 or n - int(n) <> 0 :
        return "Sorry, guy, it's not OK"
    elif n == 0:
        return 1
    return fact(n-1)*n

print fact(1.1)
#print fact(100)
"""


"""
# Числа Фибоначчи

def fibonacci(n):
    if n < 0 or n - int(n) <> 0 :
        return "Sorry, guy, it's not OK"
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(7)



# Расчёт суммы ряда 
# \sum_{i=1}^n i^k через рекурсию

def summ(n,k):
    if n: # эквивалентно if n > 0
        return summ(n-1,k) + n**k
    else:
        return 0

print summ(3,4)




# Использование accumulate 

def summ1(n,k,acc=0):    
    if n: # эквивалентно if n > 0
        return summ1(n-1,k,acc + n**k)
    else:
        return 0

print summ1(3,4)


def fib_acc(n,a = 1,b = 1):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_acc(n-1,b,a+b)

print fib_acc(7)

# даёт неверный расчёт. Почему?
"""



"""
# Цикл while vs. recursio for summ


import math 
from time import clock

def summ_row(n,k):
    sum = i = 0
    while i <= n:
        sum += i**k # sum = sum + i**k
        i += 1 # i = i + 1
    return sum


def summ(n,k):
    if n: # эквивалентно if n > 0
        return summ(n-1,k) + n**k
    else:
        return 0

t1 = clock()
res1 = summ_row(6,9)
t2 = clock()

t3 = clock()
res2 = summ(6,9)
t4 = clock()

print ('while', res1, (t2-t1)*10**6, 'microsec')
print ('recursio', res2, (t4-t3)*10**6, 'microsec')
"""


"""
# Бесконечный цикл - зацикливание
# уничтожается Ctrl+c

i = 0
while i < 10:
    print i
"""


"""
# Расширенный вариант оператора цикла

i = 0
while i <> 5:
    print i
    i += 1
else:
    print "end of loop"
"""



"""
# Табулирование функций
# "\t" - знак табуляции

import math
x = 1.0
while x < 10.0:
    print x, "\t", math.log(x)
    x += 1.0
"""

"""
# Поиск степеней 2-ки

import math
x = 1.0
while x < 2000.0:
    print x, "\t", math.log(x)/math.log(2)
    x *= 2
"""


"""
# Специальные символы

# \n - переход на новую строку
# \r - возврат курсора в начало строки - не раборает?

print "hello\rH\n\tworld"


# Экранирующий символ \

print "Main \\templace/"
print "I said: \"Hello world\""
print 'He said: "Hello world"'
"""


"""
# Цикл while vs. recursio for Fibonacci


import math 
from time import clock

def fibonacciWithWhileLoop(n):
    if n < 0 or n - int(n) <> 0 : # проверка корректности n
        return "Sorry, guy, it's not OK"
    fn = fn1 = fn2 = 1
    i = 3
    while i <= n:
        fn = fn1 + fn2
        fn2 = fn1
        fn1 = fn
        i += 1
    return fn
    

def fibonacci_R1(n):
    if n < 0 or n - int(n) <> 0 :
        return "Sorry, guy, it's not OK"
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci_R1(n-1) + fibonacci_R1(n-2)


def fibonacci_R2(n):
    if n < 0 or n - int(n) <> 0 :
        return "Sorry, guy, it's not OK"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci_R2(n-1) + fibonacci_R2(n-2)



t1 = clock()
res1 = fibonacciWithWhileLoop(30)
t2 = clock()

t3 = clock()
res2 = fibonacci_R1(30)
t4 = clock()

t5 = clock()
res3 = fibonacci_R2(30)
t6 = clock()

print ('while', res1, (t2-t1)*10**6, 'microsec')
print ('recursio', res2, (t4-t3)*10**6, 'microsec')
print ('recursio elif', res3, (t6-t5)*10**6, 'microsec')
"""



"""
# Вложенные операторы цикла
# таблица умножения


i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print i*j, "\t",
        j += 1
    print
    i += 1
"""

"""
# Строки
# оператор индексирования

print 'hello'[0]

# длина строки

print len("Hello world!")

# отрицательные индексы

a = 'Hello!'

print a[len(a)-1]
print a[-1]
print a[-5]
"""

"""
# программа, которая выводит длину введенной пользователем 
# строки, а также первый, пятый и последний символ.

string_by_user = raw_input("Input your word: ")

if len(string_by_user) >= 5:
    print string_by_user[0], string_by_user[4], string_by_user[-1]
else:
    print "Sorry. This is short word"
"""

"""
# функция, которая получает в качестве параметра строку и 
# выводит символы, ее составляющие, в обратном порядке.

a = raw_input("Input your string: ")

index = len(a)
while index > 0:
    letter = a[index-1]
    print letter
    index = index - 1
print
# обратная функция

string = "hello"
index = 0
while index < len(string):
    letter = string[index]
    print letter
    index += 1

print
# через цикл for

string = "hello"
for letter in string:
    print letter
"""

"""
# Срезы строк

s = 'Five Finger Death Punch'

print s[0:5]
print s[-3:-1]
print s[5]
print s[-3:]
print s[:]
print s[::2]
print s[::3]
print s[1:6:2]
"""

"""
# Сравнение строк
# упорядочивание слов в алфавитном порядке
# регистр вкл в питоне. Заглавный символ больше,
# чем любой строчный


def abc(word):
    if word < "banana":
        print "Your word, " + word + ", comes before banana."
    elif word > "banana":
        print "Your word, " + word + ", comes after banana."
    else:
        print "Yes, we have bananas!"


abc('all')
abc('finger')
abc('Zebra')
abc('banana')
"""

"""
# Строки нельзя изменить
# для замены символа требуется создавать новую строку

greeting = 'Hello, world!'
#greeting[0] = 'J' - Error
NewGreeting = "J" + greeting[1:]

print NewGreeting
"""


"""
# Функция find() [является встроенной
# в модуле string] - возвращает индекс первого вхождения
# символа в строке. Если 
# символ не найден, то функция возвращает -1.


def find(str, ch):
    index = 0
    while index < len(str):
        if str[index] == ch:
            return index
        index += 1
    return -1

print find('qwerty', 'r')
"""


"""
# Счёт количества символов,
# встречающихся в строке

fruit = 'banana'
count = 0
for char in fruit:
    if char == "a":
        count += 1
print count
"""


"""
# Пример классификации символов

import string

def isLower1(ch):
    return string.find(string.lowercase, ch) <> -1

def isLower2(ch):
    return ch in string.lowercase 

def isLower3(ch):
    return 'a' <= ch <= 'z'

print isLower1('b')
print isLower2('B')
print isLower3('5')
"""


"""
# Списки

print range(1,5) # от 1 до 5-1=4
print range(10) # от 0 до 10-1=9
print range(1,10,2) # 2 - шаг

print [] # - пустой список

numbers = [17,59,277,1697]
print numbers
print numbers[0]
print numbers[-2]


list1 = ['a','b','c','d','e','f']
print list1[1:3]
print list1[:4]
print list1[3:]
print list1[:]

# Элементы списков (в отличии о строк) могут меняться

numbers[1] = 23
print numbers

numbers[1:] = [37,19]
print numbers

# Длина списка

# если список содержит в качестве элемента другой список, то 
# этот вложенный список будет считаться как один элемент.


mylist = [[1,'one'],[2,'two'],[3,'three'],[4,'four'],
          [5,'five'], 6]

print len(mylist)
print len(mylist[0]) # длина подсписка


# программа, которая запрашивает количество элементов
# списка у пользователя, а затем поочередно предлагает
# пользователю ввести указанное количество элементов
# списка. По завершении ввода программа должна вывести список.

n = input("Vvedite dlinu spiska: ")
s = []
for i in range(n):
    i = input("Vvedite element spiska: ")
    s.append(i) 
    i += 1
print s

# Принадлежность элемента последовательности

print 1 in mylist
print [1,'one'] in mylist
print 6 in mylist


# Списки и цикл for

s = 0
for number in range(21):
    if number % 2 == 0:
        s += 1
        print number
print "quantity even numbers = ", s   


# Операции над списками

a = [1,2,3]
b = [4,5,6]

c = a + b
c1 = b + a

d = a *4
d1 = 4 * a

print a,b,c,c1,d,d1

# Сцепление 2-х списков с помощью среза

a[3:] = b
print a

# Удаление элементов списка

del c[1]
del a[3:]
print c, a


# Вложенные списки

l = [1,2,[3,4]]

print l[2][1]


# Матрицы

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print matrix[1]
print matrix[0][1]
"""






'''
Разбейте строку из переменной song на слова, а затем сцепите
их в обратном порядке так, чтобы при выводе на экран слова
строки выводились по одному на каждой строке.
'''

"""
import string as s

song = 'The rain in Spain ...'
a = s.split(song)
d = s.split(s.join(a.__reversed__()))
print song

n = len(d)
for i in range(n):
    print d[i]
"""





"""

# Кортежи


t1 = ('a',) # - кортеж. Скобки необязятельны. Запятая обязательна.

t2 = ('a') # - строка в скобках


tuple = ('a','b','c','d','e')

print tuple[0]
print tuple[1:3]

'''
мы не можем менять элементы кортежа, мы можем заменить его другим 
кортежем:
'''

tuple = ('A',) + tuple[1:]
print tuple



# Применение кортежи: поменять местами значения двух переменных

a = 0
b = 1

print (a,b)

a, b = b, a

print (a,b)

'''
Слева кортеж переменных, справа кортеж значений. Каждое значение
соответствует своей переменной. Все выражения справа вычисляются
до присвоения.
'''





# Случайные числа (точнее псевдослучаные)

'''
Модуль random включает в себя функцию random, которая
возвращает действительное число в диапазоне от 0.0 до 1.0.
'''

# симуляция игральных костей
import random

high = 6 # - верхняя граница. '+1' включает в интервалверхнюю границу
low = 1 # - нижняя граница

for i in range(2):
    x = low + (high-low+1)*random.random()
    print int(x)




# Генерация произвольного пароля

'''
Хороший пароль должен быть произвольным и состоять
минимум из 6 символов, в нём должны быть цифры,
строчные и прописные буквы. Приготовить такой пароль
можно по следующему рецепту:
'''

import random

# Щепотка цифр
str1 = '123456789'
# Щепотка строчных букв
str2 = 'qwertyuiopasdfghjklzxcvbnm'
# Щепотка прописных букв. Готовится преобразованием str2  в верхний регистр.
str3 = str2.upper() # 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Соединяем все строки в одну
str4 = str1+str2+str3
#'123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBN

# Преобразуем получившуюся строку в список
ls = list(str4)
# Тщательно перемешиваем список
random.shuffle(ls)
# Извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psw)


'''
Этот же скрипт можно записать всего в 1 строкy:
'''

print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))


'''
Данная команда является краткой записью цикла for,
вместо неё можно было написать так:
'''

psw = '' # предварительно создаем переменную psw
for x in range(12):
    psw = psw + random.choice(list(
            '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

print(psw)


'''
Данный цикл повторяется 12 раз и на каждом круге
добавляет к строке psw произвольно выбранный
элемент из списка.
'''





'''
Создание генератора случайных чисел без повтора.
Симуляция экзаменационных билетов.
'''

import random

# Создаём интересующий нас список

m = 1 # 1-й элемент списка
n = 15 # последний
s = []

for i in range(m,n+1): # +1 т.к. полуинтервал открыт справа
    s.append(i) 
    i += 1

random.shuffle(s) # перемешиваем список

#print s[:2] # берём 2 номера вопросов нашего билета


# тоже самое, что

for i in range(2):
    print s[i]




    
'''
Сколько всего есть четырехзначных чисел, которые делятся
на 19 и оканчиваются на 19?
'''

count = 0
for i in range(1019,9919,100):
    if i % 19 is 0:
        print i
        count += 1
print(count)




# Список случайных величин

import random

def randomList(n):
    s = [0]*n
    for i in range(n):
        s[i] = random.random()
    return s

print randomList(8)






# Паттерны программирования
# pattern – пример, образец


'''
мы просматриваем список значений и считаем количество значений, 
попадающих в данный диапазон.
'''


'''
мы написали программу, которая просматривает строку и считает, 
сколько раз в строке присутствует заданная буква. Поэтому, мы
можем начать с копирования старой программы и адаптации ее под
текущую задачу. Исходный код программы был такой:
'''

count = 0
for char in fruit:
    if char == 'a':
        count += 1
print count


'''
копируя и модифицируя существующую программу можно быстро 
реализовать нужную функциональность и не тратить много времени
на разработку алгоритма.
'''


def inBucket(list, low, high):
    count = 0
    for num in list:
        if low < num < high:
            count += 1
    return count

"""


"""
# Словари
# Создание словаря (англо-испанский)


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

print eng2sp
print eng2sp['one']


# Операции над словарями


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 
'pears': 217}

print inventory

del inventory['pears'] # Оператор del удаляет из словаря пару ключ-значение.

print inventory

inventory['pears'] = 0

print inventory

print len(inventory) # возвращает число пар ключ-значение



# Методы словарей

'''
Метод – это обычная функция, принимающая аргументы и возвращающая
значения, но отличающаяся синтаксисом вызова.
'''

print eng2sp.keys() # метод key получает словарь и возвращает список
                    # ключей которые находит

# Пустые круглые скобки показывают, что этот метод не принимает параметров.


print eng2sp.values() # возвращает список значений в словаре

print eng2sp.items() # возвращает список кортежей ключ-значение


'''
Если метод принимает аргументы, он использует тот же синтаксис что
и вызов функции. Например, метод has_key() принимает ключ и возвращает
истину (True) если такой ключ присутствует в словаре.
'''

print eng2sp.has_key('one')

print eng2sp.has_key('hour')

'''
Если вы хотите изменить словарь и сохраняете копию оригинала,
используйте метод copy().
'''

copy = eng2sp.copy()

'''
Если мы изменим copy, то словарь eng2sp останется прежним.
'''
"""


"""
# Разряженные матрицы


matrix1 = [ [0,0,0,1,0],
            [0,0,0,0,0],
            [0,2,0,0,0],
            [0,0,0,0,0],
            [0,0,0,3,0] ]

'''
Но есть и другой способ хранения матриц – мы можем использовать
словарь: ключами будут кортежи, хранящие номер строки и номер
столбца.
'''


matrix2 = {(0,3): 1, (2, 1): 2, (4, 3): 3}


print matrix1[0][3]
print matrix2[0,3]

'''
Если мы укажем на нулевой элемент, мы 
получим ошибку, так как в словаре нет элемента
с таким ключом.

Данную проблему решает метод get().

Первый аргумент – ключ, второй аргумент – значение,
которое get() должен 
возвратить, если такого ключа в словаре нет.
'''

print matrix2.get((0,3), 0)
print matrix2.get((1,3), 0)
"""


"""
# Подсказки
'''
Предыдущее вычисленное значение, которое запоминается
для последующего использования, называют подсказкой.
'''

# Числа Фибоначчи с подсказкой

previous = {0:1, 1:1} # словарь начальных данных

def fibonacci(n):
    if previous.has_key(n): # проверяет словарь, чтобы 
                            # определить содержит ли он результат
        return previous[n] 
    else: 
        newValue = fibonacci(n-1) + fibonacci(n-2) 
        previous[n] = newValue # Новое значение добавляется в словарь,
                                # перед тем как функция
                                    # вернёт результат.
        return newValue

print fibonacci(995)



# Тип «длинное целое число»

a = long(1)
b = 2L
print type(a), type(b)
"""


"""
# Подсчет букв
'''
построение гистограммы букв в строке, то есть вычисление,
сколько раз каждая буква появляется в строке.

Словари предоставляют элегантный способ создавать гистограммы:

Мы начинаем с пустого словаря. Для каждой буквы в строке мы находим
текущий счетчик (возможно нулевой) и увеличиваем его на единицу.
В конце словарь содержит пары: 
буквы и их частоты.

Для красоты можно вывести гистограмму в алфавитном порядке
с помощью методов 
items() и sort():
'''

string = "Mississippi 63416853004188347129368737436524797022794930"


letterCounts = {}

for letter in string:
    letterCounts[letter] = letterCounts.get(letter, 0) + 1

letterItems = letterCounts.items()
letterItems.sort()

print letterItems
"""


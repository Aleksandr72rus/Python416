# name = "admin"
# #print("Hello,", name, "!")
# age = 20
# #print(name + str(age))
# age = 15.2
# print(age)
# print(type(name))
# print(type(age))
from calendar import firstweekday
from html.parser import starttagopen, endendtag
from idlelib.debugger_r import restart_subprocess_debugger
from math import trunc
from tkinter.font import names

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b #5
# print(a)
# print(id(a))
# print(id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# first_name = "admin"
# print(first_name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")

# a = 5
# b = 7
# print("a:", a)
# print("b:", b)
#
# #1 способ
# # temp = a
# # a = b
# # b = temp
# #2 способ
# # a, b = b, a
# #3 способ
# # a = a + b
# # b = a - b
# # a = a - b
#
# print("a:", temp)
# print("b:", temp2)

# 2 ЗАНЯТИЕ

# print("строка "
#       "символов")
# print('строка \nсимволов')

# print("\tДокумент \"file.txt\"      находится по пути: \rD\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма", res)
# print("Произведение", a * b * c)
# print("Среднее арифметическое:", res / 3)

# print(6 + 4 * 5 ** 2 + 7) #113
# print((6 + 4) * (5 ** 2 + 7)) #320

# num = 4321
# print("Исходное число:",num)
# a = num % 10
# print("a:",a)
# num = num // 10
# #print(num)
# b = num % 10
# print("b:",b)
# num = num // 10
# #print(num)
# c = num % 10
# print("c:",c)
# num = num // 10
# #print(num)
# d = num % 10
# print("d:",d)
# print("Обратное число:",a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print("Исходное число:",num)
# res = num % 10 * 1000 #1000
# num //= 10 #432 - целочисленное деление
# res += num % 10 * 100 #1200
# num //= 10
# res += num % 10 * 10 #1230
# num //= 10
# res += num % 10
# print("Обратное число:",res)
# print(32 % 3)

# num1 = "2"
# num2 = 3
# # res = int(num1) + num2 #5
# res = num1 + str(num2) #23
# print(res)

# print(int(3.8))
# print(round(3.8))
# print(round(3.891, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, "лет.", sep="", end=" ")
# print("Новая строка")

# name = input("Введите имя: ")
# print("Ваше имя:", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
#
# res = num ** power
# print("Число", num, "в степени", power, "равно: ", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
#
# sum1 = num1 + num2
# sum2 = num3 + num4
#
# res = sum1 / sum2
#
# print(round(res, 2))

# b1 = True
# b2 = False
# # print(type(b1))
# print(b1 + 5) #6
# print(b2 + 5) #5

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool("5"))
# print(bool("0"))
# print(bool("0.1"))
# print(bool("0.0"))
# print(bool(False))
# print(bool(None))
#
# a = None
# print(type(a))

# print(7 == 7)
# print(2 + 5 == 7)
# print(2 + 5 == 7 / 3)
# print(8 > 5)
# print(8 >= 5)
# print(9 > 9)
# print("Hello" > "HELLO") #ASCII кодировка

# print(2 < 4 < 9) # True && True => True
# print(2 * 5 > 7 >= 4 + 3) # 10 > 7 >= 7 True && True => True
# print(3 * 3 <= 7 >= 2) # 9 <= 7 >= 2 False && True => False
#
# a = 10
# b = 5
# c = a == b
# print(a, b, c)


# ///////////////////// 3 урок ////////////////////////////////

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True
#
# print(not 9 - 5)
#
# a = 5
# print("a:", a)

# cnt = 5
# print(cnt)
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 25
# b = 25
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# a = input("Введите первую сторону: ")
# b = input("Введите первую сторону: ")
# c = input("Введите первую сторону: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели цифрой: "))
#
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца цифрой: "))
#
# if month == 12 or month == 1 or month == 2:
#     print("Время года - Зима")
# elif 3 <= month <= 5:
#     print("Время года - Весна")
# elif 6 <= month <= 8:
#     print("Время года - Лето")
# elif 9 <= month <= 11:
#     print("Время года - Осень")
# else:
#     print("Некорректное значение")

# month = int(input("Введите номер месяца цифрой: "))
# if 1 <= month <= 12:
#     if month == 12 or month == 1 or month == 2:
#         print("Время года - Зима")
#     if 3 <= month <= 5:
#         print("Время года - Весна")
#     if 6 <= month <= 8:
#         print("Время года - Лето")
#     if 9 <= month <= 11:
#         print("Время года - Осень")
# else:
#     print("Некорректное значение")

# crow = int(input("Введите количество ворон на ветке от 0 до 9: "))
#
# if 0 <= crow <= 9:
#     print("На ветке ", end="")
#     if crow == 1:
#         print(crow, "ворона")
#     if 2 <= crow <= 4:
#         print(crow, "вороны")
#     if 5 <= crow <= 9 or crow == 0:
#         print(crow, "ворон")
# else:
#     print("Ошибка ввода")

# crow = int(input("Введите количество ворон на ветке от 0 до 9: "))
#
# if 0 <= crow <= 9:
#     print("На ветке ворон:", end="")
#     if crow == 1:
#         print("а", crow)
#     elif 2 <= crow <= 4:
#         print("ы", crow)
#     else:
#         print("", crow)
# else:
#     print("Ошибка ввода")
#


# password = input("Введи имя: ")
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")


# day = 'суббота'
# time = 14
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходные")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# Тернарное выражение

# a, b = 20, 20
# print(a if a < b else b)


# a, b = 30, 0
# print("На 0 делить нельзя" if b == 0 else a / b)

# //////////////4 УРОК///////////////////


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
#

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print("Результат деления: ", n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:   # Когда в блоке try не возникло исключение
#     print("Все нормально вы ввели", n, "и", m)
# finally:    # Выполняется в любом случае
#     print("Конец программы")


# mean1 = input("Введите первое значение")
# mean2 = input("Введите второе значение")
#
# try:
#     mean1 = int(mean1)
#     mean2 = int(mean2)
# except ValueError:
#     mean1 = str(mean1)
#     mean2 = str(mean2)
# finally:
#     print(mean1 + mean2)

#   Циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# print()
# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2

# n = int(input("Укажите кол-во символов: "))

# i = 0
# while i <= n:
#     print("*", end="")
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# # print("*" * n)
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("введите начало диапазона: "))
# b = int(input("введите конец диапазона: "))
#
# res = 0
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма нечетных чисел: ", res, end=" ")


# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break


# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Произведение чисел: ", res)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     # print("Внешний цикл: i =", i)
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# ///////////////////5 УРОК//////////////////////////

# for element in collection:
#   print(element)

# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)

# range(start, stop, step)

# print(range(1, 10, 2))

# for i in range(0, 10, 1):  # = for i in range(10)
#     print(i, end=" ")

# print()
# j = 1
# while j < 10:
#     print(j, end=" ")
#     j += 2
#
# print()
# for i in range(10, 0, -1):
#     print(i, end=" ")

# Необходимо вывести все число, которое введенное пользователем число делится без остатка:
# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("The end")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# print()
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")

# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list([8, 3, 9, 4, 1])
# print(num1)

# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[4])
# print(nums[-3])
# print(nums[-2])
# print(nums[-1])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums[1])
# nums[3] += 100
# print(nums[3])

# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print("Длина списка:", len(nums))

# nums = [8, 3, 9, 4, 1, "one"]
# nums2 = [11, 12, 13, "two"]
# n = nums + nums2
# print(n)
# print(n * 2)

# print(list("Hello"))
#
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))

# [выражение for переменная in последовательность]

# a = ["*" for i in range(5)]
# print(a)
#
# a = [i for i in range(5)]
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)
#
# a = [0] * int(input("n = "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите кол-во элементов списка: ")))]
# print(a)

# ///////////////////// 6 WORK //////////////////////////

# a = list(range(10, 100, 10))
# print(a)    # [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# for i in range(len(a)):
#     # print(i, end=" ")    # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")    # 12 22 32 42 52 62 72 82 92
# print()
#
# for i in a:
#     print(i, end=" ")   # 10 20 30 40 50 60 70 80 90


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
#
# print()
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# Такой вариант решения не подходит:
# for i in a:
#     if i > i - 1:    # 9 > 8, 5 > 4......
#         print(i, end=" ")


# n = list(range(21, 41))
# print(n)
# s = k = 0

# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Кол-во четных эл-тов: ", k)
# print("Сумма нечетных эл-тов: ", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# sum1 = kol = 0
#
# for i in range(len(a)):
#     if a[i] != 0:
#         kol += 1
#         sum1 += a[i]
#
# print("Среднее арифметическое: ", sum1 // kol)


# lst = [7, 9, 2, 1, 17]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# Срез
# список[start:stop:step]

# s = [9, 7, 2, 1, 17, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[::3])
# print(s[::-1])
# print(s[-1:0:-1])


# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))

# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# print(lst)
# lst[15:16] = [100]
# print(lst)
# print(len(lst))
# lst[13:14] = [500]
# print(lst)

# Методы списков //////////////////////////


# lst = list(range(1, 8))
# print(lst)
#
# lst.append(99)  # Добавляет эл-т в конец списка
# print(lst)
# lst.extend([1, 2, 3])   # Добавляет список эл-тов в конец списка
# print(lst)
# lst.insert(1, 100)  # Добавляет эл-т по заданному индексу, где сам индекс 1 параметр, а элемент - 2 параметр
# print(lst)


# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)
#
# a = [1, 3, 5, 6, 2, 4, 6127]
# b = [4, 2, 1, 3, 7]
# c = []

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break

# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7, 2]
# b = []
#
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         b.append(a[i])
#
# print(b)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7, 2]
# a = ["red", "yellow", "green"]
# b = []
#
# for i in a:
#     if a.count(i) == 1:
#         print(i, end=" ")
#
# print()
#
# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         print(a[i])

# a = [1, 2, 3, 7, 3, 1, 33]
# b = [11, 22, 33]
# c = []
#
# # if len(b) > len(a):
# #     for i in range(len(a)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(a), len(b)):
# #         c.append(b[i])
# #
# # else:
# #     for i in range(len(b)):
# #         c.append(a[i])
# #         c.append(b[i])
# #     for i in range(len(b), len(a)):
# #         c.append(a[i])
# #
# # print(c)
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)
#

#
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22]
# #
# lst[5:] = []
# print(lst)
# lst[3:5] = []
# print(lst)
# del lst[2]
# print(lst)
# del lst[3:5]
# print(lst)
#
# lst.remove(22)
# print(lst)

# last = lst.pop()
# print(last)
#
# last = lst.pop()
# second = lst.pop(0)
# print(second)
# print(lst)
#
# lst.clear()
# print(lst)

# print("Введите элементы списка")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 22, 33]
# value = 33
# if value in lst:
#     ind = lst.index(value, 5)
#     print(ind)
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# a = lst.copy()
# print(lst, id(lst))
# print(a, id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst)
# print(a)

#
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# # lst.reverse()
# # print(lst)
#
# lst.sort(reverse=True)
# print(lst)
#
# new_lst = sorted(lst, reverse=True)
# print(new_lst)
#


# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len)
# print(s)

# Генерация случайных данных

#
# import random

# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(10))
# print(random.randrange(5, 10, 2))
#
# print(random.uniform(10.5, 20.5))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
#
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)


# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# max_val = max(mas)
# print("Максимальный элемент:", max_val)
# mas.remove(max_val)
# mas.insert(0, max_val)
# print(mas)

# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 in mas)
# print(3 in mas)

# lst = []
# # if len(lst) == 0:
# #     print("Spisok pustoy")
# print(bool(lst))
#
# if not lst:
#     print("Spisok pustoy")
# else:
#     print("Est' elements")


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1])
# print(m[2][1])

# print("Var1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# print("Var2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print(m)


# МОДУЛИ

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import sqrt, ceil, floor
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# import math
# print(dir(math))

# from math import pi
#
# # print(pi)
#
# rad = int(input("Radius = "))
# print("L = ", round(2 * pi * rad, 2))
#
# import time
# # import locale
# #
# # print(time.time())
# # print(time.ctime(3600))
# # res = time.localtime()
# # print(res.tm_year, "0-", res.tm_mon, "0-", res.tm_mday, sep="")
# # print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S"))
# # locale.setlocale(locale.LC_ALL, "ru")
# # print(time.strftime("Сегодня: %B %d %A, %Y"))
#
# start = time.monotonic()
# pause = 5
# print('Программа запущена')
# time.sleep(pause)
# result = time.monotonic() - start
# print('Программа выполнена за', result, 'секунд')
#
# a = 500
# for i in range(a, -1, -1):
#     time.sleep(1)
#     print()


# Функции

#
# def hello(name, age):
#     print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")

# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
#
# res = get_sum(x, y)
# print(res)


# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 16))


# def raz(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print("Результат: ", raz(a, b))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_first_big(10, 5))
# # print(is_first_big(10, 15))
#
# a = int(input("a = "))
# b = int(input("b = "))
# if is_first_big(a, b):
#     print("a > b")
# else:
#     print("b > a")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Надежный пароль")
# else:
#     print("Ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def display_info(name, age):
#     print("Name", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23)


# ////////////////////10 Занятие//////////////////////////////////

# def func(a, b):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))

# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))

#  tuple() - Кортеж()

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# print(lst)

# a = (1, 2, 3, 4, 5)
# print(a, type(a))

# a = tuple("Hello")
# print(a, type(a))
#
# a = (1, 2, 3, 4, 5)
# print(a[2])
# print(a[1:3])

# from random import randint
#
# print(tuple(randint(0, 5) for i in range(10)))
#
# # print(tuple(input("->") for i in range(5)))
#
# print(tuple(randint(50, 100) for i in range(10)))

# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2
# # print(t3 * 2)
# print(t3)
# # print(len(t3))
#
# print(t3.count('l'))
# print(t3.index('l', 4))

#
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (True, 11, "Python", (4, 5, 6), ["Hello", "World"])
# print(t, id(t))
# t[4][0] = 'New'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# РАСПАКОВКА КОРТЕЖА
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, year, married = user

# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
#
# # print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# print(lst)
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))

# set - Множество

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s)
# print(type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))
#
# s = {i for i in range(10)}
# print(s)
#
# lst = [10, 2, 2, 2, 2, 3, 5, 8, 8, 9, 9, 9]
# # st = {i for i in lst if i % 2 == 0}
# # print(st)
# st = set(lst)
# print(st)
# lst2 = list(st)
# print(lst2)
#
# t = {'red', 'yellow', 'green'}
# print("green" in t)
# print("blue" in t)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if 'a' in i])
# print(tuple(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"]))
# print(["A" + i[1:] if i[0] == "a" else "B" + i[1:] for i in lst if i[1] == "c"])
#

# print(dir(set))

# a = {'red', 'yellow', 'green'}
# print(a)
# a.add('black')
# print(a)

# a.remove('yellow')
# print(a)

# el = 'blue'
# if el in a:
#     a.remove(el)
#
# print(a)

# a.discard('yellow')
# print(a)
#
# a.pop()
# print(a)
#
# a.clear()
# print(a)

#
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a | b
# # print(c)
# # a |= b
# # print(a)
# #
# # c = a & b
# # print(c)
# # a &= b
# # print(a)
# #
# # c = a - b
# # print(c)
# a -= b
# print(a, type(a))
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print("Кол-во уникальных элементов: ", len(s))
# print("Min: ", min(s))
# print("Max: ", max(s))

# s1 = "Hello"
# s2 = "How are yoy"
#
# a = set(s1) & set(s2)
# print(a, type(s1))
# #
# for i in a:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)
#
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({"hello", "world"})
# print(a)

# dict - словарь

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst[1])
# lst[1] = "ten"
# print(lst)
#
# d["second"] = "ten"
# print(d)

# d = dict(a="hello", b="world")
# print(d)
# print(type(d))
#
# d1 = {"a": "Hello", "b": "World"}
# print(d1)

# d = {0: "text", "one": 1, (1, 2): [2, 3, 4, 5], 42: [9, 8], True: 1, False: 0}
# print(d)


# user = [
#     ["a", 1],
#     ["b", 2],
#     ["c", 3]
# ]
#
# print(user)
# new_dict = dict(user)
# print(new_dict)
#
# # 12 Занятие
#
# d = {i: i ** 2 for i in range(1, 8)}
#
# print(d)
#
# # print(3 in d)
# # print(25 in d)
#
# key = 9

# if key in d:
#     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключем", key, "нет в словаре.")
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# res = 1
#
# for key in d:
#     res *= d[key]
#
# print(res)

# d = dict()
#
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)
#
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент удалить: "))
# del d[dislike]
# print(d)
#
#
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Введите кол-во: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб.", sep="")

# Методы словарей

# d = {"A": 1, "B": 2, "C": 3}
#
# print(d)
#
# # print(d.keys())
# # print(d.values())
# # print(d.items())
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {"A": 1, "B": 2, "C": 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d2["B"] = 5
# print("D =", d)
# print("D2 =", d2)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # d.clear()
# # item = d.pop("M", "Такого ключа нет")
# item = d.popitem()
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# print(d)
# # # print(d["B"])
# # val = d.get("W", "Такого ключа нет")
# # print(val)
# item = d.setdefault("W", 5)
# print(d)
# print(item)

# d = {"A": 1, "B": 2, "C": 3}
# # d2 = {"R": 7, "Q": 9, "B": 5}
# d2 = [("R", 7), ("Q", 9)]
# print(d)
# print(d2)
# # d3 = d | d2
# d.update(d2)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}

# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d['name'], new_d['salary'] = d.pop('name'), d.pop('salary')
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d['location'] = d.pop('city')
#
# print(d)

# d = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(d)
#
# # for x in d:
# #     print(x)
# #     for y in d[x]:
# #         print("\t", y, ": ", d[x][y], sep="")
#
#
# for x, y in d.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")


# //////////////////13 UROK////////////////


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({val: key for key, val in d.items()})
# print({key: val for key, val in d.items() if val <= 2})

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {i: i*3 for i in s}
# print(d1)

# lst = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# s = None
#
# for i in lst:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)
#
# d1 = list(zip([1, 2, 3], ['one', 'two', 'three'], [True, False, True]))
# print(d1)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = {key: val for key, val in zip(a, b)}
# print(d)

# a = [1, 2, 3]
# c = list(zip(a))
# print(c)

# one = {"name": "Igor", "surname": "Pavlov", "job": "Consultant"}
# two = {"name": "Irina", "surname": "Vetrova", "job": "Manager"}
#
# for (key1, val1), (key2, val2) in zip(one.items(), two.items()):
#     print(key1, "->", val1)
#     print(key2, "->", val2)

# lst = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*lst)
# print(a)
# print(b)

# letter = ['b', 'a', 'd', 'c']
# number = [3, 4, 1, 2]
# d = dict(zip(letter, number))
# print(d)
#
# data = sorted(zip(letter, number))
# print(data)

# data1 = list(zip(letter, number))
# print(data1)
# data1.sort()
# print(data1)
#
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(number, letter))
# print(data2)
# data2.sort()
# print(data2)
#
# d3 = {val: key for key, val in data2}
# print(d3)

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# one = {"один": 1, "два": 2}
# two = {"три": 3, "четыре": 4}
# print({**one, **two})

# colors = ['red', 'yellow', 'green']
# i = 1
# for color in colors:
#     print(i, ") ", color, sep="")
#     i += 1
# print()
#
# for j, color in enumerate(colors, 1):
#     print(j, ") ", color, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3))

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(5, 6))
# print(func(1, 2, 3, 4, 5))

# def scores(student, *score):
#     print("Student Name: ", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 5, 5, 4, 3, 3, 5)
# scores("Ivan", 4, 3, 3)
#
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(st="python"))


# def info(**data):
#     for key, val in data.items():
#         print(key, ":", val)
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone=456789, age=22, email="Igor@mail.ru")


# ///////////////14 UROK///////////////

# def func1(*args):
#     print("args", args)
#     print(args[0])
#
#
# def func2(**kwargs):
#     print("kwargs", kwargs)
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5, 6)
# func2(one=123, two=456)

# name = "Tom"    # Глобальная область видимости
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson"  # Локальная область видимости
#     print("Hello, ", name, surname)
#
#
# def bye():
#     print("Good bye, ", name)

#
# hi()
# bye()
# print(name)

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# sum_ = 5
#
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(sum(lst))

# x = 4


# def func():
#     x = 2
#
#     def inner():
#         print("x =", x)
#         print(x + 3)
#
#     inner()
#
#
# func()

# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")
#
#
# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Summa: ", a + b)
#
#     print("a: ", a)
#     fun2(3)
#
#
# fun1()

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a: ", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x = ", x)
#
#     fn2()
#     print("fn1.x = ", x)
#

# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))

#   Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# func1 = outer(5)
# print(func1(10))
#
# func2 = outer(6)
# print(func2(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         c.append(4)
#         nonlocal a, b
#         a += 1
#         b += '!'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     n = 0
#
#     def inner():
#         nonlocal n
#         n += 1
#         print(city, n)
#
#     return inner

#
# res1 = func("Moscow")
# res1()
# res1()
# res1()
# res1()
# res2 = func("Sochi")
# res2()
# res2()
# res1()


# /////////////////////14 UROK/////////////////////////////

# Анонимные фугкции (lambda)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
#
# print(func(1, 2))
#
# func = (lambda x, y: x + y)(1, 2)
# print(func)

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4))
# print((lambda *args: max(args))(1, 2, 3, 4))

# tpl = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for func in tpl:
#     print(func("abc___"))

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(42)
# print(f(3))

# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(42)
# print(f(3))
#
#
# outer = lambda n: lambda x: n + x
# f = outer(42)
# print(f(3))

# print((lambda n: lambda x: n + x)(42)(3))

# print((lambda a: lambda b: lambda c: a + b + c)(2)(4)(6))

# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

#
# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)


# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
# print(lst[0](12, 6))
# print(lst[1](12, 6))
# print(lst[2](12, 6))
# print(lst[3](12, 6))
#
# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[2]()

# print((lambda a, b: a if a > b else b)(5, 13))

# from random import randint
# print((lambda lst: [i * 2 for i in lst])([1, 2, 3, 4, 5, 6]))
#
# print((lambda lst: [randint(10, 20) for i in range(10)])([]))


# map(function, iterables), filter(function, iterables)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(tuple(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
# print(list(map(lambda t: t * 2, lst)))

# t = (2.88, -1.75, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))
# print(tuple(map(round, t)))
# print(tuple(map(str, t)))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# tpl = (True, False, False, True, True)
#
# print(dict(map(lambda k, v: (k, v), st, num)))
# print(list(map(lambda k, v: (k, v), st, num)))
#
# print(list(map(lambda a, b, c: a + str(b) + str(c), st ,num, tpl)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda a, b: a + b, l1, l2)))

# lst = [input("->") for i in range(5)]
# print(lst)
# lst = list(map(int, lst))
# print(lst)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))
# print(tuple(filter(lambda s: s * 3, t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# lst1 = list(filter(lambda s: s > 75, lst))
# print(lst)
# print(lst1)

# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# print(list(filter(lambda a:( a >= 10) and a <= 20, lst)))
# print(list(filter(lambda a: 10 <= a <= 20, lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print([x ** 2 for x in range(10) if x % 2])


# ///////////16 UROK///////////////////

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print("Code do vizova")
#         func()
#         print("Code posle vizova")
#
#     return func_wrapper
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")


# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def func_wrapper():
#         print("Code do vizova")
#         func()
#         print("Code posle vizova")
#
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "<b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "<i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов ф-ции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(args1, args2):
#         print("Data:", args1, args2)
#         fn(args1, args2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("My name is", first, last)
#
#
# print_full_name("Aleksandr", "Vasiliev")
#
# def outer(fn):
#     def inner(*args, ** kwargs):
#         print("args: ", args)
#         print("kwargs: ", kwargs)
#         fn(*args, ** kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "study", study, end="\n\n")
#
#
# print_data("Boris", "Lisa", "Svetlana", study="JS")
# print_data("Vladimir", "Ekaterina", "Viktoria")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
# @decor("Summa", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Raznost", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def mulyiply(arg):
#     def my_decorator(func):
#         def wrap(*args, ** kwargs):
#             return arg * func(*args, ** kwargs)
# 
#         return wrap
#     return my_decorator
# 
# 
# @mulyiply(3)
# def return_num(num):
#     return num
# 
# 
# print("Answer: ", return_num(5))


#   Строки

# print(bin(3))
# print(hex(18))
# print(0b10010)
# print(0b10010 + 0x12 + 4)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# print("y" in e)
# print(e[1])
# print(e[1:3])


# def chang_char_to_str(s, old, new):
#     s2 = ""
#
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = chang_char_to_str(str1, "N", "P")
#
# print(str1)
# print(str2)


# print(u"Hello")
# print("Hello")

#
# print("C:\\file.txt\\")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")

# ///////////////////// 17 UROK ////////////////////////////////////////


# print(b"a1b2v2")

# name = "Alex"
# age = 25
# print("My name is ", name, ". I'm ", age, " age.", sep = "")
# print("My name is " + name + ". I'm " + str(age) + " age.")
# print(f"My name is  {name}. I'm  {age} age.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
#
# print(f"{x} x {y} / 7 = {round(x * y / 7, 2)}")
# print(f"{x} x {y} / 7 = {x * y / 7:.2f}")

# num = 74
# print(f"{{{num}}}")
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)

# st = ("Однострочный "
#       "текст")
# print(st)
#
# s = """Многострочный
# текст"""
# print(s)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)


# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(val) for val in st]
# print("ASCII коды:", arr)
#
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
#
# arr += [ord(val) for val in input("-> ")[:3] if ord(val) not in arr]
# print(arr)
#
# print(arr.count(arr[-1]) - 1)
#
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))
# print(chr(456))

#
# a = 122
# b = 97
#
# if a > b:
#     for val in range(b, a + 1):
#         print(chr(val), end=" ")
# else:
#     for val in range(a, b + 1):
#         print(chr(val), end=" ")
#

# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     result = ""
#     for val in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())
# print(s.lower())
# print(s.upper())

# print(s.count("h")) # h = 2
# print(s.count("h", 1))  # h = 1
# print(s.count("h", 1, - 4))    # h = 0
# print(s.lower().count("i"))

# print(s.find("Python"))
# print(s.find("h"))
# print(s.find("h", 1))
# print(s.find("h", 1, - 4))
# print(s.rfind("h"))
#
# print(s.index("h"))
# print(s.rindex("h"))

# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ") + 1:]
# res = two + " " + one
# print(res)
# print(st[st.find(" ") + 1:] + " " + st[:st.find(" ")])
#
# s = "hello, WORLD! I am learning Python."
# # print(s.startswith("hello"))
# # print(s.startswith("I am", 14))
# # print(s.startswith("I am"))
#
# print(s.endswith("Python."))

# print("abc123".isalnum())   # состоит ли строка из букв и цифр
# print("abc!123".isalnum())
# print("123".isalnum())
#
# print("ABCabc".isalpha())   # состоит ли строка из букв

# print("123".isdigit())  # состоит ли строка и цифр

# print('aab'.islower())  # есть ли в строке буквы в нижнем регистре
# print('SDS'.islower())  # есть ли в строке буквы в верхнем регистре

# print("py".center(10))
# print("py".center(10, "-"))
#
# print("     py".lstrip())
# print("py     ".rstrip())
# print("     py     ".strip())
#
# print("https://www.python.org".lstrip("/:htps"))
# print("https://www.python.org.www".lstrip("/:htps").rstrip(".w"))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("N", "P"))

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '99']))
#
# print(":".join("Hello"))


# ////////////////////   18 UROK //////////

# print("Строка разделенная пробелами".split())
# print("www.python.org".split(".", 1))

# s = input("Введите ФИО: ").split()
# print(s)
# print(f"{s[0]} {s[1][0]}. {s[2][0]}.")

# s = input("Введите набор чисел через пробел: ").split()
# print(s)
# num = list(map(int, s))
# print(sum(num))

# Регулярные выражения

# import re


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# print(dir(re))

# reg = r"\."
# print(re.findall(reg, s))   # возвращает список с шаблоном
# print(re.search(reg, s))
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.split(reg, s))  # Возвращает список, который разбит по заданному шаблону
# print(re.sub(reg, "!", s))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld"

# reg = r"[205]"
# reg = r"[1-2][0-9][0-9][0-9]"
# print(re.findall(reg, s))

# reg = r"[А-яЁё.\[\]-]"
# reg = r"[A-Za-z]"
# reg = r"[^0-9]"
# print(re.findall(reg, s))


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты в диапазоне от 00 до 59. 2021-06-15T01:09"
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld"

# reg = r"\d"
# reg = r"\D"
# reg = r"\s"
# reg = r"\S"
# reg = r"\w"
# reg = r"\W"
# reg = r"\AЯ ищу"
# reg = r"Wor-ld\Z"
# reg = r"ния\b"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения

#
# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# st = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s#.+", "", st))
# print(re.sub(r"\s#.+", "", st))
#
# print("Дата рождения:", re.sub("-", ".", st))
# print("Дата рождения:", re.sub(r"\s#.+", "", re.sub("-", ".", st)))
#
#
# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w*\.?\w*\.?"
# # reg = r"\w+\s*=\s*\w+[\s\w\.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s", st))

# st = "12 сентября 2025 год 456 789456123"
# # reg = r"\d{4}"
# reg = r"\d{2,4}"
# # reg = r"\d{,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))


# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel_lo] Wor-ld 20000000000"
#
# reg = r"^\w+\s\w+"
# # reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[a-zA-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt45_"))


#///////////////////// 19 UROK ////////////////////////////

import re

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
#
# text = "hello world"
# print(re.findall(r"\w+", text))
# print(re.findall(r"\w+", text, re.DEBUG))

# text = "helLo worLd"
# print(re.findall(r"l", text, re.IGNORECASE))

# text = """
# one
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+    # part1
# @   # @
# [a-z.]+     # part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python
# PYTHON
# """
#
# reg = "(?im)^python"
# print(re.findall(reg, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
#
# st = "12 сентября 2025 год 456 789456123"
# # # reg = r"\d{4}"
# # reg = r"\d{2,4}?"
# # reg = r"\d{,4}?"
# reg = r"\d{4,}?"
# print(re.findall(reg, st))

# s = "Петр, Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга|Виталий|Василий"
# print(re.findall(reg, s))
#
# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"int\s*=\s*\d[\w.]*|float\s*=\s*\d[\w.]*"
# reg = r"(?:int|float)\s*=\s*\d[\w.]*"
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE))

# s = "5 + 7*2 - 4"
# reg = r"\s*[+*-]\s*"
# print(re.split(reg, s))
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# s = "18-08-2021"
# reg = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s))
# print(re.search(reg, s).group())

# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d+)"
# print(re.findall(reg, s, re.IGNORECASE))
# print(re.search(reg, s, re.IGNORECASE).group())
# m = re.search(reg, s, re.IGNORECASE)
# print(m[1])
# print(m[2])
# print(m[0])
#
# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# РЕКУРСИЯ


# def elevator(n):
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for val in lst:
#         res += val
#     return res

# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, "=>lst[0]", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=>lst[0]", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))
#
# names = ['Adam', ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names)
# print(len(names))
# print(names[0])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names1 = ['Adam', ["Bob", ["Chet", "Cat"], "Barb", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else: count += 1
#     return count
#
#
# print(count_items(names1))

# print("Текст в локальном репозитории")

print("Код написан на новом устройстве")

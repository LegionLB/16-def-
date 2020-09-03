import math


# 1=================================================
#a_list = [1,2,3,4]
# def f_sum(a):
#     sum = 0
#     for i in a:
#         sum += i
#     return sum
# print(f_sum(a_list))

# def w_sum(a):
#     sum = 0
#     while a:
#         sum = sum + a.pop()
#     return sum
# print(w_sum(a_list))

# def recursion(work_list,sum = 0):
#     if work_list:
#         sum += work_list.pop()
#         return recursion(work_list, sum)
#     else:
#         print(sum)
#         return sum
# recursion(work_list=a_list)

#2==============================================
#[1,2,3] +[11,22,33] --> [1,11,2,22,3,33]


# a_list = [1,2,3]
# b_list = [11,22,33]
# c_list = []
# def func(a,b):
#     for i in range(len(a)):
#         c_list.append(a[i])
#         c_list.append(b[i])
#     return c_list
# print(func(a_list, b_list))


#3==============================================
# IS triangle?

# a_l = int(input("Введите сторону А:"))
# b_l = int(input("Введите сторону В:"))
# c_l = int(input("Введите сторону С:"))
#
# def func_t(a,b,c):
#     if (a + b) > c:
#         print("Cуществует")
#     elif (c + a) > b:
#         print("Cуществует")
#     else:
#         print("Не существует")
# print(func_t(a_l, b_l, c_l))

#4=============================================
# Earth distance

# x = float(input('Введите координаты широты точки А: '))
# x1 = float(input('Введите координаты долготы точки А: '))
# y = float(input('Введите координаты широты точки В: '))
# y1 = float(input('Введите координаты долготы точки В: '))
#
# def func(a, b, a1, b1):
#
#     R = 6371
#     a_tuple = (a, a1)
#     b_tuple = (b, b1)
#
#     d = math.sin(a) * math.sin(a1) + math.cos(a) * math.cos(a1) * math.cos(b - b1)
#     d = math.acos(math.cos(d))
#     L = d * R
#     L = L/10
#     return L
#
# print(func(x,x1,y,y1))


#5===========================================================
#discr

# x = int(input('Введите начало диапазона "a" : '))
# x1 = int(input('Введите конец диапазона "a" : '))
# y = int(input('Введите начало диапазона "b" : '))
# y1 = int(input('Введите конец диапазона "b" : '))
# d = int(input('Введите начало диапазона "с" : '))
# d1 = int(input('Введите конец диапазона "с" : '))
#
# def discr(a, a1, b, b1, c, c1):
#     a_list = []
#     b_list = []
#     c_list = []
#
#     for i in range(a, a1 + 1):
#         for dis in range(b, b1+1):
#             for dis2 in range(c, c1+1):
#                 D = dis ** 2 - 4 * i * dis2
#                 if D > 0:
#                     a_list.append(D)
#                     print('Дискриминант равен -' , [D] , 'Cуществуют вещественные корни, график квадратичной функции пересекает ось Х в двух местах.')
#                 elif D < 0:
#                     b_list.append(D)
#                     print('Дискриминант равен -' , [D] ,'Не существует вещественных корней, а только комплексные корни. График функции не пересекает ось Х.')
#                 else:
#                     c_list.append(D)
#                     print('Дискриминант равен -' , [D] ,'Cуществует один вещественный корень, график функции пересекает ось Х в одном месте.')
#                 print(a_list,b_list,c_list)
#                 return a_list, b_list, c_list
# print(discr(x,x1,y,y1,d,d1))

#6==================================================
# replace "?"--->"*"

# a_list = []
# b_list = ['pip????', '???']
# def replace(a):
#     str = int(input('Input a count of strokes: '))
#     for i in range(str):
#         a_str = input('Input a stroke or strokes: ')
#         a.append(a_str.replace('?', '*'))
#         return a
# print(replace(b_list))

#7==================================================
#2009-06-15 -----> 15/06/2009

# date = '2009-06-15'
# def reverse(a):
#     formated = '{}/{}/{}'
#     a_list = a.split('-')
#     a_list.reverse()
#     d = formated.format(a_list[0], a_list[1], a_list[2])
#     return d
# print(reverse(date))

#8===================================================
#gr --->tons, kilo

# weight = int(input('Input weight in Gr: '))
# def transform(a):
#     a_copy = a
#     b = a / 1000
#     c = a_copy / 10000
#     return b, c
# print('Your weght in kilos and tons: ', transform(weight))

#9===================================================
# can the box pass the door?

# a_box = int(input("Введите высоту коробки: "))
# b_box = int(input("Введите ширину коробки: "))
# c_box = int(input("Введите длинну коробки: "))
# def door_pass(a, b, c):
#     a_d = 90
#     b_d = 50
#     if a < a_d and b < b_d:
#         print("Коробка пройдёт.")
#     elif c < a_d and b < b_d:
#         print("Коробка пройдёт.")
#     else:
#         print("Нет")
#     return
# door_pass(a_box, b_box, c_box)

#10======================================
#Cube inside the block of wood

# a_block = int(input("Введите ширину бруса: "))
# b_block = float(input("Введите диаметр бревна: "))
# def make_a_cube(a, b):
#     c = math.sqrt(a*a*2)
#     if c<=b:
#         print("Можем")
#     else:
#         print("Нет")
#     return
# make_a_cube(a_block, b_block)


#11======================================
# Vagon

# print('Стандартный вагон имеет 54 места.')
# a_place = int(input('Введите номер в плацкартном вагоне для определения места: '))
#
# def find_a_place(a):
#     if a <= 54 and a != 0 and a > 0:
#         if a > 36 and a %2 == 0:
#             print('Ваше место верхнее и боковое!')
#         elif a <= 36 and a %2 == 0:
#             print('Ваше место верхнее и в купе!')
#         elif a <= 36 and a %2 != 0:
#             print('Ваше место нижнее и в купе!')
#         elif a > 36 and a %2 != 0:
#             print('Ваше место нижнее и боковое!')
#     else:
#         print('Вы ввели неверное место в вагоне.')
#         return
# find_a_place(a_place)

#12===================================================
#Exchange your money ( only 500,100,10,2)


# money = int(input('Введите данные для размена купюрами 500,100,10 и 2: '))
# def exchange(money_input):
#     m500 = 0
#     m100 = 0
#     m10 = 0
#     m2 = 0
#     if money_input > 0:
#         money_output = money_input
#         m500 = money_output / 500
#         money_output = money_output % 500
#         m100 = money_output / 100
#         money_output = money_output % 100
#         m10 = money_output / 10
#         money_output = money_output % 10
#         m2 = money_output / 2
#         money_output = money_output % 2
#         m500 = math.floor(m500)
#         m100 = math.floor(m100)
#         m10 = math.floor(m10)
#         m2 = math.floor(m2)
#         print('Полученные купюры при обмене', money_input, ':''\n', m500, 'купюр - по 500грн''\n', m100, 'купюр - по 100грн''\n', m10, 'купюр - по 10грн'
#               '\n', m2, 'монет - по 2грн')
#         if money_output > 0:
#             print("Разменный пункт не смог разменять эти деньги -->", money_output, 'грн')
#         else:
#             print('Работа разменного пункта завершена.')
#     else:
#         print('Введены неверные данные!')
#     return
# exchange(money)

#13=========================================================
#simple num or not?

#14=========================================================
#tabl(*) from a till b

# a = int(input('input start: '))
# # b = int(input('input end: '))
# # c = int(input('input num "*": '))
# # def show_me(num_1, num_2, num_mnoj):
# #     for i in range(num_1, num_2 + 1):
# #         print('{} * {} = {}'.format(num_mnoj, i, num_mnoj*i))
# #     return
# #
# # show_me(a, b, c)


#15==============================================
#A[1] --> A[2], A[3] ---> A[4]
#??????????????????????????????????????????????????
#########################################################
#16==============================================
#??????????????????????????????????????????????















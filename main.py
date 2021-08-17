# 1)Дан лист:
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 22, 3, 5, 2, 8, 2, 32424, 343434, 5434, 2]
#  - найти min число в листе
# list.sort()
# print(list[0])
#  - удалить все дубликаты в листе
# list.reverse()
# i = 0
# while i == 0:
#    for item in list:
#        if list.count(item) > 1:
#            list.remove(item)
#            print(list)
#            if i == 0:
#                i -= 1
#    i += 1
# list.reverse()
# print(list)
#  - заменить каждое четвертое значение на "Х"
# i = 1
# while i <= len(list):
#    if (i % 4 == 0):
#        list[i - 1] = "X"
#    i += 1
# print(list)
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# w = int(input('Enter width: '))
# h = int(input('Enter height: '))-1
# if h > 0:
#    print('*' * w)
#    for i in range(h):
#        if i != h - 1:
#            print('*', '*', sep=' ' * (w - 2))
#        else:
#            print('*' * w)
#
# 3) вывести табличку умножения с помощью цикла while
# h = 1
# while h < 10:
#     w = 1
#     while w < 10:
#         item = w * h
#         if (w < 9):
#             print(item, end='')
#             if (len(str(item)) == 1):
#                 print('  ', end='')
#             else:
#                 print(' ', end='')
#         else:
#             print(item)
#         w += 1
#     h += 1

# 4) переделать первое задание под меню с помощью цикла
#
# list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5, 22, 3, 5, 2, 8, 2, 32424, 343434, 5434, 2]
# index = 0
#
# while index == 0:
#     print('1 - найти min число в листе')
#     print('2 - удалить все дубликаты в листе')
#     print('3 - заменить каждое четвертое значение на "Х"')
#     print(
#         '4 - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа')
#     print('6 - выход')
#     num = int(input('ваш выбор: '))
#     if (num == 1):
#         list.sort()
#         print(list[0])
#     elif (num == 2):
#         list.reverse()
#         i = 0
#         while i == 0:
#             for item in list:
#                 if list.count(item) > 1:
#                     list.remove(item)
#                     if i == 0:
#                         i -= 1
#             i += 1
#         list.reverse()
#         print(list)
#     elif (num == 3):
#         i = 1
#         while i <= len(list):
#             if (i % 4 == 0):
#                 list[i - 1] = "X"
#             i += 1
#         print(list)
#     elif (num == 4):
#         list = [-10, 5, 5]
#
#         sum = 0
#         for i in list:
#             sum += i
#         avg = round(sum / len(list))
#
#         arr_comparison = []
#         for i in list:
#             comparison = avg - i
#             arr_comparison.append(comparison if comparison > 0 else comparison * -1)
#
#         sorted_arr_comparison = arr_comparison.copy()
#         sorted_arr_comparison.sort()
#         min = sorted_arr_comparison[0]
#         index_of_chosen = arr_comparison.index(min)
#         chosen = list[index_of_chosen]
#         print(chosen)
#     elif (num == 6):
#         index += 1


# ***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
# list = [-10, 5, 5]
#
# sum = 0
# for i in list:
#     sum += i
# avg = round(sum / len(list))
#
# arr_comparison = []
# for i in list:
#     comparison = avg - i
#     arr_comparison.append(comparison if comparison > 0 else comparison * -1)
#
# sorted_arr_comparison = arr_comparison.copy()
# sorted_arr_comparison.sort()
# min = sorted_arr_comparison[0]
# index_of_chosen = arr_comparison.index(min)
# chosen = list[index_of_chosen]
# print(chosen)

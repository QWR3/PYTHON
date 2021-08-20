# Vitaliy Demchyshyn, [18.08.21 21:32]
# print('1234'.split('')) # да это меня с js ушторило, если вам нужно разбить на символы строку то используйте list('1234')  или [i for i in '123']
#
# + по строкам можете итерироватся  обращатся по индексу и делать срезы
# print('asd'[-1])
# print('asd'[0])
# print('name'[::2])
# #ДЗ
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = input('введите строку : ')
# result = [int(i) for i in st if i.isdigit()]
# print(str(result).strip('[]'))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = input('введите строку : ')
# # st = 'as 23 fdfdg544 34'
# result = ''
# arr = []
# i = 0
# while i < len(st):
#     start_index = int()
#     end_index = int()
#     if st[i].isdigit():
#         print('start', i, st[i])
#         start_index = i
#         while True:
#             next_i = i + 1
#             if next_i < len(st) and st[next_i].isdigit():
#                 print('while', next_i, st[next_i])
#                 end_index = next_i
#                 i = next_i
#             else:
#                 i = next_i
#                 break
#
#         print(start_index, end_index, 'start-end')
#         arr.append(st[start_index:end_index+1])
#     i += 1
# print(arr)
# БАГОДЕЛНЯ РОБОТАЕТ!
# #################################################################################
#
# list comprehension
#
# 1)есть строка:
greeting = 'Hello, world'


# записать каждый символ в лист поменяв его на верхний регистр
# пример:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting_to_uppercase = greeting.upper()
# print(list(greeting_to_uppercase))

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# print([pow(i, 2) for i in range(50)])


# function
#
# - створити функцію яка виводить ліст
# def f(arr):
#     print("list", list(), arr)
#
#
# f(['list'])


# - створити функцію яка приймає три числа та виводить та повертає найменьше.
# def f(a, b, c):
#     print(min([a, b, c]))
#     return (min([a, b, c]))
#
#
# f(3, 2, 1)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# def f(a, b, c):
#     print(max([a, b, c]))
#     return (max([a, b, c]))
#
#
# f(3, 2, 1)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def f(*args):
#     print(max(args))
#     return min(args)
#
#
# f(3, 2, 1)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def f(arr=[1, 2, 3]):
#     print(sum(arr) / len(arr))
#
#
# f([3, 2, 1])
#
# decorators
# - є функція:
# def pr():
#     return 'Hello_boss_!!!'


#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
#
def decor(f):
    def inner(*args, **kwargs):
        item = f(*args, **kwargs)
        item_replace = item.replace('_', ' ')
        return (item_replace)

    return inner


@decor
def pr():
    return 'Hello_boss_!!!'


result = pr()
print(result)

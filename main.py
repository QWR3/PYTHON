# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# def funk():
#     list_of_todo = ["toDo"]
#
#     def add_todos(todo):
#         nonlocal list_of_todo
#         list_of_todo.append(todo)
#
#     def get_todos():
#         return list_of_todo
#
#     return add_todos, get_todos
#
#
# res = funk()
#
# res[0]('подтянуть английский')
# res[0]('обновить ubuntu touch на телефоне')
# res[0]('установить GNU debian 11, с ручной розметкой диска')
# res[0]('посмотреть лекцию')
# res[0]('сделать ДЗ с програмирования')
# print(res[1]())

# 2) протипизировать первое задание
# from typing import List, Tuple, Optional
#
#
# def funk() -> Optional[Tuple]:
#     list_of_todo: List[str] = ["toDo"]
#
#     def add_todos(todo: str):
#         nonlocal list_of_todo
#         list_of_todo.append(todo)
#
#     def get_todos() -> List[str]:
#         return list_of_todo
#
#     return add_todos, get_todos
#
#
# res = funk()
#
# res[0]('подтянуть английский')
# res[0]('обновить ubuntu touch на телефоне')
# res[0]('установить debian 11, с ручной разметкой диска')
# res[0]('посмотреть лекцию')
# res[0]('сделать ДЗ по програмирования')
# print(res[1]())
# 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.
# list_ = [1, 15, 30, 45, 34, 546, 600, 1000]
# filter_list = list(filter(lambda x: not x % 15, list_))
# print(filter_list)


#
# 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# Пример:
# summ(7) -> 7+77+777=861
def sum_(num: int) -> int:
    res = num + int(str(num) * 2) + int(str(num) * 3)
    print(res)
    return res


sum_(7)

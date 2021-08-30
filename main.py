# мучить вас сильно не буду
# просто разберите лекцию
#
# и переделайте это задание:
#
# Создать класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в переменной класса
# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты
#
# но в этот раз данные записываем в файл

import json


class Book:
    try:
        file = open('book.json', 'r+')
    except FileNotFoundError as e:
        print('файл не найден')
        print('создаем новый файл')
        file = open('book.json', 'w+')
    finally:
        if file.read() == '':
            file.write('{}')
        file.close()

    file = open('book.json', 'r+')
    records = json.load(file)

    def __str__(self):
        return str(self.records)

    def get_book(self):
        return str(self.records)

    def add_record(self, name: str, price: int):
        self.records = {**self.records, name: price}

    def sum(self):
        sum = 0
        for name in self.records:
            sum += self.records[name]

        return sum

    def max_price(self):
        res = max(self.records.values())
        for k, v in self.records.items():
            if v == res:
                return k + ':' + str(v)

    def search(self, world):
        res = list(filter(lambda x: x.lower() == world.lower(), self.records.keys()))
        if res:
            return world + ' : ' + str(self.records[res[0]])
        else:
            return 'not found'

    def write_in_file(self):
        self.file.seek(0)
        self.file.truncate()
        json.dump(self.records, self.file)
        self.file.close()


book = Book()

while True:
    print('1) Создать запись')
    print('2) Список всех записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Сохранить и выйти')
    choise = int(input('ваш выбор: '))
    if choise == 1:
        name = input('назва :')
        price = int(input('ціна :'))
        book.add_record(name=name, price=price)
    elif choise == 2:
        print(book.get_book())
    elif choise == 3:
        print(book.sum())
    elif choise == 4:
        print(book.max_price())
    elif choise == 5:
        search = input("поиск: ")
        print(book.search(search))
    elif choise == 9:
        book.write_in_file()
        break

# 1)
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name=name, age=age)
        Cinderella.__count += 1
        self.size = size

    def get_count(self):
        return self.__count


class Prince(Human):
    def __init__(self, name: str, age: int, chosen_size: int):
        super().__init__(name=name, age=age)
        self.chosen_size = chosen_size

    def search(self, list_of_cinderellas: list):
        for cinderella in list_of_cinderellas:
            if cinderella.size == self.chosen_size:
                return cinderella


# cinderella1 = Cinderella(name='cinderella1', age=18, size=39)
# cinderella2 = Cinderella(name='cinderella2', age=19, size=40)
# prince1 = Prince(name='prince1', age=20, chosen_size=39)
# print(prince1.search([cinderella1, cinderella2]))
# print(cinderella1.get_count())

# 2)
# Создать класс записной книжки
# -А каждая манипуляция над ней должна быть методом класса
# -Все данные сохраняем в переменной класса
#
#
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

class Book:
    records = {}

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


book = Book()

while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')
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
        break

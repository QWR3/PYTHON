# #ДЗ
#
# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __sub__(self, other):
        return self.x * self.y - other.x * other.y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

    def __ne__(self, other):
        return self.x * self.y != other.x * other.y

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __len__(self):
        return self.x + self.y


abcd = Rectangle(10, 20)
klmn = Rectangle(5, 5)


# print('+', abcd + klmn)
# print('-', abcd - klmn)
# print('==', abcd == klmn)
# print('!=', abcd != klmn)
# print('<', abcd < klmn)
# print('>', abcd > klmn)
# print('len', len(abcd))

#   ###############################################################################
# Це завдання на наслідування... все максимально розбити по классах
#
# 1) написати програму для запису відомостей про пасажирські перевезення

# 2) перевезення відбувається трьома способами, літаком, машиною, поїздом,

# 3) дані які треба буде зберігати:
#   - вартість квитка(літак, поїзд)
#   - кількість пасажирів(машина)
#   - час в дорозі(всі)
#   - час реєстрації(літак)
#   - клас:перший,другий(літак)
#   - вартість пального(машина)
#   - км(машина)
#   - місце: купе,св(поїзд)

# 4) методи:
#   - розрахунок вартості доїзду(машина)
#   - загальний час перельоту(літак)
#   - порівняти час в дорозі між двома будь якими транспортними засобами(двома об'єктами) - наприклад"літак на 5 годин швидше за поїзд"
#   - вивести всі дані про перевезення(поїзд)
class Traffic:
    info = {}

    def set_info(self, name, value):
        self.info = {**self.info, name: value}

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return f'{self.__class__.__name__} на {other.info["час в дорозі"] - self.info["час в дорозі"]} годин швидше за {other.__class__.__name__}'

    def __gt__(self, other):
        return f'{self.__class__.__name__} на {self.info["час в дорозі"] - other.info["час в дорозі"]} годин повільніше за {other.__class__.__name__}'


class Car(Traffic):
    def __init__(self, price_of_fuel: int, number_of_passengers: int, time_in_travel: int, kilometer: int, **kwargs):
        self.info = {"кількість пасажирів": number_of_passengers, "час в дорозі": time_in_travel,
                     "вартість пального": price_of_fuel, "км": kilometer, **kwargs}

    def get_cost_of_travel(self):
        return self.info["вартість пального"] * self.info["км"]


class Airplane(Traffic):
    def __init__(self, price: int, time_in_travel: int, time_of_registration, category: int, **kwargs):
        self.info = {'вартість': price, "час в дорозі": time_in_travel, "час реєстрації": time_of_registration,
                     "клас": category, **kwargs}

    def get_all_time(self):
        return self.info["час в дорозі"] + self.info["час реєстрації"]


class Train(Traffic):
    def __init__(self, price: int, time_in_travel: int, place: int, **kwargs):
        self.info = {'вартість': price, "час в дорозі": time_in_travel, "місце": place, **kwargs}

    def get_info(self):
        return self.info


car = Car(price_of_fuel=23, number_of_passengers=2, kilometer=34, time_in_travel=24)
train = Train(time_in_travel=25, place=3, price=5)
airplane = Airplane(price=534, time_in_travel=5, time_of_registration=2, category=1)
# print(car > airplane)
# print(car < airplane)
# print(car.get_cost_of_travel())
# print(airplane.get_all_time())
# print(train.get_info())

#   ######################################################################
#
# 1)Створити пустий list
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
list_ = []


class Letter():
    __count = 0

    def __init__(self, text: str):
        Letter.__count += 1
        self.__text = text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text: str):
        self.__text = new_text

    @text.getter
    def text(self):
        return self.__text

    def write_in_list(self):
        global list_
        list_.append(self.__text)

    def get_count(self):
        return self.__count


x = Letter(text='xx')
z = Letter(text='zz')
y = Letter(text='yy')
print(x.text, z.text, y.text)
print(x.get_count())
x.text = '(*.*)'
x.write_in_list()
z.write_in_list()
y.write_in_list()
print(list_)

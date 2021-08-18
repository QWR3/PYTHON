# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#    '1) Создать запись'
#    '2) Список все записей'
#    '3) Общая сумма всех покупок'
#    '4) Самая дорогая покупка'
#    '5) Поиск по названию покупки'
#    '9) Выход'
# - можете придумать свои пункты
index = 0
vocabulary = {'egg': 0.5, 'milk': 4.9, 'bread': 16}
while index == 0:
    print("1) Создать запись")
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')
    choise = int(input('Ваш выбор: '))
    if choise == 1:
        name = input('название: ')
        price = float(input('цена: '))
        item = {name: price}
        vocabulary.update(item)
    elif choise == 2:
        print(vocabulary)
    elif choise == 3:
        sum = 0
        for item in vocabulary:
            sum += vocabulary[item]
        print(sum)
    elif choise == 4:
        sorted_vocabulary = sorted(vocabulary.items(), key=lambda x: x[1], reverse=True)
        # https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/sortirovka-slovarja-znacheniju-kljuchu/
        print(sorted_vocabulary[0])
    elif choise == 5:
        find_key = input('введите название покупки: ')
        if find_key in vocabulary:
            print(find_key, vocabulary[find_key])
        else:
            print('ууупс, ничего не найдено')
    elif choise == 9:
        index += 1

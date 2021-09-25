class Car:
    def __init__(self, code, mark, model, year, body_type, price):
        self.code = code
        self.maker = mark
        self.model = model
        self.year = year
        self.body_type = body_type
        self.price = price

    def __str__(self):
        return f"{self.code}: {self.maker} {self.model} {self.year} год {self.body_type} - {self.price}$"


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass


def add():
    code = input_int("Введите код: ")
    maker = input("Введите марку: ")
    model = input("Введите модель: ")
    year = input_int("Введите год выпуска: ")
    body_type = input("Введите тип кузова: ")
    price = input_int("Введите стоимость: ")
    cars.append(Car(code, maker, model, year, body_type, price))


def delete():
    del_code = input_int("Введите код: ")
    for i in range(len(cars)):
        if cars[i].code == del_code:
            cars.pop(i)
            return


def search():
    search_year = input_int('Введите год выпуска: ')
    for i in range(len(cars)):
        if cars[i].year == search_year:
            print(cars[i])


stop = False
cars = []
while not stop:
    print("1. Добавить\n2. Удалить\n3. Отобразить\n4. Поиск")
    key = input()
    if key == '1':
        add()
    elif key == '2':
        delete()
    elif key == '3':
        print(*cars, sep='\n')
    elif key == '4':
        search()
    else:
        stop = True

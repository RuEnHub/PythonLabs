def t():
    while True:
        try:
            a = float(input("Введите основание a: "))
            b = float(input("Введите основание b: "))
            h = float(input("Введите высоту: "))
        except ValueError:
            print("Введено неверное число")
        else:
            break
    print(1/2*h*(a+b))


def r():
    while True:
        try:
            a = float(input("Введите сторону ромба: "))
            h = float(input("Введите высоту: "))
        except ValueError:
            print("Введено неверное число")
        else:
            break
    print(a*h)


def e():
    while True:
        try:
            a = float(input("Введите основание: "))
            h = float(input("Введите высоту: "))
        except ValueError:
            print("Введено неверное число")
        else:
            break
    print(a*h/2)


stop = False
while not stop:
    print("T - площадь трапеции\nR - площадь ромба\nE - площадь равностороннего треугольника\nQ - выход")
    key = input("Выберите пункт: ")
    if key == 'T':
        t()
    elif key == 'R':
        r()
    elif key == 'E':
        e()
    elif key == 'Q':
        stop = True
    else:
        print("Данного пункта не существует")
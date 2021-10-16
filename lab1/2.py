def normal_type(x):
    try:
        return int(x)
    except ValueError:
        pass
    try:
        return float(x)
    except ValueError:
        return x


lis = [2, "word", 1.5, 2, "word2", 2.5]

stop = False
while not stop:
    key = input("Введите пункт меню: ")
    if key == '1':
        print(lis)
    elif key == '2':
        lis.append(normal_type(input("Введите элемент: ")))
    elif key == '3':
        try:
            lis.pop(int(input("Введите позицию удаляемого элемента: ")))
        except (ValueError, IndexError):
            print("Введена неверная позиция")
    elif key == '4':
        print(tuple(lis[::2]))
    elif key == '5':
        mul = "Вещественных чисел не обнаружено"
        for i in range(len(lis)):
            if type(lis[i]) == float:
                mul = lis[i] if type(mul) == str else mul * lis[i]
        print(mul)
    elif key == '6':
        kol = 0
        zn = [',', '.', ':', '-']
        str_list = str("".join(map(str, lis)))
        for i in str_list:
            if i in zn:
                kol += 1
        print(kol)
    elif key == '7':
        M1 = set(map(normal_type, input("Введите множество M1: ").split()))
        M2 = set(lis)
        print(M1)
        print(M2)
        print(M2.difference(M1))
    elif key == '8':
        dct = {i: lis[i] for i in range(len(lis))}
        for i, value in dct.items():
            if i % 2 == 0:
                print("{0}: {1}".format(i, value))
    else:
        stop = True
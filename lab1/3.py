def t():
    while True:
        try:
            a = float(input("������� ��������� a: "))
            b = float(input("������� ��������� b: "))
            h = float(input("������� ������: "))
        except ValueError:
            print("������� �������� �����")
        else:
            break
    print(1/2*h*(a+b))


def r():
    while True:
        try:
            a = float(input("������� ������� �����: "))
            h = float(input("������� ������: "))
        except ValueError:
            print("������� �������� �����")
        else:
            break
    print(a*h)


def e():
    while True:
        try:
            a = float(input("������� ���������: "))
            h = float(input("������� ������: "))
        except ValueError:
            print("������� �������� �����")
        else:
            break
    print(a*h/2)


stop = False
while not stop:
    print("T - ������� ��������\nR - ������� �����\nE - ������� ��������������� ������������\nQ - �����")
    key = input("�������� �����: ")
    if key == 'T':
        t()
    elif key == 'R':
        r()
    elif key == 'E':
        e()
    elif key == 'Q':
        stop = True
    else:
        print("������� ������ �� ����������")
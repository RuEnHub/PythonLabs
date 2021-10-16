from math import cos, fabs, exp, log, pow, sin

while True:
    try:
        m = float(input("Введите m: "))
        n = float(input("Введите n: "))
        a = float(input("Введите a: "))
    except ValueError:
        print("Введено неверное число")
    else:
        break
try:
    result = pow(fabs(cos(a)),pow(n,m)) + exp(pow(n, 3))/log(a) + pow(sin(pow(a, 2)), 1/n)
    print(result)
except Exception as e:
    print(e)
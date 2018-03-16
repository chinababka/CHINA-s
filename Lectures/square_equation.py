from math import sqrt, fabs

print("Квадратное уравнение вида a*x**2 + b*x + c = 0")
a = int(input("Введите коэффицент a: "))
b = int(input("Введите коэффицент b: "))
c = int(input("Введите коэффицент c: "))

if (a != 0) and (b != 0) and (c != 0):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = ((-b + sqrt(d))/(2 * a))
        x2 = ((-b - sqrt(d))/(2 * a))
        print(x1, ",", x2)

    elif d == 0:
        x = (-b/(2 * a))
        print(x)

    elif d < 0:
        print("Корней нет")

elif (a != 0) and (b != 0) and (c == 0):
    x1 = 0
    if b > 0:
        x2 = - b
    else:
        x2 = b
    print(x1, ",", x2)
elif (a == 0) and (b != 0) and (c != 0):
    x = float(-c/b)
elif (a != 0) and (b == 0) and (c != 0):
    if c > 0:
        print("Корней нет")
    else:
        x1 = sqrt(fabs(c))
        x2 = -sqrt(fabs(c))
        print(x1, ",", x2)
else:
    print("Введи квадратное уравнение нормально!")
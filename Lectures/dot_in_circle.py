circle = input("Введите координаты и радиус оркужности(x y r): ")
dot = input("Ввведите координаты точки(x y): ")

if int(circle[4]) >= 0:
    if (int(dot[0]) - int(circle[0]))**2 + (int(dot[2]) - int(circle[2]))**2 <= int(circle[4])**2:
        print("Точка попала в круг!")
    else:
        print("Точка не попала в круг!")
else:
    print("Попробуйте ввести другой радиус")
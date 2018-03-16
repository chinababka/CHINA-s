s = [0, 1]
oper = ["and", "or", "+", "~"]
print("Доступные операции: ", oper)

a = int(input("Введите 1-е число(1 или 0): "))
sign = input("Введите знак булевой алгебры: ")
b = int(input("Введите 2-е число(1 или 0): "))

if (a in s) and (b in s) and (sign in oper):
    a = bool(a)
    b = bool(b)
    if sign == oper[0]:
        result = int(a and b)
        print(result)
    if sign == oper[1]:
        result = int(a or b)
        print(result)
    if sign == oper[2]:
        result = int(not (a == b))
        print(result)
    if sign == oper[3]:
        result = int(a == b)
        print(result)

else:
    print("Вы ввели невозможные значения")
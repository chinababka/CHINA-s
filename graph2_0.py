import re
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy


def odz(line):
    global k, tri_tochki
    if re.search(r'sin*|cos*|tan*|cot*', line):
        k = False
        if re.search(r'tan', line):
            tri_tochki = np.arange(-1.5, 1.625, 0.125)
            if re.search(r'/', line):
                new_tri_tochki = []
                znam = re.findall(r'\/\(.*?\)+', line)[0]
                znam = znam[2:-1]
                check_odz = odz_ext(znam)
                for i in tri_tochki:
                    if i != check_odz:
                        new_tri_tochki.append(i)
                tri_tochki = new_tri_tochki
            return trigonometry(line)
        elif re.search(r'cot', line):
            tri_tochki = np.arange(0.25, 3.125, 0.125)
            if re.search(r'/', line):
                new_tri_tochki = []
                znam = re.findall(r'\/\(.*?\)+', line)[0]
                znam = znam[2:-1]
                check_odz = odz_ext(znam)
                for i in tri_tochki:
                    if i != check_odz:
                        new_tri_tochki.append(i)
                tri_tochki = new_tri_tochki
            return trigonometry(line)
        else:
            tri_tochki = np.arange(-5, 5.5, 0.5)
            if re.search(r'/', line):
                new_tri_tochki = []
                znam = re.findall(r'\/\(.*?\)+', line)[0]
                znam = znam[2:-1]
                check_odz = odz_ext(znam)
                for i in tri_tochki:
                    if i != check_odz:
                        new_tri_tochki.append(i)
                tri_tochki = new_tri_tochki
            return trigonometry(line)
    elif re.search(r'/', line):
        k = False
        default = np.arange(-5, 5.5, 0.5)
        tri_tochki = []
        for i in default:
            znam = re.findall(r'\/\(.*?\)', line)[0]
            znam = znam[2:-1]
            pz = polskaya_zapis(znam)
            check_odz = vychysleniay_trig(pz, i, " ")
            if check_odz != 0.0:
                tri_tochki.append(i)
        return trigonometry(line)
    else:
        k = True
        tri_tochki = np.arange(-5, 5.5, 0.5)
        return polskaya_zapis(line)


def odz_ext(trig_line):
    new_trig_line = trig_line
    items_trigs = re.findall(r'sin\(.*?\)+|cos\(.*?\)+|tan\(.*?\)+|cot\(.*?\)+', new_trig_line)
    for i in tri_tochki:
        for j in items_trigs:
            text_in_brackets = re.findall(r'\(.*\)+', j)[0]
            pz = polskaya_zapis(text_in_brackets[1:-1])
            result_of_one_item = round(vychysleniay_trig(pz, i, j), 3)
            if result_of_one_item == 0.0:
                return i


def polskaya_zapis(initial):
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}
    out = []
    operators = []
    first_ch = re.findall(r'\-?\w+\.?\w*|[(+*)/\-]', initial)
    for item in first_ch:
        if item == ")":
            for item2 in range(len(operators)):
                if operators[-1] != "(":
                    out.append(operators[-1])
                    operators.remove(operators[-1])
                else:
                    operators.remove("(")
        elif not item.isdigit() and not item.isalpha() and len(item) < 2:
            if "(" in operators and len(operators) > 1 and priority[item] <= priority[operators[-1]]:
                for item3 in range(len(operators)):
                    if operators[-1] != "(":
                        out.append(operators[-1])
                        operators.remove(operators[-1])
                    else:
                        operators.append(item)
                        break
            elif "(" == item and len(operators) != 0:
                operators.append(item)
            elif "(" not in operators and len(operators) != 0 and priority[item] <= priority[operators[-1]]:
                for item4 in range(len(operators)):
                    out.append(operators[-1])
                    operators.remove(operators[-1])
                else:
                    operators.append(item)
            else:
                operators.append(item)
        else:
            out.append(item)
    else:
        for item5 in range(len(operators)):
            out.append(operators[-1])
            operators.remove(operators[-1])
    if k:
        return vychysleniay(out)
    else:
        return out


def trigonometry(trig_line):
    new_trig_line = deepcopy(trig_line)
    graph_y = []
    items_trigs = re.findall(r'sin\(.*?\)|cos\(.*?\)|tan\(.*?\)|cot\(.*?\)', new_trig_line)
    for i in tri_tochki:
        for j in items_trigs:
            text_in_brackets = re.findall(r'\(.*\)+', j)[0]
            pz = polskaya_zapis(text_in_brackets[1:-1])
            result_of_one_item = round(vychysleniay_trig(pz, i, j), 3)
            new_trig_line = new_trig_line.replace(j, str(result_of_one_item))
        else:
            pz = polskaya_zapis(new_trig_line)
            final_result = vychysleniay_trig(pz, i, new_trig_line)
            graph_y.append(round(final_result, 4))
            new_trig_line = deepcopy(trig_line)
    return tri_tochki, graph_y


def vychysleniay_trig(y, tt, trig_item):
    for j in range(len(y)):
        if y[j] == value:
            y[j] = tt
    y = list(map(lambda x: x if x == "+" or x == "-" or x == "*" or x == "/" else float(x), y))
    lenght = len(y)
    i = 0
    while i < lenght:
        if len(y) != 1:
            if y[i] in ["+", "-", "*", "/"]:
                if y[i] == "*":
                    y[i] = y[i - 2] * y[i - 1]
                    y.pop(i - 1)
                    y.pop(i - 2)
                    i = 0
                    lenght -= 2
                elif y[i] == "+":
                    y[i] = y[i - 2] + y[i - 1]
                    y.pop(i - 1)
                    y.pop(i - 2)
                    i = 0
                    lenght -= 2
                elif y[i] == "-":
                    y[i] = y[i - 2] - y[i - 1]
                    y.pop(i - 1)
                    y.pop(i - 2)
                    i = 0
                    lenght -= 2
                elif y[i] == "/":
                    y[i] = y[i - 2] / y[i - 1]
                    y.pop(i - 1)
                    y.pop(i - 2)
                    i = 0
                    lenght -= 2
            else:
                i += 1
        else:
            break
    if re.search(r'sin', trig_item):
        return np.sin(y[0])
    elif re.search(r'cos', trig_item):
        return np.cos(y[0])
    elif re.search(r'tan', trig_item):
        return np.tan(y[0])
    elif re.search(r'cot', trig_item):
        return 1 / np.tan(y[0])
    else:
        return y[0]


def vychysleniay(y):
    y_copy = deepcopy(y)
    graph_y = []  # Новый список для значений y(x)
    for i in tri_tochki:
        for j in range(len(y)):
            if y[j] == value:
                y[j] = i
        else:
            y = list(map(lambda x: x if x == "+" or x == "-" or x == "*" or x == "/" else float(x), y))
            lenght = len(y)
            i = 0
            while i < lenght:
                if len(y) != 1:
                    if y[i] in ["+", "-", "*", "/"]:
                        if y[i] == "*":
                            y[i] = y[i - 2] * y[i - 1]
                            y.pop(i - 1)
                            y.pop(i - 2)
                            i = 0
                            lenght -= 2
                        elif y[i] == "+":
                            y[i] = y[i - 2] + y[i - 1]
                            y.pop(i - 1)
                            y.pop(i - 2)
                            i = 0
                            lenght -= 2
                        elif y[i] == "-":
                            y[i] = y[i - 2] - y[i - 1]
                            y.pop(i - 1)
                            y.pop(i - 2)
                            i = 0
                            lenght -= 2
                        elif y[i] == "/":
                            y[i] = y[i - 2] / y[i - 1]
                            y.pop(i - 1)
                            y.pop(i - 2)
                            i = 0
                            lenght -= 2
                    else:
                        i += 1
                else:
                    graph_y.append(y[0])
                    y = deepcopy(y_copy)
                    break
    return tri_tochki, graph_y


def main():
    global value
    print("\t\t---WELCOME TO GRAPH BUILDER---\n"
          "Here is some basic notes to ease you to make a plot:\n"
          "1.Arguments of all trigonometric functions have to be in brackets\n"
          "     Example: sin(x), cos(5*z), tan(8), cot((j - 4) * 2)\n"
          "2.There is a tip with negative numbers:\n"
          "     Example: [5 + -4], [5+-4], [5 - 4] - are the same, but [5-4] - not\n"
          "3.In case you prefer to use /(as division), do it like this:\n"
          "     1/(x+5) or 1/(tan(x)) or 1/(sin(x+-4)) and so on\n"
          "Altogether, my prog is quite restricted, so it can not make complicated graphs\n")
    value = input("Set a letter of function's argument --F(?)--:")
    statement = input("Enter the function:")
    #print(odz(statement))

    graph = odz(statement)

    with plt.style.context("bmh"):
        plt.plot(graph[0], graph[1], 'k-o')
        plt.xlabel(value)
        plt.ylabel("F(" + value + ")")
    plt.show()

if __name__ == "__main__":
    main()

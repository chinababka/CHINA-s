import re


def vychysleniay(y):
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
            return y[0]


def polskaya_zapis(initial):
    priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}
    out = []
    operators = []
    first_ch = re.findall(r'\-?\d+\.?\d*|[(+*)(/)(\-)]', initial)
    for item in first_ch:
        if item == ")":
            for item2 in range(len(operators)):
                if operators[-1] != "(":
                    out.append(operators[-1])
                    operators.remove(operators[-1])
                else:
                    operators.remove("(")
        elif not item.isdigit() and len(item) < 2:
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
    return vychysleniay(list(map(lambda x: x if x == "+" or x == "-" or x == "*" or x == "/" else float(x), out)))


def main():
    statement = input(
        "--NOTE, THERE IS NO ERROR CHECK, SO TRY NOT TO MAKE MISTAKES WHILE INPUTTING THE EXPRESSION--\n\n"
        "Basic hints:\n"
        "-use only '+', '-', '*', '/' and brackets\n"
        "-there is a tip with a MINUS operation:\n"
        "[-5 * 12 - 4]\n"
        "[-5*12+-4]\n"
        "[-5 * 12 + -4] will give the SAME RESULT\n\n"
        "Enter the expression: ")

    print("The result is " + str(polskaya_zapis(statement)))


if __name__ == "__main__":
    main()

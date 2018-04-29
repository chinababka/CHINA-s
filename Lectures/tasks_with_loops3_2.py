from re import findall

# РАЗБИТЬ СТРОКУ НА ОТДЕЛЬНЫЕ СЛОВА И ОСОРТИРОВАТЬ ИХ В АЛФАВИТНОМ ПОРЯДКЕ
result = sorted(findall("\w+", input("Enter the string: ")))
print(result)

"""
"Я веселый таракан, я бегу, бегу, бегу"
"""
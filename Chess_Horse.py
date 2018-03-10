def Chess_Figure(var):
    lst_alp = ["a", "b", "c", "d", "e", "f", "g", "h"]
    lst_num = [1, 2, 3, 4, 5, 6, 7, 8]
    prt1 = var[:2]  # h1
    prt2 = var[3:]  # g3
    ind_alp = lst_alp.index(prt1[0])  # h = index 7 ;
    ind_num = lst_num.index(int(prt1[1]))  # 1 = index 0 ;
# 1 условие(+2;+1)
# [ind_alp] Допустмый дипазон АЛФАВИТНОГО индекса равен (2 <= ind_alp <= 5), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс АЛФАВИТНОГО листа на (+- 2).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 1).
#           Допусимый диапазон НОМЕРНОГО индекса равен (0 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 1).
    if ind_alp >= 2 and ind_alp <= 5 and (prt2[0] == lst_alp[ind_alp - 2] or prt2[0] == lst_alp[ind_alp + 2]):
        if (ind_num >= 0 and ind_num < 7 and int(prt2[1]) == lst_num[ind_num + 1]) or \
                (ind_num <= 7 and ind_num > 0 and int(prt2[1]) == lst_num[ind_num - 1]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

# 2 условие(+1;+2)
# [ind_alp] Допустмый дипазон АЛФАВИТНОГО индекса равен (1 <= ind_alp <= 6), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс АЛФАВИТНОГО листа на (+- 1).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 6), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 2).
#           Допусимый диапазон НОМЕРНОГО индекса равен (1 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 2).
    elif ind_alp >= 1 and ind_alp <= 6 and (prt2[0] == lst_alp[ind_alp - 1] or prt2[0] == lst_alp[ind_alp + 1]):
        if (ind_num >= 0 and ind_num < 6 and int(prt2[1]) == lst_num[ind_num + 2]) or \
                (ind_num <= 7 and ind_num > 1 and int(prt2[1]) == lst_num[ind_num - 2]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

# 3 доп условие(1)
# [ind_alp] ИСКЛЮЧЕНИЕ ИЗ 1-ого УСЛОВИЯ: допустмые значения АЛФАВИТНОГО индекса (ind_alp == 0, 1).
#           Поэтому я могу только изменить АЛФАВИТНЫЙ индекс на (+ 2).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 1).
#           Допусимый диапазон НОМЕРНОГО индекса равен (0 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 1).
    elif (ind_alp == 0 or ind_alp == 1) and prt2[0] == lst_alp[ind_alp + 2]:
        if (ind_num >= 0 and ind_num < 7 and int(prt2[1]) == lst_num[ind_num + 1]) or \
                (ind_num <= 7 and ind_num > 0 and int(prt2[1]) == lst_num[ind_num - 1]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

# 4 доп условие(1)
# [ind_alp] ИСКЛЮЧЕНИЕ ИЗ 1-ого УСЛОВИЯ: допустмые значения АЛФАВИТНОГО индекса (ind_alp == 6, 7).
#           Поэтому я могу только изменять АЛФАВИТНЫЙ индекс на (- 2).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 1).
#           Допусимый диапазон НОМЕРНОГО индекса равен (0 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 1).
    elif (ind_alp == 6 or ind_alp == 7) and prt2[0] == lst_alp[ind_alp - 2]:
        if (ind_num >= 0 and ind_num < 7 and int(prt2[1]) == lst_num[ind_num + 1]) or \
                (ind_num <= 7 and ind_num > 0 and int(prt2[1]) == lst_num[ind_num - 1]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

# 5 доп условие(2)
# [ind_alp] ИСКЛЮЧЕНИЕ ИЗ 2-ого УСЛОВИЯ: допустмые значения АЛФАВИТНОГО индекса (ind_alp == 0).
#           Поэтому я могу только изменять АЛФАВИТНЫЙ индекс на (+ 1).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 6), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 2).
#           Допусимый диапазон НОМЕРНОГО индекса равен (1 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 2).
    elif ind_alp == 0 and prt2[0] == lst_alp[ind_alp + 1]:
        if (ind_num >= 0 and ind_num < 6 and int(prt2[1]) == lst_num[ind_num + 2]) or \
                (ind_num > 1 and ind_num <= 7 and int(prt2[1]) == lst_num[ind_num - 2]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

# 6 доп условие(2)
# [ind_alp] ИСКЛЮЧЕНИЕ ИЗ 2-ого УСЛОВИЯ: допустмые значения АЛФАВИТНОГО индекса (ind_alp == 7).
#           Поэтому я могу только изменять АЛФАВИТНЫЙ индекс на (- 1).
# [ind_num] Допусимый диапазон НОМЕРНОГО индекса равен (0 <= ind_num < 6), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (+ 2).
#           Допусимый диапазон НОМЕРНОГО индекса равен (1 < ind_num <= 7), чтобы не выйти за границы листа.
#           Так как для поиска допустимых значений, я изменяю индекс НОМЕРНОГО листа на (- 2).
    elif ind_alp == 7 and prt2[0] == lst_alp[ind_alp - 1]:
        if (ind_num >= 0 and ind_num < 6 and int(prt2[1]) == lst_num[ind_num + 2]) or \
                (ind_num > 1 and ind_num <= 7 and int(prt2[1]) == lst_num[ind_num - 2]):
            return "Well done, You've made a right move !"
        else:
            return "Ooops, You've made a wrong move !"

    else:
        return "Wrong choice at all"
enter = input("Enter the coordinates(_ _-_ _): ")
print(Chess_Figure(enter))
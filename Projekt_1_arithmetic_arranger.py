def arithmetic_arranger(problems, i=False):
    def init_check(a):
        try:
            broj = int(a)
            return True
        except:
            return False

    a = list()
    nazivnik = list()
    brojnik = list()
    operacija = list()
    for lines in problems:
        a.append(lines.split(" "))
    for line in a:
        nazivnik.append(line[0])
        brojnik.append(line[2])
        operacija.append(line[1])

    # Part where I'm checking for errors
    if len(problems) > 5:
        return "Error: Too many problems."
    for x in operacija:
        if x == "+" or x == "-":
            continue
        else:
            return "Error: Operator must be '+' or '-'."
    for y in nazivnik:
        if len(y) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            continue
    for z in brojnik:
        if len(z) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            continue
    for xy in nazivnik:
        if init_check(xy) is False:
            return "Error: Numbers must only contain digits."
    for xz in brojnik:
        if init_check(xz) is False:
            return "Error: Numbers must only contain digits."

    lista_gore = list()     # list for first line
    lista_dolje = list()    # list for second line
    lista_crte = list()     # list for lines under first and second line
    odmak = "    "      # space between operations
    count = 0
    for b in range(len(problems)):
        first_line = "  " + ""  # two spaces
        shift = len(nazivnik[b]) - len(brojnik[b])  # like len('54') - len('4')
        if shift < 0:
            first_line += " " * abs(shift)
        first_line += nazivnik[b]
        # print(first_line, end="    ")
        count += 1
        if count == len(problems):
            lista_gore.append(first_line)   # list of first line numbers on distance of 4 whitespaces
        else:
            lista_gore.append(first_line + odmak)
    count = 0
    for c in range(len(brojnik)):
        second_line = operacija[c] + " "  # the operator (+ or -) and one space
        shift = len(nazivnik[c]) - len(brojnik[c])
        if shift > 0:
            second_line += ' ' * shift
        second_line += brojnik[c]
        # print(second_line, end="    ")
        count += 1
        if count == len(problems):
            lista_dolje.append(second_line)  # list of first line numbers on distance of 4 whitespaces
        else:
            lista_dolje.append(second_line + odmak)

    count = 0
    for d in range(len(nazivnik)):

        count += 1
        if len(brojnik[d]) > len(nazivnik[d]):

            crtice = "-" * (len(operacija[d]) + len(brojnik[d]) + 1)    # operator + len of upper number if upper number is greater than under number
            # print("-" * (len(operacija[d]) + len(brojnik[d]) + 1), end="    ")

        else:
            crtice = "-" * (len(operacija[d]) + len(nazivnik[d]) + 1)   # if under number is greater than upper number
            # print("-" * (len(operacija[d]) + len(nazivnik[d]) + 1), end="    ")

        if count == len(problems):
            lista_crte.append(crtice)  # list of first line numbers on distance of 4 whitespaces
        else:
            lista_crte.append(crtice + odmak)   # list of dashes + shift of 4 whitespaces


    # aligned is all 3 lists joined with new line between
    aligned = "".join(lista_gore) + "\n" + "".join(lista_dolje) + "\n" + "".join(lista_crte)

    lista_rezultat = list()     # list for result if i is True
    count = 0
    for e in range(len(problems)):

        if operacija[e] == "+":     # if operator is + then upper numbers + under number
            add = str(int(nazivnik[e]) + int(brojnik[e]))
        else:       # if operator is - then upper numbers - under number
            add = str(int(nazivnik[e]) - int(brojnik[e]))
        line_1 = " "

        if len(nazivnik[e]) - len(brojnik[e]) == 0:     # if upper number - under number is 0:
            if operacija[e] == "+":     # operator is +
                if len(add) == len(nazivnik[e]) or len(add) == len(brojnik[e]):     # if lenght of sum = lenght of upper or lower number(44 = 22)
                    line_1 += line_1 + add
                    # print(line_1, end="    ")
                else:
                    line_1 += add
                    # print(line_1, end="    ")
            else:   # if operator is "-"
                if add[0] == "-":   # if result is negative number
                    line_1 += add
                    # print(line_1, end="    ")
                else:   # if result is positive number
                    line_1 += line_1 * len(nazivnik[e]) + add
                    # print(line_1, end="    ")

        elif len(nazivnik[e]) - len(brojnik[e]) == -1 or len(nazivnik[e]) - len(brojnik[e]) == 1:   # upper - lower is -1 or 1 (432-22, 22-432)
            if len(add) == len(nazivnik[e]) or len(add) == len(brojnik[e]):     # result = upper, or under number (22+22=44)
                line_1 += line_1 + add
                # print(line_1, end="    ")
            else:
                line_1 += add
                # print(line_1, end="    ")

        elif len(add) == len(nazivnik[e]) + len(brojnik[e]):    # result = upper + lower (999 + 2 = 1000)
            line_1 += add
            # print(line_1, end="    ")

        else:       # lenght between upper and lower num is greater than 1 or lowe than -1
            if add[0] == "-":   #
                line_1 += add
                # print(line_1, end="    ")

            else:
                line_1 += line_1 + add
                # print(line_1, end="    ")
        count += 1
        if count == len(problems):
            lista_rezultat.append(line_1)   # list of results
        else:
            lista_rezultat.append(line_1 + odmak)

    rezultat = "\n" + "".join(lista_rezultat)  # new line + list of results
    rjesenje = aligned + rezultat
    if i is False:
        return aligned
    if i is True:
        return rjesenje


print(arithmetic_arranger(["22 + 22", "333 + 333", "333 + 333", "333 + 333", "333 + 333"], True))

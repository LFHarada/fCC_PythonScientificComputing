def arithmetic_arranger(problems, answer=False):
    # Confere a quantidade de problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    fir_op = []
    sec_op = []
    op = []

    for problem in problems:
        pieces = problem.split()
        fir_op.append(pieces[0])
        op.append(pieces[1])
        sec_op.append(pieces[2])

    # Confere a operação
    if "*" in op or "/" in op:
        return "Error: Operator must be '+' or '-'."

    # Confere os números
    for i in range(len(fir_op)):
        if not (fir_op[i].isdigit() and sec_op[i].isdigit()):
            return "Error: Numbers must only contain digits."

    # Confere o comprimento
    for i in range(len(fir_op)):
        if len(fir_op[i]) > 4 or len(sec_op[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    fir_line = []
    sec_line = []
    thi_line = []
    fou_line = []

    for i in range(len(fir_op)):
        if len(fir_op[i]) > len(sec_op[i]):
            fir_line.append(" " * 2 + fir_op[i])
        else:
            fir_line.append(" " * (len(sec_op[i]) - len(fir_op[i]) + 2) + fir_op[i])

    for i in range(len(sec_op)):
        if len(sec_op[i]) > len(fir_op[i]):
            sec_line.append(op[i] + " " + sec_op[i])
        else:
            sec_line.append(
                op[i] + " " * (len(fir_op[i]) - len(sec_op[i]) + 1) + sec_op[i])

    for i in range(len(fir_op)):
        thi_line.append("-" * (max(len(fir_op[i]), len(sec_op[i])) + 2))

    if answer:
        for i in range(len(fir_op)):
            if op[i] == "+":
                ans = str(int(fir_op[i]) + int(sec_op[i]))
            else:
                ans = str(int(fir_op[i]) - int(sec_op[i]))

            if len(ans) > max(len(fir_op[i]), len(sec_op[i])):
                fou_line.append(" " + ans)
            else:
                fou_line.append(" " * (max(len(fir_op[i]), len(sec_op[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(fir_line) + "\n" + "    ".join(sec_line) + "\n" + "    ".join(
            thi_line) + "\n" + "    ".join(fou_line)
    else:
        arranged_problems = "    ".join(fir_line) + "\n" + "    ".join(sec_line) + "\n" + "    ".join(thi_line)

    return arranged_problems

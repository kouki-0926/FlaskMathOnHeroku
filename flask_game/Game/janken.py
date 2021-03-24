from random import uniform
from flask import flash


result = [0, 0, 0]
result_2 = [0, 0, 0]
total = 0


def janken(n):
    try:
        global total
        te = ["グー", "チョキ", "パー"]
        nc = int(uniform(0, 100)) % 3+1

        Anser = [[n, nc], []]

        if (nc == n):
            result[2] += 1
            Anser[1].append("あいこ")
        elif ((nc - n == -2) or (nc - n == 1)):
            result[0] += 1
            Anser[1].append("あなたの勝ち")
        else:
            result[1] += 1
            Anser[1].append("あなたの負け")
        total += 1
        for i in range(3):
            result_2[i] = round(result[i]/total*100, 1)

        Anser[1].append("勝ち　: {}回, {}%".format(result[0], result_2[0]))
        Anser[1].append("負け　: {}回, {}%".format(result[1], result_2[1]))
        Anser[1].append("あいこ: {}回, {}%".format(result[2], result_2[2]))
    except:
        Anser = ["Error"]
        flash("Error")
    return Anser


def janken_reset():
    global result, total
    result = [0, 0, 0]
    total = 0

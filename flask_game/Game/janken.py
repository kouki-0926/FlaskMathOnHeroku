from random import uniform
from flask import flash


def janken(n, result):
    try:
        nc = int(uniform(0, 100)) % 3+1

        Anser = [[n, nc], [], result]
        if (nc == n):
            Anser[2][2] += 1
            Anser[1].append("あいこ")
        elif ((nc - n == -2) or (nc - n == 1)):
            Anser[2][0] += 1
            Anser[1].append("あなたの勝ち")
        else:
            Anser[2][1] += 1
            Anser[1].append("あなたの負け")

        total = 0
        for i in range(3):
            total += Anser[2][i]

        Anser[1].append("勝ち　: {}回, {}%".format(Anser[2][0], round(Anser[2][0]/total*100, 1)))
        Anser[1].append("負け　: {}回, {}%".format(Anser[2][1], round(Anser[2][1]/total*100, 1)))
        Anser[1].append("あいこ: {}回, {}%".format(Anser[2][2], round(Anser[2][2]/total*100, 1)))
    except:
        Anser = ["Error"]
        flash("Error")
    return Anser

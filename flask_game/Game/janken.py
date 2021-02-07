from random import uniform
from flask import flash


def janken(n):
    try:
        te = ["グー", "チョキ", "パー"]
        nc = int(uniform(0, 100)) % 3+1

        Anser = ["君は["+str(te[n-1])+"]か。"]

        if (nc == n):
            Anser.append("俺も["+te[nc - 1]+"]だ。あいこだな。")
        elif ((nc - n == -2) or (nc - n == 1)):
            Anser.append("俺は["+te[nc - 1]+"]だ。君の勝ちだな。")
        else:
            Anser.append("俺は["+te[nc - 1]+"]だ。俺の勝ちだな。")
    except:
        Anser = ["Error"]
        flash("Error")
    return Anser

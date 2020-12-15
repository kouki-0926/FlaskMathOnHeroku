from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

x = Symbol('x')


def equation(formula, type):
    try:
        A = solve(formula, dict=True)

        Anser = ["方程式:"+LATEX(formula)+"=0", ""]
        if(type == "analytical"):
            for i in range(len(A)):
                a = A[i]
                for B in a.items():
                    anser = LATEX(B[0])+"="+LATEX(B[1])
                    Anser.append(anser)
        elif(type == "numerical"):
            for i in range(len(A)):
                a = A[i]
                for B in a.items():
                    anser = LATEX(B[0])+"="+LATEX(B[1].evalf())
                    Anser.append(anser)
    except:
        Anser = ["Error"]
        flash("エラー：もう一度入力してください")
    return Anser
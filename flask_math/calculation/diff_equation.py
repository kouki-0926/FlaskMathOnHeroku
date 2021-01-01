from sympy import Symbol, Function, sympify, dsolve
from flask import flash
from flask_math.calculation.common.STR import LATEX


def diff_equation(formula):
    try:
        x = Symbol('x')
        y = Function('y')
        formula = sympify(formula)
        A = dsolve(formula)
        Anser = [LATEX(formula) + "=0"]
        if (type(A) is list):
            for i in range(len(A)):
                Anser.append(LATEX(A[i]))
        else:
            Anser.append(LATEX(A))
    except:
        Anser = ["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

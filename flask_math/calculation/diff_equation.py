from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

x = Symbol('x')
y = Function('y')

def diff_equation(formula):
    try:
        formula=sympify(formula)
        A=dsolve(formula)
        Anser=[LATEX(formula)+"=0"]
        if type(A) is list:
            for i in range(len(A)):
                Anser.append(LATEX(A[i]))
        else:
            Anser.append(LATEX(A))
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

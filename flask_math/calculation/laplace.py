from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

s, t = symbols('s, t')
w = symbols('w', real=True)


def laplace(formula, type):
    try:
        formula = simplify(formula)
        if(type == "lap"):
            anser = laplace_transform(formula, t, s)
            return LATEX(anser[0])
        elif(type == "inv"):
            anser = inverse_laplace_transform(formula, s, t)
            anser = str(anser).replace("Heaviside(t)", "u_s(t)")
            return LATEX(anser)
        else:
            flash("type エラー：もう一度入力してください")
        return "Error"
    except:
        flash("エラー：もう一度入力してください")
        return "Error"

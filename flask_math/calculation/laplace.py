from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

s, t = symbols('s, t')
w = symbols('w', real=True)


def laplace(formula, type):
    try:
        formula = simplify(formula)
        if(type == "lap"):
            Anser = laplace_transform(formula, t, s)
            anser = str(Anser[0]).replace("Heaviside(", "u_s(")
            formula = str(formula).replace("Heaviside(", "u_s(")
            return "\mathcal{L}["+LATEX(formula)+"]="+LATEX(anser)
        elif(type == "inv"):
            anser = inverse_laplace_transform(formula, s, t)
            anser = str(anser).replace("Heaviside(", "u_s(")
            formula = str(formula).replace("Heaviside(", "u_s(")
            return "\mathcal{L}^{-1}["+LATEX(formula)+"]="+LATEX(anser)
        else:
            flash("type エラー：もう一度入力してください")
        return "Error"
    except:
        flash("エラー：もう一度入力してください")
        return "Error"

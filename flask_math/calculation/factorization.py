from sympy import factor
from flask import flash
from flask_math.calculation.common.STR import LATEX


def factorization(formula):
    try:
        A = factor(formula)
        anser = LATEX(formula)+" = "+LATEX(A)
    except:
        anser = "Error"
        flash("エラー：もう一度入力してください")
    return anser

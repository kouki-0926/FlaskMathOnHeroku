from sympy import apart,Symbol
from flask import flash
from flask_math.calculation.common.STR import LATEX

x=Symbol('x')

def Apart(formula):
    try:
        anser=apart(formula)
        anser=LATEX(formula)+"="+LATEX(anser)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

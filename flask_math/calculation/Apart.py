from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x=Symbol('x')

def Apart(formula):
    try:
        anser=apart(formula)
        anser=STR(formula)+"="+STR(anser)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

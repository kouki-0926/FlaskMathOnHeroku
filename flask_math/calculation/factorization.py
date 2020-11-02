from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

def factorization(formula):
    try:
        A=factor(formula)
        anser=STR(formula)+" = "+STR(A)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

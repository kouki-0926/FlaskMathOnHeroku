from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

def Expand(formula):
    try:
        A=expand(formula)
        anser=STR(formula)+" = "+STR(A)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

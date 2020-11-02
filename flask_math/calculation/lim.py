from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x = Symbol('x')

def lim(formula,a):
    try:
        a=sympify(a)
        A=limit(formula, x, a)

        a=str(a)
        anser=STR(formula)+" = "+STR(A)
        Anser=[anser,"x→"+a,"lim"]
    except:
        Anser=["Error","",""]
        flash("エラー:もう一度関数を入力してください")
    return Anser

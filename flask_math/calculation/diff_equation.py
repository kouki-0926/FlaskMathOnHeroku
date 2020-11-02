from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR,STR_2

x = Symbol('x')
y = Function('y')

def diff_equation(formula):
    try:
        formula=sympify(formula)
        A=dsolve(formula)
        Anser=[]
        if type(A) is list:
            for i in range(len(A)):
                Anser.append(STR_2(A[i]))
        else:
            Anser.append(STR_2(A))
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

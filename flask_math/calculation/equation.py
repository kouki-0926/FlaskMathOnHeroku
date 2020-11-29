from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

x = Symbol('x')

def equation(formula):
    try:
        A=solve(formula, dict = True)

        Anser=[]
        for i in range(len(A)):
            a=A[i]
            for B in a.items():
                anser=LATEX(B[0])+"="+LATEX(B[1])
                Anser.append(anser)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    print(Anser)    
    return Anser

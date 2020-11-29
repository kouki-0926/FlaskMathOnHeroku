from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX

def equations(formula,number):
    try:
        A=solve(formula)

        Anser=[]
        if number==1:
            for i in range(len(A)):
                a=A[i]
                for B in a.items():
                    anser=LATEX(B[0])+"="+LATEX(B[1])
                    Anser.append(anser)
        else:
            for B in A.items():
                anser=LATEX(B[0])+" = "+LATEX(B[1])
                Anser.append(anser)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

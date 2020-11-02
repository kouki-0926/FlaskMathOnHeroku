from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

def equations(formula,number):
    try:
        A=solve(formula)

        Anser=[]
        if number==1:
            for i in range(len(A)):
                a=A[i]
                for B in a.items():
                    anser=STR(B[0])+"="+STR(B[1])
                    Anser.append(anser)
        else:
            for B in A.items():
                anser=STR(B[0])+" = "+STR(B[1])
                Anser.append(anser)
    except:
        Anser=["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

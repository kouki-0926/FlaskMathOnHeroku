from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x,y,z=symbols('x y z')

def derivative(formula,type):
    try:
        if type=="x":
            A = diff(formula,x)
        elif type=="y":
            A = diff(formula,y)
        elif type=="z":
            A = diff(formula,z)
        elif type=="xx":
            A = diff(formula,x,x)
        elif type=="yy":
            A = diff(formula,y,y)
        elif type=="zz":
            A = diff(formula,z,z)
        elif type=="xy":
            A = diff(formula,x,y)
        elif type=="yz":
            A = diff(formula,y,x)
        elif type=="zx":
            A = diff(formula,z,x)
        elif type=="grad":
            A = (diff(formula,x),diff(formula,y),diff(formula,z))
        elif type=="∆":
            A = (diff(formula,x,x),diff(formula,y,y),diff(formula,z,z))

        formula=" = "+STR(formula)
        A=" = "+STR(factor(A))
        Anser=[formula,"f",type,A]
    except:
        Anser=["Error","","",""]
        flash("エラー：もう一度入力してください")
    return Anser

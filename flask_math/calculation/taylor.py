from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x = Symbol('x')

def taylor(formula,dimension,center):
    try:
        f=sympify(formula)
        center=float(center)

        A=f.subs(x,center)
        for number in range(1,int(dimension)+1,1):
            f=diff(f)
            D=f.subs(x,center)/factorial(number)
            A=D*(x-center)**number+A

        anser_1="f(x)="+STR(formula)
        anser_2="f(x)≒"+STR(A)
        Anser=[anser_1,anser_2]
        print(Anser)
    except:
        Anser=["Error",""]
        flash("エラー：もう一度入力してください")
    return Anser

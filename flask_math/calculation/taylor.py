from sympy import Symbol, sympify, diff, factorial
from flask import flash
from flask_math.calculation.common.STR import LATEX

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

        anser_1="f(x)="+LATEX(formula)
        anser_2="f(x)≒"+LATEX(A)
        Anser=[anser_1,anser_2]
    except:
        Anser=["Error",""]
        flash("エラー：もう一度入力してください")
    return Anser

from sympy import Symbol, sympify, limit
from flask import flash
from flask_math.calculation.common.STR import LATEX

x=Symbol('x')

def lim(formula, a):
    try:
        A=limit(formula,x,sympify(a))
        anser="\lim_{x \\to "+str(a)+"}"+LATEX(formula)+"="+LATEX(A)
    except:
        anser="Error"
        flash("エラー:もう一度関数を入力してください")
    return anser

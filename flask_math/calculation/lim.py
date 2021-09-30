from sympy import Symbol, sympify, limit
from flask import flash
from flask_math.calculation.common.STR import LATEX

x = Symbol('x')


def lim(formula, a, type):
    try:
        if(type == "left"):
            A = limit(formula, x, sympify(a), "-")
            if(sympify(a) == 0):
                STR_a = "-"+str(a)
            else:
                STR_a = str(a) + "-0"
        elif(type == "both"):
            A = limit(formula, x, sympify(a))
            STR_a = str(a)
        elif(type == "right"):
            A = limit(formula, x, sympify(a), "+")
            if(sympify(a) == 0):
                STR_a = "+"+str(a)
            else:
                STR_a = str(a) + "+0"
        anser = "\lim_{x \\to "+STR_a+" }"+LATEX(formula)+"="+LATEX(A)
    except:
        anser = "Error"
        flash("エラー:もう一度関数を入力してください")
    return anser

from sympy import symbols, integrate
from flask import flash
from flask_math.calculation.common.STR import LATEX

x, y = symbols('x y')


def integral(formula, Up, Low, type):
    try:
        if(type == "multiple_integral_1" or type == "multiple_integral_2"):
            A = integrate(formula, (x, Low[0], Up[0]), (y, Low[1], Up[1]))
            anser = "\int_{"+LATEX(Low[1])+"}^{"+LATEX(Up[1])+"} \int_{"+LATEX(Low[0])+"}^{"+LATEX(Up[0])+"}"+LATEX(formula)+"dxdy="
            if(type == "multiple_integral_1"):
                anser += LATEX(A)
            elif(type == "multiple_integral_2"):
                anser += LATEX(A.evalf())
        else:
            g = integrate(formula, x)
            if(type == "indefinite_integral"):
                anser = "\int "+LATEX(formula)+"dx="+LATEX(g)+"+C"
            else:
                A = g.subs(x, Up[0])-g.subs(x, Low[0])
                anser = "\int_{"+LATEX(Low[0])+"}^{"+LATEX(Up[0])+"}"+LATEX(formula)+"dx="
                if(type == "definite_integral_1"):
                    anser += LATEX(A)
                elif(type == "definite_integral_2"):
                    anser += LATEX(A.evalf())
    except:
        anser = "Error"
        flash("エラー:もう一度入力してください")
    return anser

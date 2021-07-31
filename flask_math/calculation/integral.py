from sympy import symbols, integrate
from flask import flash
from flask_math.calculation.common.STR import LATEX


def integral(formula, Up, Low, type):
    try:
        x, y = symbols('x y')
        if(type == "multiple_integral_1" or type == "multiple_integral_2"):
            A = integrate(formula, (x, Low[0], Up[0]), (y, Low[1], Up[1]))
            anser = "\int_{"+LATEX(Low[1])+"}^{"+LATEX(Up[1])+"} \int_{"+LATEX(Low[0])+"}^{"+LATEX(Up[0])+"}"+LATEX(formula)+"dxdy="
            if(type == "multiple_integral_1"):
                anser += LATEX(A)
            elif(type == "multiple_integral_2"):
                anser += LATEX(A.evalf())
        else:
            if(type == "indefinite_integral"):
                A = integrate(formula, x)
                anser = "\int "+LATEX(formula)+"dx="+LATEX(A)+"+C"
            else:
                A = integrate(formula, (x, Low[0], Up[0]))
                anser = "\int_{"+LATEX(Low[0])+"}^{"+LATEX(Up[0])+"}"+LATEX(formula)+"dx="
                if(type == "definite_integral_1"):
                    anser += LATEX(A)
                elif(type == "definite_integral_2"):
                    anser += LATEX(A.evalf())
    except:
        anser = "Error"
        flash("エラー:もう一度入力してください")
    return anser

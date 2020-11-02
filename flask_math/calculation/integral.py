from sympy import *
from flask import flash
from flask_math.calculation.common.STR import STR

x,y = symbols('x y')

def integral(formula,Upper_end,Lower_end,type):
    try:
        if type=="multiple_integral_1" or type=="multiple_integral_2":
            A=integrate(formula,(x,Lower_end[0],Upper_end[0]),(y,Lower_end[1],Upper_end[1]))
            if type=="multiple_integral_1":
                anser=STR(formula)+"dxdy = "+STR(A)
            elif type=="multiple_integral_2":
                anser=STR(formula)+"dxdy = "+str(A.evalf())
        else:
            g=integrate(formula,x)
            if type=="indefinite_integral":
                anser=STR(formula)+"dx = "+STR(g)+"+c"
                Upper_end=[""]
                Lower_end=[""]
            else:
                A=g.subs(x,Upper_end[0])-g.subs(x,Lower_end[0])
                if type=="definite_integral_1":
                    anser=STR(formula)+"dx = "+STR(A)
                elif type=="definite_integral_2":
                    anser=STR(formula)+"dx = "+str(A.evalf())
        Anser=["∫",anser,Upper_end,Lower_end]
    except:
        Anser=["","Error",["",""],["",""]]
        flash("エラー:もう一度入力してください")
    return Anser

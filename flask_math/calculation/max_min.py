from sympy import *
from flask import flash
from flask_math.calculation.common.STR import LATEX


def max_min(formula):
    try:
        x, y = symbols('x y')
        formula = sympify(formula)
        f_x = diff(formula, x)
        f_y = diff(formula, y)
        f_xx = diff(formula, x, x)
        f_yy = diff(formula, y, y)
        f_xy = diff(formula, x, y)

        if f_x == 0 or f_y == 0:
            if f_x == 0:
                var = y
                det = f_yy
                A = solve(f_y, dict=True)
            else:
                var = x
                det = f_xx
                A = solve(f_x, dict=True)

            Max_Anser = []
            Min_Anser = []
            for i in range(len(A)):
                a = A[i]
                for B in a.items():
                    b = det.subs(var, B[1])
                    c = formula.subs(var, B[1])
                    if b >= 0:
                        anser = "極小値　f("+LATEX(B[1])+") = "+LATEX(c)
                        Min_Anser.append(anser)
                    else:
                        anser = "極大値　f("+LATEX(B[1])+") = "+LATEX(c)
                        Max_Anser.append(anser)
            Anser = ["f("+LATEX(var)+")="+LATEX(formula)]+Max_Anser+Min_Anser
        else:
            A = solve([f_x, f_y])
            B = []
            if type(A) == list:
                for i in range(len(A)):
                    a = A[i]
                    D = []
                    for C in a.items():
                        D.append(C[1])
                    B.append(D)
            else:
                D = []
                for C in A.items():
                    D.append(C[1])
                B.append(D)

            Anser = ["f(x,y)="+LATEX(formula)]
            for j in range(len(B)):
                a, b = B[j]

                D = f_xx*f_yy-(f_xy)**2
                D = D.subs([(x, a), (y, b)])
                f_xx = f_xx.subs([(x, a), (y, b)])
                if D > 0:
                    if f_xx > 0:
                        anser = "極小値 f("+LATEX(a)+","+LATEX(b)+")=" + \
                            LATEX(formula.subs([(x, a), (y, b)]))
                    else:
                        anser = "極大値 f("+LATEX(a)+","+LATEX(b)+")=" + \
                            LATEX(formula.subs([(x, a), (y, b)]))
                elif D < 0:
                    anser = "点("+LATEX(a)+","+LATEX(b)+")で極値をとらない"
                else:
                    anser = "点("+LATEX(a)+","+LATEX(b)+")での極値は判別できない"
                Anser.append(anser)
        if len(Anser) == 1:
            Anser.append("極値をとらない")
    except:
        Anser = ["Error"]
        flash("エラー：もう一度入力してください")
    return Anser

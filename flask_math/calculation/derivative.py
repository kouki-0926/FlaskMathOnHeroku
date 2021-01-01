from sympy import symbols, diff, factor
from flask import flash
from flask_math.calculation.common.STR import LATEX


def derivative(formula, type):
    try:
        x, y, z = symbols('x y z')
        anser = "f_{" + type + "}="
        if (type == "x"):
            A = diff(formula, x)
        elif (type == "y"):
            A = diff(formula, y)
        elif (type == "z"):
            A = diff(formula, z)
        elif (type == "xx"):
            A = diff(formula, x, x)
        elif (type == "yy"):
            A = diff(formula, y, y)
        elif (type == "zz"):
            A = diff(formula, z, z)
        elif (type == "xy"):
            A = diff(formula, x, y)
        elif (type == "yz"):
            A = diff(formula, y, x)
        elif (type == "zx"):
            A = diff(formula, z, x)
        elif (type == "grad"):
            anser = "\mathrm{grad} f="
            A = (diff(formula, x), diff(formula, y), diff(formula, z))
        elif (type == "∆"):
            anser = "\Delta f="
            A = (diff(formula, x, x), diff(formula, y, y), diff(formula, z, z))

        anser += LATEX(factor(A))
        formula = "f\left(x,y,z \\right)=" + LATEX(formula)
        Anser = [formula, anser]
    except:
        Anser = ["Error", ""]
        flash("エラー：もう一度入力してください")
    return Anser

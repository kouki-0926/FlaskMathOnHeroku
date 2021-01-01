from sympy import latex, sympify


def STR(a):
    b = str(a)
    b = b.replace("**", "#").replace("*", "").replace("#", "^")
    return b


def LATEX(formula):
    formula = sympify(formula)
    anser = latex(formula)
    anser = anser.replace("\left[", "")
    anser = anser.replace("\\right]", "")
    anser = anser.replace("{matrix}", "{pmatrix}")
    return anser

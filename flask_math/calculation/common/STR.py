from sympy import latex, sympify, factor


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


def LATEX_M(formula):
    for i in range(formula.shape[0]):
        for j in range(formula.shape[1]):
            formula[i, j] = sympify(formula[i, j])
    anser = latex(formula)
    anser = anser.replace("\left[", "")
    anser = anser.replace("\\right]", "")
    anser = anser.replace("{matrix}", "{pmatrix}")
    return anser

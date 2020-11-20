from sympy import latex, sympify

def STR(a):
    b=str(a)
    b=b.replace("**","#").replace("*","").replace("#","^")
    return b

def STR_2(a):
    a=STR(a)
    a=a.replace("Eq(","").replace(",","=")
    a=a[:-1]
    return a

def LATEX(formula):
    formula=sympify(formula)
    anser=latex(formula)
    return anser

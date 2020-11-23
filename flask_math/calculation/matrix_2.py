from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX

def calculation(matrixA,matrixB,Ar,Ac,Br,Bc,type,k,l):
    try:
        Ar,Ac,Br,Bc,k,l=[int(Ar),int(Ac),int(Br),int(Bc),int(k),int(l)]
        A=MATRIX(matrixA,Ar,Ac)
        B=MATRIX(matrixB,Br,Bc)

        if type=="A":
            anser=LATEX(A)
        elif type=="B":
            anser=LATEX(B)
        elif type=="kA+lB":
            anser=LATEX(k*A+l*B)
            type=str(k)+"A+"+str(l)+"B"
        elif type=="AB":
            anser=LATEX(A*B)
        elif type=="BA":
            anser=LATEX(B*A)
        elif type=="A・B(内積)":
            anser=LATEX(B.dot(A))
        elif type=="A×B(外積)":
            anser=LATEX(A.cross(B))
        elif type=="B×A(外積)":
            anser=LATEX(B.cross(A))
        anser=str(type)+"="+anser    
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

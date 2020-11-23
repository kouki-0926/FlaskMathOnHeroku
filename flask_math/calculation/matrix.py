from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX

def calculation(matrixA,Ar,Ac,type):
    try:
        Ar,Ac=[int(Ar),int(Ac)]
        A=MATRIX(matrixA,Ar,Ac)

        if type=="A":
            anser=LATEX(A)

        elif type=="A^n":
            A=list(A.diagonalize())
            P=A[0]
            D=A[1]
            for i in range(0,Ac,1):
                D[i,i]="("+str(D[i,i])+")^n"
            anser=LATEX(P*D*P.inv())

        elif type=="A^t":
            anser=LATEX(A.transpose())

        elif type=="A^{-1}":
            anser=LATEX(A.inv())

        elif type=="\widetilde{A}":
            anser=LATEX(A.adjugate())

        elif type=="det(A)":
            anser=LATEX(A.det())

        elif type=="rank(A)":
            anser=LATEX(A.rank())

        elif type=="tr(A)":
            anser=LATEX(A.trace())

        elif type=="λ":
            A=A.eigenvals()
            anser=""
            for B in A.items():
                anser+=LATEX(B[0])+"(n="+LATEX(B[1])+"), "    

        elif type=="P":
            A=A.diagonalize()
            A=list(A)
            anser=LATEX(A[0])

        elif type=="P^{-1}AP":
            A=A.diagonalize()
            A=list(A)
            anser=LATEX(A[1])
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

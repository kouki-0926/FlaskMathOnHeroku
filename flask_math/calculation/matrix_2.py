from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX

def calculation(matrixA,matrixB,Ar,Ac,Br,Bc,type,k,l):
    try:
        Ar,Ac,Br,Bc,k,l=[int(Ar),int(Ac),int(Br),int(Bc),int(k),int(l)]
        A=MATRIX(matrixA,Ar,Ac)
        B=MATRIX(matrixB,Br,Bc)
        type=type+" = "
        output_type="MATRIX"

        if type=="A = ":
            anser=A
            anser_r=Ar
            anser_c=Ac

        elif type=="B = ":
            anser=B
            anser_r=Br
            anser_c=Bc

        elif type=="kA+lB = ":
            anser=k*A+l*B
            type=str(k)+"A+"+str(l)+"B = "
            anser_r=Ar
            anser_c=Ac

        elif type=="AB = ":
            anser=A*B
            anser_r=Ar
            anser_c=Bc

        elif type=="BA = ":
            anser=B*A
            anser_r=Br
            anser_c=Ac

        elif type=="A・B(内積) = ":
            anser=B.dot(A)
            anser_r=""
            anser_c=""
            output_type="NUMBER"

        elif type=="A×B(外積) = ":
            anser=A.cross(B)
            anser_r=Ar
            anser_c=Ac

        elif type=="B×A(外積) = ":
            anser=B.cross(A)
            anser_r=Ar
            anser_c=Ac
    except:
        anser="Error"
        type=""
        anser_r=""
        anser_c=""
        output_type="NUMBER"
        flash("エラー：もう一度入力してください")
    Anser=[anser,type,anser_r,anser_c,output_type]
    return Anser

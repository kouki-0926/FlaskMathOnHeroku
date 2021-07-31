from sympy import *
from flask import flash
from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX, LATEX_M


a, α, d, θ = symbols("a, α, d, θ")


def calcT(parm):
    T = Matrix([[cos(θ), -sin(θ), 0, a],
                [cos(α)*sin(θ), cos(α)*cos(θ), -sin(α), -sin(α)*d],
                [sin(α)*sin(θ), sin(α)*cos(θ), cos(α), cos(α)*d],
                [0, 0, 0, 1]])
    TT = T.subs(a, parm[0])
    TT = TT.subs(α, parm[1])
    TT = TT.subs(d, parm[2])
    TT = TT.subs(θ, parm[3])
    return TT


def calcT_2(parm):
    T_list = [calcT(parm.row(i)) for i in range(parm.shape[0])]

    T = T_list[0]
    for i in range(1, len(T_list), 1):
        T = T*T_list[i]

    for i in range(T.shape[0]):
        for j in range(T.shape[0]):
            T[i, j] = replace2(T[i, j])
    return T


def Homogeneous(matrixA):
    A, Ar, Ac = MATRIX(matrixA)
    T = calcT_2(A)
    anser = "^{0}T_{"+str(T.shape[0]-1)+"} = "+LATEX_M(T)
    return anser


def replace2(a):
    b = str(a)
    for i in range(1, 4, 1):
        b = b.replace("sin(θ"+str(i)+")", "S" + str(i))
        b = b.replace("cos(θ"+str(i)+")", "C" + str(i))
    return sympify(b)

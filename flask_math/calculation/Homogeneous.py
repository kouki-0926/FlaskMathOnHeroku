# -*- coding: utf-8 -*-
from sympy import *
import re
try:
    from flask_math.calculation.common.STR import LATEX
except ImportError:
    from common.STR import LATEX


a, α, d, θ = symbols("a, α, d, θ")
L, L1, L2 = symbols("L,L1, L2")
θ1, θ2, θ3, θ4 = symbols("θ1, θ2, θ3, θ4")


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
    T_list = [calcT(parm[i]) for i in range(len(parm))]

    T = T_list[0]
    for i in range(1, len(T_list), 1):
        T = T*T_list[i]
    return T


def calc_r0(T, r3):
    r0 = T*Matrix(r3)
    return r0


def replace2(a):
    b = str(a)
    for i in range(1, 4, 1):
        b = b.replace("sin(θ"+str(i)+")", "S" + str(i))
        b = b.replace("cos(θ"+str(i)+")", "C" + str(i))
    return b


def pprint2(mat):
    mat_2 = [[], [], []]
    for j in range(3):
        mat_2[j] = [replace2(factor(mat[j, i])) for i in range(3)]
    pprint(Matrix(mat_2))


# T = calcT_2([[0, 0, 0, θ1],
#              [0, -pi/2, 0, θ2],
#              [L, 0, 0, θ3]])
# r0 = calc_r0(T, [[L], [0], [0], [1]])


def calc(r0):
    J = Matrix([[r0[0].diff(θ1, 1), r0[0].diff(θ2, 1), r0[0].diff(θ3, 1)],
                [r0[1].diff(θ1, 1), r0[1].diff(θ2, 1), r0[1].diff(θ3, 1)],
                [r0[2].diff(θ1, 1), r0[2].diff(θ2, 1), r0[2].diff(θ3, 1)]])


# pprint2(T)

# r_3 = [replace2(factor(r0[i])) for i in range(4)]
# pprint(Matrix(r_3))

# pprint2(J)

from sympy import *


def MATRIX(matrixA, Ar, Ac):
    matrixA_list = list(matrixA)
    List = []
    for j in range(Ar):
        List.append([])
        for i in range(j*(3*Ac+1), (j+1)*(3*Ac+1)-3, 3):
            if matrixA_list[i] == " ":
                m = int(matrixA_list[i+1])
            else:
                m = -int(matrixA_list[i+1])
            List[j].append(m)
    A = Matrix(List)
    return A

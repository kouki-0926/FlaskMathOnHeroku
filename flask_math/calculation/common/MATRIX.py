from sympy import Matrix


def MATRIX(matrixA):
    matrixA = matrixA.replace("\n", "")
    matrixA_list = matrixA.split("\r")

    List = []
    for i in range(len(matrixA_list)):
        tmp = matrixA_list[i].split(" ")
        List.append([j for j in tmp if j != ''])

    List = [k for k in List if len(k) != 0]
    A = Matrix(List)

    return [A, len(List), len(List[0])]

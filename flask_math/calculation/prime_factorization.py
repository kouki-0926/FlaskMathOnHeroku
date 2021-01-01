from sympy import factorint
from flask import flash


def prime_factorization(number):
    try:
        A = factorint(int(number))

        key_list = []
        value_list = []
        for B in A.items():
            key_list.append(B[0])
            value_list.append(B[1])

        C = str(key_list[0])+"^"+str(value_list[0])
        for i in range(1, len(key_list), 1):
            C = C+"・"+str(key_list[i])+"^"+str(value_list[i])

        anser = str(number)+" = "+C
    except:
        anser = "Error"
        flash("エラー：もう一度入力してください")
    return anser

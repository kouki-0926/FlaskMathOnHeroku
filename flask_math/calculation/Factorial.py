import math
from flask import flash

def Factorial(formula):
    try:
        A=math.factorial(int(formula))
        anser=str(formula)+"! = "+str(A)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

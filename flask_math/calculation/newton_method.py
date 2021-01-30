from flask_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD
from flask import flash
from sympy import sympify


def newton_method(number):
    try:
        number = sympify(number)
        if(number > 0):
            anser = "\sqrt{"+str(number)+"} = "+str(NEWTON_METHOD(number))
        else:
            anser = "Error"
            flash("エラー：正の数を入力してください")
    except:
        anser = "Error"
        flash("エラー：もう一度入力してください")
    return anser

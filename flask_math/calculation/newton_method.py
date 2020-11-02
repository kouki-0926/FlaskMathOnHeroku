from flask_math.calculation.common.NEWTON_METHOD import NEWTON_METHOD
from flask import flash

def newton_method(number):
    try:
        if float(number)>0:
            anser="="+str(NEWTON_METHOD(number))
            Anser=[number,anser]
        else:
            Anser=["Error",""]
            flash("エラー：正の数を入力してください")
    except:
        Anser=["Error",""]
        flash("エラー：もう一度入力してください")
    return Anser

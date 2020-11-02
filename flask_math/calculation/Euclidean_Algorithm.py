from flask import flash

def Euclidean_Algorithm(number_x,number_y):
    try:
        x,y=int(number_x),int(number_y)

        r=x%y
        while r>0:
            x=y
            y=r
            r=x%y
        else:
            gcd=y
        anser=str(number_x)+"と"+str(number_y)+"の最大公約数は"+str(gcd)
    except:
        anser="Error"
        flash("エラー：もう一度入力してください")
    return anser

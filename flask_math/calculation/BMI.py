from flask import flash


def BMI(height, weight):
    try:
        height = float(height)
        weight = float(weight)
        BMI = weight * 10000 / (height * height)
        if (BMI < 18.5):
            degree = "あなたは低体重です"
        elif (BMI >= 18.5 and BMI < 25):
            degree = "あなたは普通体重です"
        elif (BMI >= 25):
            degree = "あなたは肥満です"
        BMI = "BMI:" + str(BMI)
        degree = "肥満度:" + str(degree)
        anser = [BMI, degree]
    except:
        anser = ["Error", ""]
        flash("エラー：もう一度入力してください")
    return anser

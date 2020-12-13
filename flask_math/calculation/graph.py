from flask import flash, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from io import BytesIO
from sympy import *

x = symbols('x')


def graph(formula_1, lower_end_x, upper_end_x, type):
    formula_1 = sympify(formula_1)
    lower_end_x = sympify(lower_end_x)
    upper_end_x = sympify(upper_end_x)

    if(lower_end_x >= upper_end_x):
        tmp = upper_end_x
        upper_end_x = lower_end_x
        lower_end_x = tmp

    # データ作成
    num = 300
    dx = (upper_end_x-lower_end_x)/num
    t, y = [], []

    if(type == "re"):
        for i in range(int(lower_end_x/dx), int(upper_end_x/dx), 1):
            t.append(dx*i)
            y.append(formula_1.subs(x, dx*i))
    elif(type == "im"):
        re_formula = re(formula_1)
        im_formula = im(formula_1)
        for i in range(int(lower_end_x/dx), int(upper_end_x/dx), 1):
            t.append(re_formula.subs(x, dx*i))
            y.append(im_formula.subs(x, dx*i))

    fig = plt.figure(figsize=(7, 4))
    plt.plot(t, y)
    plt.title("f(x)="+str(formula_1) +" ("+str(lower_end_x)+"<x<"+str(upper_end_x)+")")
    # canvasにプロットした画像を出力
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    data = png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response = make_response(data)
    response.headers['Content-Type'] = 'image/png'
    response.headers['Content-Length'] = len(data)
    return response

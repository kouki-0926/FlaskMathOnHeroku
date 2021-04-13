from flask import make_response
from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
import numpy as np
from io import BytesIO


def graph(formula_1, lower_end_x, upper_end_x):
    x, y = symbols('x y')
    formula_1 = sympify(formula_1)
    lower_end_x = float(lower_end_x)
    upper_end_x = float(upper_end_x)

    fig = plt.figure(figsize=(7, 4))

    # データ作成
    dx = diff(formula_1, x)
    dy = diff(formula_1, y)
    if((dx == 0) or (dy == 0)):
        X = np.linspace(lower_end_x, upper_end_x, 300)
        if((dx == 0) and (dy == 0)):
            Y = lambdify(x, formula_1, "numpy")(lower_end_x)*np.ones(300)
        elif(dy == 0):
            Y = lambdify(x, formula_1, "numpy")(X)
        elif(dx == 0):
            Y = lambdify(y, formula_1, "numpy")(X)
        ax = fig.add_subplot(111)
        ax.plot(X, Y)
    else:
        s = np.linspace(lower_end_x, upper_end_x, 50)
        X, Y = np.meshgrid(s, s)
        Z = lambdify((x, y), formula_1, "numpy")(X, Y)
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.title("$f(x)="+LATEX(formula_1)+"("+str(lower_end_x)+"<x,y<"+str(upper_end_x)+")$")

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

from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response
from io import BytesIO
from sympy import *
import numpy as np

s, t, τ = symbols('s, t, τ')
num = 150


def sysio(formula, formula_2, lower_end, upper_end, type):
    formula = simplify(formula)
    formula_2 = simplify(formula_2)
    lower_end = float(lower_end)
    upper_end = float(upper_end)

    if(type == "s"):
        output = apart(formula*formula_2)
        anser = inverse_laplace_transform(output, s, t)
    else:
        g = simplify(formula).subs(t, t-τ)
        u = simplify(formula_2).subs(t, τ)
        y = integrate(g*u, τ)
        anser = y.subs(τ, t)-y.subs(τ, 0)
        anser = str(anser).replace("Heaviside(0)", "0")
        anser = simplify(anser)
    title = str(factor(anser)).replace("Heaviside(", "u_s(")

    # データ作成
    T = np.linspace(lower_end, upper_end, num)
    Y = np.array([anser.subs(t, T[i]) for i in range(len(T))])

    fig = plt.figure(figsize=(7, 4))
    plt.plot(T, Y)
    plt.xlim(lower_end, upper_end)
    plt.title("$y(t)="+LATEX(title)+"("+str(lower_end)+"<t<"+str(upper_end)+")$")

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

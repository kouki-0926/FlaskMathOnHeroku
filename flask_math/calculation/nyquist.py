from flask import make_response
from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from math import degrees
from sympy import *
import numpy as np
from io import BytesIO


def nyquist(formula):
    s = symbols('s')
    formula = sympify(formula)
    formula_2 = lambdify(s, formula, "numpy")

    w_list_1 = np.array([-10**(i/100) for i in range(-3000, 3000, 1)])
    w_list_2 = np.array([10**(i/100) for i in range(-3000, 3000, 1)])
    w_list = np.hstack((w_list_1, w_list_2))
    formula_3 = formula_2(1j*w_list)

    deg = np.linspace(0, 2*np.pi, 100)
    circle_x = np.cos(deg)
    circle_y = np.sin(deg)

    fig = plt.figure(figsize=(7, 4))
    plt.title("$G(s)="+LATEX(formula)+"$")
    plt.plot(np.real(formula_3), np.imag(formula_3))
    plt.plot(circle_x, circle_y, label="0dB")
    plt.plot(-1, 0, marker="x", color="red", label="s=-1+0j")
    plt.axhline(y=0, color="black")
    plt.axvline(x=0, color="black")
    plt.legend()

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

from flask_math.calculation.common.MATRIX import MATRIX
from flask_math.calculation.common.STR import LATEX
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response
from io import BytesIO
from sympy import *
import numpy as np

s, t, τ = symbols('s, t, τ')
num = 150


def sysio_matrix(matrix_A, matrix_B, matrix_C, matrix_D, matrix_X, formula, lower_end, upper_end, type):
    A, Ar, Ac = MATRIX(matrix_A)
    B, Br, Bc = MATRIX(matrix_B)
    C, Cr, Cc = MATRIX(matrix_C)
    D, Dr, Dc = MATRIX(matrix_D)
    X, Xr, Xc = MATRIX(matrix_X)
    formula = simplify(formula)
    lower_end, upper_end = [float(lower_end), float(upper_end)]

    inverse = (s*eye(Ar)-A).inv()
    matrix_T = inverse_laplace_transform(inverse, s, t)
    print(matrix_T)

    anser_1 = matrix_T*X
    Integrand = (matrix_T.subs(t, t-τ))*B*formula
    T = integrate(Integrand, τ)
    anser_2 = T.subs(τ, t)-T.subs(τ, 0)

    anser = LATEX(anser_1+anser_2)
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

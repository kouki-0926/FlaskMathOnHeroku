from flask import flash, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from math import degrees
from sympy import *
import numpy as np
from io import BytesIO


def bode(formula, lower_end, upper_end, width):
    s = symbols('s')
    formula = sympify(formula)
    formula_2 = lambdify(s, formula, "numpy")
    title = ""

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    # データ作成
    w_list = np.array([10**(i/width) for i in range(int(lower_end)*width, int(upper_end)*width, 1)])
    g_list = 20*np.log10(np.abs(formula_2(1j*w_list)))
    φ_list = np.rad2deg(np.angle(formula_2(1j*w_list)))
    φ_list[np.where(φ_list > 0)] = φ_list[np.where(φ_list > 0)]-360

    tmpWc = np.average(w_list[np.where(abs(g_list) < 5)])
    if(str(tmpWc) != "nan"):
        w_list_c = np.array([i/100 for i in range(int((tmpWc-0.3)*100), int((tmpWc+0.3)*100), 1)])
        g_list_c = 20*np.log10(np.abs(formula_2(1j*w_list_c)))
        Wc = w_list_c[np.argmin(np.abs(g_list_c))]
        Pm = 180+np.rad2deg(np.angle(formula_2(1j*Wc)))

        ax1.axvline(x=Wc, color="black")
        ax2.axvline(x=Wc, color="black")
        title += "Wc="+str(round(Wc, 2))+"rad/s, Pm="+str(round(Pm, 2))+"deg, "

    tmpWp = np.average(w_list[np.where((-190 < φ_list) & (φ_list < -170))])
    if(str(tmpWp) != "nan"):
        w_list_p = np.array([i/100 for i in range(int((tmpWp-0.3)*100), int((tmpWp+0.3)*100), 1)])
        φ_list_p = np.rad2deg(np.angle(formula_2(1j*w_list_p)))
        φ_list_p[np.where(φ_list_p > 0)] = φ_list_p[np.where(φ_list_p > 0)]-360
        Wp = w_list_p[np.argmin(np.abs(180+φ_list_p))]
        Gm = -20*np.log10(np.abs(formula_2(1j*Wp)))

        ax1.axvline(x=Wp, color="black")
        ax2.axvline(x=Wp, color="black")
        title += "Wπ="+str(round(Wp, 2))+"rad/s, Gm="+str(round(Gm, 2))+"dB, "

    ax1.plot(w_list, g_list)
    ax2.plot(w_list, φ_list)
    ax1.set_xscale("log")
    ax2.set_xscale("log")
    ax1.axhline(y=0, color="black")
    ax2.axhline(y=-180, color="black")

    ax1.set_title("G(s)="+str(formula))
    plt.title(title, y=-0.30)
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

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
    title = ""

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    # データ作成
    w_list = np.array([10**(i/width) for i in range(int(lower_end)*width, int(upper_end)*width, 1)])
    g_list = np.array([20*log(Abs(formula.subs(s, I*w_list[i])), 10) for i in range(len(w_list))])
    φ_list = np.array([degrees(arg(formula.subs(s, I*w_list[i]))) for i in range(len(w_list))])
    φ_list[np.where(φ_list > 0)] = φ_list[np.where(φ_list > 0)]-360

    ax1.plot(w_list, g_list)
    ax2.plot(w_list, φ_list)
    ax1.axhline(y=0, xmin=int(lower_end), xmax=int(upper_end), color="black")
    ax2.axhline(y=-180, xmin=int(lower_end),xmax=int(upper_end), color="black")
    ax1.set_xscale("log")
    ax2.set_xscale("log")

    tmpWc = np.average(w_list[np.where(abs(g_list) < 5)])
    if(str(tmpWc) != "nan"):
        w_list_c = np.array([i/100 for i in range(int((tmpWc-0.3)*100), int((tmpWc+0.3)*100), 1)])
        g_list_c = np.array([20*log(Abs(formula.subs(s, I*w_list_c[i])), 10) for i in range(len(w_list_c))])
        Wc = w_list_c[np.argmin(abs(g_list_c))]
        Pm = round(180+degrees(arg(formula.subs(s, I*Wc))), 2)
        ax1.axvline(x=Wc, color="black")
        ax2.axvline(x=Wc, color="black")
        title += "Wc="+str(Wc) + "rad/s, Pm="+str(Pm)+"deg, "

    tmpWp = np.average(w_list[np.where((-190 < φ_list) & (φ_list < -170))])
    if(str(tmpWp) != "nan"):
        w_list_p = np.array([i/100 for i in range(int((tmpWp-0.3)*100), int((tmpWp+0.3)*100), 1)])
        φ_list_p = np.array([degrees(arg(formula.subs(s, I*w_list_p[i]))) for i in range(len(w_list_p))])
        φ_list_p[np.where(φ_list_p > 0)] = φ_list_p[np.where(φ_list_p > 0)]-360
        Wp = w_list_p[np.argmin(abs(180+φ_list_p))]
        Gm = round(-20*log(Abs(formula.subs(s, I*Wp)), 10), 2)
        ax1.axvline(x=Wp, color="black")
        ax2.axvline(x=Wp, color="black")
        title += "Wπ="+str(Wp)+"rad/s, Gm="+str(Gm)+"dB, "
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

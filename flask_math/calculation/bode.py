import numpy as np
from flask import flash, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from io import BytesIO
from sympy import *
from math import degrees
import numpy as np


def bode(formula, lower_end, upper_end, width):
    s = symbols('s')
    w_pi_flag = 0
    w_c_flag = 0
    formula = sympify(formula)

    # データ作成
    w_list, g_list, φ_list = np.empty(0), np.empty(0), np.empty(0)
    for i in range(int(lower_end)*width, int(upper_end)*width, 1):
        w = 10**(i/width)
        g = 20*log(Abs(formula.subs(s, I*w)), 10)
        φ = degrees(arg(formula.subs(s, I*w)))
        if(φ >= 0):
            φ -= 360
        if(g != zoo):
            w_list = np.append(w_list, w)
            g_list = np.append(g_list, g)
            φ_list = np.append(φ_list, φ)
        if((-185 <= φ) & (φ <= -175)):
            w_pi = w
            w_pi_flag = 1
        if((-5 <= g) & (g <= 5)):
            w_c = w
            w_c_flag = 1

    if(w_pi_flag):
        b_2_list = [[], []]
        for j in range(int((w_pi-1)*100), int((w_pi+1)*100), 1):
            c_2 = j/100
            b_2 = degrees(arg(formula.subs(s, I*c_2)))
            if(b_2 >= 0):
                b_2 -= 360
            b_2_list[0].append(abs(b_2+180))
            b_2_list[1].append(c_2)
        w_pi_2 = b_2_list[1][np.argmin(b_2_list[0])]
        Gm = float(-20*log(Abs(formula.subs(s, I*w_pi_2)), 10))
    if(w_c_flag):
        b_3_list = [[], []]
        for k in range(int((w_c-1)*100), int((w_c+1)*100), 1):
            c_3 = k/100
            g_c = 20*log(Abs(formula.subs(s, I*c_3)), 10)
            b_3_list[0].append(abs(g_c))
            b_3_list[1].append(c_3)
        w_c_2 = b_3_list[1][np.argmin(b_3_list[0])]
        Pm = 180+degrees(arg(formula.subs(s, I*w_c_2)))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)

    ax1.plot(w_list, g_list)
    ax1.axhline(y=0, xmin=int(lower_end), xmax=int(upper_end), color="black")
    ax1.set_xscale("log")

    ax2.plot(w_list, φ_list)
    ax2.axhline(y=-180, xmin=int(lower_end), xmax=int(upper_end), color="black")
    ax2.set_xscale("log")

    title = "G(s)="+str(formula)
    title_2 = ""
    if(w_pi_flag):
        title_2 += "ωπ="+str(w_pi_2)+"rad/s, Gm="+str(round(Gm, 2))+"dB, "
        ax1.axvline(x=w_pi_2, color="black")
        ax2.axvline(x=w_pi_2, color="black")
    if(w_c_flag):
        title_2 += "ωc="+str(w_c_2)+"rad/s, Pm="+str(round(Pm, 2))+"deg "
        ax1.axvline(x=w_c_2, color="black")
        ax2.axvline(x=w_c_2, color="black")
    ax1.set_title(title)
    plt.title(title_2, y=-0.30)

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

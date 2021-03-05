from functools import wraps
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response, flash, redirect, url_for
from subprocess import getoutput
from io import BytesIO
import datetime
import serial
import os

graph_Data = [[], [], []]
connected = False
try:
    ser = serial.Serial("/dev/ttyACM0", 9600)
    connected = True
    print("pyserial was initialized")
except:
    connected = False
    print("pyserial was not initialized")


def decode():
    a = ser.readline()
    a = a.strip()
    a = a.decode("utf-8")
    return a


def check_connect(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if(connected):
            return func(*args, **kwargs)
        else:
            print("Arduino is not connected")
    return inner


@check_connect
def arduino_destroy():
    ser.close()
    print("arduino_destroy")


@check_connect
def LED(state):
    ser.write(state.encode("utf-8"))


def reset_graph_Data():
    global graph_Data
    graph_Data = [[], [], []]
    print("graph_Data was initialized")


def measure_temp():
    global graph_Data, ser
    Data = []

    ser.write(b'm')
    if(decode() == "OK"):
        connected = True
        print("Arduino is connected")
    else:
        try:
            ser = serial.Serial("/dev/ttyACM0", 9600)
            connected = True
            print("pyserial was initialized")
            return redirect(url_for("arduino.measure_temp_view"))
        except:
            connected = False
            print("Arduino is not connected")
            return ["Error"]

    date = datetime.datetime.now()
    display_date = str(date).split(".")
    Data.append(display_date[0])
    graph_date = date.strftime("%H:%M:%S")
    graph_Data[0].append(graph_date)

    tmp_Data = []
    for count in range(2):
        data = decode()
        tmp_Data.append(float(data))
    Data.append(tmp_Data)
    graph_Data[1].append(tmp_Data[0])
    graph_Data[2].append(tmp_Data[1])

    print("measure_temp was successful")
    return Data


def graph_temp(graph_type):
    global graph_Data
    try:
        if(len(graph_Data[0]) != len(graph_Data[1])):
            graph_Data = [[], [], []]
        if(len(graph_Data[0]) >= 20):
            graph_Data[0] = graph_Data[0][1:]
            graph_Data[1] = graph_Data[1][1:]
            graph_Data[2] = graph_Data[2][1:]

        fig = plt.figure(figsize=(7, 8))
        plt.xlabel("time")
        plt.xticks(rotation=60)

        if(graph_type == "temp"):
            plt.title('temperature')
            plt.ylabel("temperature [℃]")
            plt.plot(graph_Data[0], graph_Data[1])
        elif(graph_type == "humi"):
            plt.title('humidity')
            plt.ylabel("humidity [%]")
            plt.plot(graph_Data[0], graph_Data[2])

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
    except:
        flash("graph error")

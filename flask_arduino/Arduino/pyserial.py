from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response,flash
from subprocess import getoutput
from io import BytesIO
import datetime
import serial
import os

ser=0
def init():
    global ser
    if(ser==0):
        flash("pyserial was initialized")
        ser=serial.Serial("/dev/ttyACM0",9600)
        

graph_Data=[[],[]]
def measure():
    global graph_Data
    Data=[]
    try:
        ser.write(b'm')
    except:
        init()  

    date=datetime.datetime.now()
    display_date=str(date).split(".")
    Data.append(display_date[0])
    graph_date=date.strftime("%H:%M:%S")
    graph_Data[0].append(graph_date)
  
    tmp_Data=[]
    for count in range(2):
        data=ser.readline()
        data=data.strip()
        data=data.decode("utf-8")
        tmp_Data.append(float(data))
    Data.append(tmp_Data)
    graph_Data[1].append(tmp_Data[0])
    return Data

def graph_temp():
    global graph_Data
    try:
        if(len(graph_Data[0])!=len(graph_Data[1])):
            graph_Data=[[],[]]
        if(len(graph_Data[0])>=20):
            graph_Data[0]=graph_Data[0][1:]
            graph_Data[1]=graph_Data[1][1:]

        fig=plt.figure(figsize=(7,8))
        plt.title('temperature')
        plt.xlabel("time")
        plt.xticks(rotation=60)      
        plt.ylabel("temperature [℃]")

        plt.plot(graph_Data[0],graph_Data[1])
        # canvasにプロットした画像を出力
        canvas=FigureCanvasAgg(fig)
        png_output=BytesIO()
        canvas.print_png(png_output)
        data=png_output.getvalue()
        # HTML側に渡すレスポンスを生成する
        response=make_response(data)
        response.headers['Content-Type']='image/png'
        response.headers['Content-Length']=len(data)
        return response
    except:
        flash("graph error")


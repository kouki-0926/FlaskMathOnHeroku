from flask import redirect, url_for, render_template, flash, Blueprint, request
from flask_arduino.Arduino import pyserial as pys
from termcolor import cprint


arduino = Blueprint("arduino", __name__, template_folder='templates_arduino', static_folder="static_arduino")


@arduino.route("/")
def index_view():
    return render_template("index_arduino.html")


@arduino.route("/init")
def init_view():
    connected = pys.arduino_init()
    if(connected):
        flash("Arduinoとの接続が確認できました")
    else:
        flash("Error:Arduinoとの接続が確認できませんでした")
    return redirect(url_for("arduino.index_view"))


@arduino.route("/measure_temp")
def measure_temp_view():
    try:
        Data = pys.measure_temp()
        graph_type = request.args.get("graph_type")
        if(graph_type == "reset"):
            return redirect(url_for("arduino.reset_graph_Data_view"))
        elif(graph_type != "temp" and graph_type != "humi"):
            graph_type = "temp"
        return render_template("measure_temp.html", time=Data[0], temperature=Data[1][0], humidity=Data[1][1], graph_type=graph_type)
    except:
        flash("Error:Arduinoとの接続が確認できませんでした")
        return redirect(url_for("arduino.index_view"))


@arduino.route("/measure_temp/reset")
def reset_graph_Data_view():
    pys.reset_graph_Data()
    flash("データは正常に初期化されました")
    return redirect(url_for("arduino.index_view"))


@arduino.route("/graph_temp")
def graph_temp_view():
    graph_type = request.args.get("graph_type")
    return pys.graph_temp(graph_type)


@arduino.route("/led")
def led_view():
    state = request.args.get("state")
    if(pys.LED(state[0])):
        cprint("arduino LED state: "+state, "cyan")
        return render_template("led_arduino.html", state=state)
    else:
        flash("Error:Arduinoとの接続が確認できませんでした")
        return redirect(url_for("arduino.index_view"))

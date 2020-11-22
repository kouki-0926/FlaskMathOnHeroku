from flask import redirect,url_for,render_template,flash,Blueprint
from flask_arduino.Arduino import pyserial as pys

arduino=Blueprint("arduino",__name__,template_folder='templates_arduino',static_folder="static_arduino")

@arduino.route("/")
def index_view():
    return render_template("index_arduino.html")

@arduino.route("/measure")
def measure_view():
    try:
        Data=pys.measure()
        return render_template("measure_temp.html",time=Data[0],temperature=Data[1][0],humidity=Data[1][1])
    except:
        flash("Error:Arduinoとの接続が確認できませんでした")
        return redirect(url_for("arduino.index_view"))

@arduino.route("/graph_temp")
def graph_temp_view():
    return pys.graph_temp()

@arduino.route("/measure/reset")
def reset_graph_Data_view():
    pys.reset_graph_Data()
    return redirect(url_for("arduino.measure_view"))

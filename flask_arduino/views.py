from flask import redirect,url_for,render_template,flash,Blueprint
from flask_arduino.Arduino import pyserial as pys

arduino=Blueprint("arduino",__name__,template_folder='templates_arduino',static_folder="static_arduino")

@arduino.route("/")
def index_view():
    return render_template("index_arduino.html")


@arduino.route("/measure_temp")
def measure_temp_view():
    try:
        Data=pys.measure_temp()
        return render_template("measure_temp.html",time=Data[0],temperature=Data[1][0],humidity=Data[1][1])
    except:
        flash("Error:Arduinoとの接続が確認できませんでした")
        return redirect(url_for("arduino.index_view"))

@arduino.route("/graph_temp")
def graph_temp_view():
    return pys.graph_temp()

@arduino.route("/measure_temp/reset")
def reset_graph_Data_view():
    pys.reset_graph_Data()
    flash("データは正常に初期化されました")
    return redirect(url_for("arduino.measure_temp_view"))



@arduino.route("/blink")
def blink_view():
    pys.blink()
    return redirect(url_for("arduino.index_view"))

@arduino.route("/RGB")
def RGB_view():
    pys.RGB()
    return redirect(url_for("arduino.index_view"))

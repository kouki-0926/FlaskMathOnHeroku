from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_CPU.CPU import *
import json

cpu = Blueprint("cpu", __name__, template_folder='templates_cpu', static_folder="static_cpu")


@cpu.route("/")
def index_view():
    return render_template("index_cpu.html")


@cpu.route("/measure", methods=["GET", "POST"])
def measure_view():
    try:
        Data = CPU.get_display_Data()
        if (Data[0] == "Error"):
            flash("Error:CPU情報の取得失敗")
            return redirect(url_for("cpu.index_view"))
        if (request.method == "GET"):
            graph_type = request.args.get("graph_type")
        elif (request.method == "POST"):
            graph_type = request.form.get("graph_type")
        return render_template("measure.html", Data=Data, graph_type=graph_type)
    except:
        flash("Error:CPU情報の取得失敗")
        return redirect(url_for("cpu.index_view"))


@cpu.route('/graph.png')
def graph_view():
    graph_type = request.args.get("graph_type")
    return CPU.graph_cpu(graph_type)


@cpu.route("/weather")
def weather_view():
    pref_num = request.args.get("pref_num")
    if (pref_num is None):
        return redirect(url_for("cpu.weather_view", pref_num="130010"))

    try:
        Data = weather.get_weather(pref_num)
        return render_template("weather.html", Data=Data, pref_num=pref_num)
    except:
        flash("ERROR")
        return redirect(url_for("cpu.index_view"))


@cpu.route("/ip_address")
def ip_address_view():
    ip_address = request.args.get("ip_address")
    if (ip_address is not None):
        Data = ip.get_location(ip_address)
        try:
            st_Data = station.get_data(Data["longitude"], Data["latitude"])
        except:
            st_Data = []
            flash("最寄り駅の情報取得失敗")
        return render_template("ip_address.html", Data=Data, st_Data=st_Data, init_flag=0)
    else:
        return render_template("ip_address.html", Data=[], st_Data=[], init_flag=1)


@cpu.route("/translate", methods=['GET', 'POST'])
def translate_view():
    if (request.method == "GET"):
        return render_template("translate.html", en_text="", ja_text="", init_flag=1)
    elif (request.method == "POST"):
        en_text = request.form.get("en_text")
        if (en_text is None):
            flash("英文を入力してください")
            return render_template("translate.html", en_text="", ja_text="", init_flag=1)
        try:
            en_text = en_text.replace("\n", " ").replace("\r", "")  # 改行文字を削除
            if (request.form.get("translate_method") == "Google"):
                ja_text = translate.translate(en_text) # Google翻訳
                return render_template("translate.html", en_text=en_text, ja_text=ja_text, init_flag=0)
            else:
                return render_template("translate.html", en_text=en_text, ja_text="", init_flag=0, new_page=1)
        except:
            flash("翻訳失敗")
            return render_template("translate.html", en_text=en_text, ja_text="", init_flag=1)


@cpu.route('/map')
def map_view():
    try:
        longitude = float(request.args.get("longitude"))
        latitude = float(request.args.get("latitude"))
        return render_template("map.html", longitude=json.dumps(longitude), latitude=json.dumps(latitude), init_flag=1)
    except:
        return redirect(url_for("cpu.map_view", longitude=139.755868, latitude=35.682783))

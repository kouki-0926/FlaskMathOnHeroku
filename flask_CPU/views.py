from flask import redirect,request,url_for,render_template,flash,Blueprint
from flask_CPU.CPU import *

cpu=Blueprint("cpu",__name__,template_folder='templates_cpu',static_folder="static_cpu")

@cpu.route("/")
def index():
    return render_template("index_cpu.html")


@cpu.route("/measure",methods=["GET","POST"])
def measure():
    Data=CPU.get_display_Data()
    if(request.method=="GET"):
        graph_type=request.args.get("graph_type")
    elif(request.method=="POST"):
        graph_type=request.form.get("graph_type")
    return render_template("measure.html",Data=Data,graph_type=graph_type)

@cpu.route('/graph.png')
def graph():
    graph_type=request.args.get("graph_type")
    return CPU.graph_cpu(graph_type)


@cpu.route("/weather",methods=["GET","POST"])
def weather_view():
    pref_num=request.args.get("pref_num")
    if(pref_num is None):
        pref_num="130010"

    try:
        data=weather.get_weather(pref_num)
    except:
        flash("ERROR : pref_num")
        return redirect(url_for("cpu.weather_view"))
    return render_template("weather.html", Data=data[0], Forecast=data[1],pref_num=pref_num)


@cpu.route("/ip_address", methods=["GET", "POST"])
def ip_address_view():
    Data = ip.get_location()
    if(Data[0] == "error: True"):
        Data[0] = "ERROR"
        flash("error")
    return render_template("ip_address.html", Data=Data)

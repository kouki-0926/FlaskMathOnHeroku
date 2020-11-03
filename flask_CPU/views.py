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

data=[[],[]]
@cpu.route("/weather",methods=["GET","POST"])
def weather_view():
    global data
    new_pref_num=request.args.get("new_pref_num")
    region=request.args.get("region")

    if(region is not None):
        return render_template("weather.html", Data=data[0], Forecast=data[1], region=region, new_pref_num=new_pref_num)
    if(new_pref_num is None):
        new_pref_num="130010"
        
    data=weather.get_weather(new_pref_num)
    return render_template("weather.html", Data=data[0], Forecast=data[1], region=region, new_pref_num=new_pref_num)
    

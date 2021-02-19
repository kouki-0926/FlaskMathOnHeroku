from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_raspi.raspi.raspi import Blink, High, LOW

raspi = Blueprint("raspi", __name__, template_folder='templates_raspi', static_folder="static_raspi")


@raspi.route("/")
def index_view():
    return render_template("index_raspi.html")


@raspi.route("/Blink", methods=["GET", "POST"])
def Blink_view():
    try:
        Blink()
        return render_template("Blink.html")
    except:
        flash("Error")
        return redirect(url_for("raspi.index_view"))


@raspi.route("/led", methods=["GET", "POST"])
def led_view():
    if(request.method == "GET"):
        state = request.args.get("state")
        if(state == "high"):
            High()
            return render_template("led.html", state="high")
        elif(state == "low"):
            LOW()
            return render_template("led.html", state="low")
        else:
            return redirect(url_for("raspi.led_view", state="high"))
    else:
        return redirect(url_for("raspi.led_view", state="high"))
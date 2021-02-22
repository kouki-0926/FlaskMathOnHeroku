from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_raspi.raspi.raspi import Blink, High, LOW

raspi = Blueprint("raspi", __name__, template_folder='templates_raspi', static_folder="static_raspi")


@raspi.route("/")
def index_view():
    return render_template("index_raspi.html")


@raspi.route("/led", methods=["GET", "POST"])
def led_view():
    if(request.method == "GET"):
        state = request.args.get("state")
        if(state == "high"):
            High()
            return render_template("led_raspi.html", state="high")
        elif(state == "low"):
            LOW()
            return render_template("led_raspi.html", state="low")
        elif(state == "blink"):
            Blink()
            return render_template("led_raspi.html", state="blink")
        else:
            return redirect(url_for("raspi.led_view", state="high"))
    else:
        return redirect(url_for("raspi.led_view", state="high"))

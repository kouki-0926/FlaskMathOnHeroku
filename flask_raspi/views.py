from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_raspi.raspi.raspi import Blink

raspi = Blueprint("raspi", __name__, template_folder='templates_raspi', static_folder="static_raspi")


@raspi.route("/")
def index_view():
    return render_template("index_raspi.html")


@raspi.route("/Blink", methods=["GET", "POST"])
def Blink_view():
    Blink()
    return render_template("led.html")
    # try:
    # except:
    #     flash("Error")
    #     return redirect(url_for("raspi.index_view"))
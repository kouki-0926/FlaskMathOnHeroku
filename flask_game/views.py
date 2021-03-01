from flask import request, redirect, url_for, render_template, flash, Blueprint
from flask_game.Game import *

game = Blueprint("game", __name__, template_folder='templates_game', static_folder="static_game")


@game.route("/")
def index_view():
    return render_template("index_game.html")


@game.route("/janken")
def janken_view():
    n = request.args.get("n")
    if(n == '1' or n == '2' or n == '3'):
        Anser = janken.janken(int(n))
        return render_template("janken.html", n=n, Anser=Anser)
    else:
        return redirect(url_for("game.janken_view", n='1'))

@game.route("/janken_ml")
def janken_ml_view():
    n = request.args.get("n")
    if(n == '1' or n == '2' or n == '3'):
        Anser = janken_ml.janken_ml(int(n))
        return render_template("janken_ml.html", n=n, Anser=Anser)
    else:
        return redirect(url_for("game.janken_ml_view", n='1'))


@game.route("/box")
def box_view():
    return render_template("box.html")


@game.route("/bike")
def bike_view():
    return render_template("bike.html")

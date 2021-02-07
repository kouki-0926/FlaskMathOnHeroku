from flask import redirect, render_template, flash, Blueprint, request
from flask_game.Game import *

game = Blueprint("game", __name__,
                 template_folder='templates_game', static_folder="static_game")


@game.route("/")
def index_view():
    return render_template("index_game.html")


@game.route("/janken", methods=["GET", "POST"])
def janken_view():
    if request.method == "POST":
        n = int(request.form.get("n"))
        Anser = janken.janken(n)
        return render_template("janken.html", n=n, Anser=Anser)
    else:
        return render_template("janken.html", n=1)


@game.route("/box")
def box_view():
    return render_template("box.html")


@game.route("/bike")
def bike_view():
    return render_template("bike.html")

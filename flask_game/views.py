from flask import redirect, render_template, flash, Blueprint, request
from flask_game.Game import *

game = Blueprint("game", __name__, template_folder='templates_game', static_folder="static_game")


@game.route("/")
def index_view():
    return render_template("index_game.html")


@game.route("/jyanken", methods=["GET", "POST"])
def jyanken_view():
    if request.method == "POST":
        n = int(request.form.get("n"))
        Anser = jyanken.jyanken(n)
        return render_template("jyanken.html", n=n, Anser=Anser)
    else:
        return render_template("jyanken.html", n=1)

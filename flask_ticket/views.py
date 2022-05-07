from flask import request, redirect, url_for, render_template, flash, Blueprint, session

ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


Date = ["R40301-R40303",
        "R40303-R40308",
        "R40301",
        "R40301"]
Caption = ["東北一周旅行1枚目 東千葉->陸前山王",
           "東北一周旅行2枚目 陸前山王->東千葉",
           "東北一周旅行3枚目 宇都宮->日光(往復(ゆき))",
           "東北一周旅行4枚目 日光->宇都宮(往復(かえり))"]
ID = range(len(Date))


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", ID=ID, Date=Date, Caption=Caption)


@ticket.route("/ticket")
def ticket_view():
    id = int(request.args.get("id"))
    return render_template("ticket.html", id=id, preid=id-1, nextid=id+1, maxid=len(Date)-1, Date=Date, Caption=Caption)

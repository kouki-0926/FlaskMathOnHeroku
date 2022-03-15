from flask import request, redirect, url_for, render_template, flash, Blueprint, session

ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html")

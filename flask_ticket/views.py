from flask import Blueprint, render_template, request, redirect, url_for
from flask_ticket.ticket.tokyo import tokyo
from flask_ticket.ticket.kobe import kobe
from flask_ticket.ticket.ise_bousou_nagano import ise, bousou, nagano
from flask_ticket.ticket.kagoshima import kagoshima
from flask_ticket.ticket.tohoku import tohoku
from flask_ticket.ticket.hokaido import hokaido
from flask_ticket.ticket.hokuriku import hokuriku
from flask_ticket.ticket.food import food
from flask_ticket.ticket import index_info

ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", index_info=index_info)


@ticket.route("/<name>", methods=["GET"])
def list_view(name):
    page_id = request.args.get("page_id")
    if page_id is None:
        return redirect(url_for('ticket.list_view', name=name, page_id=0))
    else:
        page_id = int(page_id)

    NUM = 6  # 1ページに表示するチケットの数
    min_id = page_id * NUM
    if (min_id < 0 or min_id > len(globals()[name])):
        return redirect(url_for('ticket.list_view', name=name, page_id=0))

    max_id = min_id + NUM
    if (max_id > len(globals()[name])):
        max_id = len(globals()[name])
        page_id = int(max_id / NUM)

    return render_template("list_ticket.html", index_info=index_info, name=name, disp_info=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@ticket.route("/<name>/img<id>", methods=["GET"])
def ticket_view(name, id):
    return render_template("ticket.html", index_info=index_info, name=name, disp_info=globals()[name], id=int(id))

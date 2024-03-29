from flask import Blueprint, render_template, request, redirect, url_for

# 切符
from flask_ticket.ticket.tokyo import tokyo
from flask_ticket.ticket.kobe import kobe
from flask_ticket.ticket.ise import ise
from flask_ticket.ticket.kagoshima import kagoshima
from flask_ticket.ticket.bousou import bousou
from flask_ticket.ticket.nagano import nagano
from flask_ticket.ticket.tohoku import tohoku
from flask_ticket.ticket.hokaido import hokaido
from flask_ticket.ticket.hokuriku import hokuriku
from flask_ticket.ticket.internship import internship
from flask_ticket.ticket.shikoku import shikoku
from flask_ticket.ticket.nara import nara
from flask_ticket.ticket.si2023 import si2023
from flask_ticket.ticket.sanin import sanin
from flask_ticket.ticket import contents_ticket

# ブログ
from flask_ticket.blog.kobe_blog import kobe_blog
from flask_ticket.blog.shikoku_blog import shikoku_blog
from flask_ticket.blog import contents_blog


ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("ticket/index_ticket.html", contents_ticket=contents_ticket)


@ticket.route("/<name>", methods=["GET"])
def ticket_index_view(name):
    page_id = request.args.get("page_id")
    if page_id is None:
        return redirect(url_for('ticket.ticket_index_view', name=name, page_id=0))
    else:
        page_id = int(page_id)

    NUM = 6  # 1ページに表示するチケットの数
    min_id = page_id * NUM
    if (min_id < 0 or min_id > len(globals()[name])):
        return redirect(url_for('ticket.ticket_index_view', name=name, page_id=0))

    max_id = min_id + NUM
    if (max_id > len(globals()[name])):
        max_id = len(globals()[name])
        page_id = int(max_id / NUM)

    return render_template("ticket/ticket_index.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@ticket.route("/<name>/img<id>", methods=["GET"])
def ticket_view(name, id):
    return render_template("ticket/ticket.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], id=int(id))


# ============================ ブログ ============================
@ticket.route("/blog", methods=["GET"])
def blog_index_view():
    return render_template("blog/index_blog.html", contents_blog=contents_blog)


@ticket.route("/blog/trip_<trip_id>", methods=["GET"])
def blog_index_view2(trip_id):
    name = contents_blog[int(trip_id)][2]
    return render_template("blog/index_blog2.html", contents_blog=contents_blog, disp_contents=globals()[name], trip_id=int(trip_id))


@ticket.route("/blog/trip_<trip_id>/day_<day_id>", methods=["GET"])
def blog_view(trip_id, day_id):
    name = contents_blog[int(trip_id)][2]
    return render_template("blog/blog.html", contents_blog=contents_blog, disp_contents=globals()[name], trip_id=int(trip_id), day_id=int(day_id))


# ============================ 日本地図 ============================
@ticket.route("/map", methods=["GET"])
def map_view():
    return render_template("map/japan_map.html")
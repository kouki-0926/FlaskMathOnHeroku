from flask import Blueprint, render_template, request, redirect, url_for

# 切符
from flask_ticket.ticket.tokyo import tokyo
from flask_ticket.ticket.kobe import kobe
from flask_ticket.ticket.ise_bousou_nagano import ise, bousou, nagano
from flask_ticket.ticket.kagoshima import kagoshima
from flask_ticket.ticket.tohoku import tohoku
from flask_ticket.ticket.hokaido import hokaido
from flask_ticket.ticket.hokuriku import hokuriku
from flask_ticket.ticket.internship import internship
from flask_ticket.ticket.shikoku import shikoku
from flask_ticket.ticket import contents_ticket

# ブログ
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


@ticket.route("/blog/index", methods=["GET"])
def blog_index_view():
    return render_template("blog/index_blog.html", contents_blog=contents_blog)


@ticket.route("/blog/<name>", methods=["GET"])
def blog_index_view2(name):
    return render_template("blog/index_blog2.html", contents_blog=contents_blog, disp_contents=globals()[name])


@ticket.route("/blog/<name>/<day_id>", methods=["GET"])
def blog_view(name, day_id):
    return render_template("blog/blog.html", contents_blog=contents_blog, disp_contents=globals()[name], day_id=int(day_id))

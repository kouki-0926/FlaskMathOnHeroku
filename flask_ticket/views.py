from flask import Blueprint, render_template, request, redirect, url_for
import json

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


ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", contents_ticket=contents_ticket)


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

    return render_template("ticket_index.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@ticket.route("/<name>/img<id>", methods=["GET"])
def ticket_view(name, id):
    return render_template("ticket.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], id=int(id))


# blog
@ticket.route("/blog/map", methods=["GET"])
def map_view():
    return render_template("japan_map.html", contents_ticket=contents_ticket)


with open("flask_ticket/static_ticket/images/blog/image_info.json", "r", encoding='utf-8') as f:
    image_info = json.load(f)


@ticket.route("/blog/<pref_name>", methods=["GET"])
def blog_view(pref_name):
    pref_info = image_info[pref_name]
    centerCoordinates = [{"coords": pref_info["centerCoordinates"]}]
    markers = pref_info["markers"]
    return render_template("blog.html", contents_ticket=contents_ticket, pref_name=pref_name, centerCoordinates=centerCoordinates, markers=markers)

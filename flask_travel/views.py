from flask import Blueprint, render_template, request, redirect, url_for
import requests

# 切符
from flask_travel.travel.tokyo import tokyo
from flask_travel.travel.kobe import kobe
from flask_travel.travel.ise import ise
from flask_travel.travel.kagoshima import kagoshima
from flask_travel.travel.bousou import bousou
from flask_travel.travel.nagano import nagano
from flask_travel.travel.tohoku import tohoku
from flask_travel.travel.hokaido import hokaido
from flask_travel.travel.hokuriku import hokuriku
from flask_travel.travel.internship import internship
from flask_travel.travel.shikoku import shikoku
from flask_travel.travel.nara import nara
from flask_travel.travel.si2023 import si2023
from flask_travel.travel.sanin import sanin
from flask_travel.travel import contents_travel


travel = Blueprint("travel", __name__, template_folder='templates_travel', static_folder="static_travel")


@travel.route("/")
def index_view():
    return render_template("index_travel.html", contents_travel=contents_travel)


@travel.route("/<name>", methods=["GET"])
def travel_index_view(name):
    page_id = request.args.get("page_id")
    if page_id is None:
        return redirect(url_for('travel.travel_index_view', name=name, page_id=0))
    else:
        page_id = int(page_id)

    NUM = 6  # 1ページに表示するチケットの数
    min_id = page_id * NUM
    if (min_id < 0 or min_id > len(globals()[name])):
        return redirect(url_for('travel.travel_index_view', name=name, page_id=0))

    max_id = min_id + NUM
    if (max_id > len(globals()[name])):
        max_id = len(globals()[name])
        page_id = int(max_id / NUM)

    return render_template("travel_index.html", contents_travel=contents_travel, name=name, disp_contents=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@travel.route("/<name>/img<id>", methods=["GET"])
def travel_view(name, id):
    return render_template("travel.html", contents_travel=contents_travel, name=name, disp_contents=globals()[name], id=int(id))


# blog
@travel.route("/blog/map", methods=["GET"])
def map_view():
    return render_template("japan_map.html", contents_travel=contents_travel)


@travel.route("/blog/<pref_name>", methods=["GET"])
def blog_view(pref_name):
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/blog/image_info.json")
    image_info = response.json()

    if pref_name == "全国":
        centerCoordinates = [{"coords": [35.0, 135.0]}]
        markers = [marker for key in image_info.keys() for marker in image_info[key]["markers"]]
    else:
        centerCoordinates = image_info[pref_name]["centerCoordinates"]
        markers = image_info[pref_name]["markers"]
        pref_name = pref_name.split("_")[1]
    return render_template("blog.html", contents_travel=contents_travel, pref_name=pref_name, centerCoordinates=centerCoordinates, markers=markers)

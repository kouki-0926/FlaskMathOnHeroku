from flask import Blueprint, render_template, request, redirect, url_for
import requests

from flask_ticket.ticket.R0_Conference import conference
from flask_ticket.ticket.R0_Tokyo import tokyo
from flask_ticket.ticket.R1_Tokaido import tokaido
from flask_ticket.ticket.R3_Ise import ise
from flask_ticket.ticket.R3_Sanyo_Kyushu import sanyo_kyushu
from flask_ticket.ticket.R4_Bousou_Nagano import bousou_nagano
from flask_ticket.ticket.R4_Hokkaido import hokkaido
from flask_ticket.ticket.R4_Tohoku_Ou import tohoku_ou
from flask_ticket.ticket.R5_Hokuriku import hokuriku
from flask_ticket.ticket.R5_Internship import internship
from flask_ticket.ticket.R5_Nara import nara
from flask_ticket.ticket.R5_Shikoku import shikoku
from flask_ticket.ticket.R6_Kusatsu import kusatsu
from flask_ticket.ticket.R6_Kyushu import kyushu
from flask_ticket.ticket.R6_Okinawa import okinawa
from flask_ticket.ticket.R6_Sanin import sanin
from flask_ticket.ticket.R7_Takayama import takayama
from flask_ticket.ticket.R7_Tohoku_Uetsu import tohoku_uetsu
from flask_ticket.ticket.R7_Yamanashi import yamanashi

from flask_ticket.ticket import contents_ticket


ticket = Blueprint("ticket", __name__, template_folder="templates_ticket", static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", contents_ticket=contents_ticket)


# =========================== 切符 ===========================
@ticket.route("/<name>", methods=["GET"])
def ticket_index_view(name):
    page_id = request.args.get("page_id")
    if page_id is None:
        return redirect(url_for("ticket.ticket_index_view", name=name, page_id=0))
    else:
        page_id = int(page_id)

    NUM = 6  # 1ページに表示するチケットの数
    min_id = page_id * NUM
    if (min_id < 0 or min_id > len(globals()[name])):
        return redirect(url_for("ticket.ticket_index_view", name=name, page_id=0))

    max_id = min_id + NUM
    if (max_id > len(globals()[name])):
        max_id = len(globals()[name])
        page_id = int(max_id / NUM)

    return render_template("ticket_index.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@ticket.route("/<name>/img<id>", methods=["GET"])
def ticket_view(name, id):
    return render_template("ticket.html", contents_ticket=contents_ticket, name=name, disp_contents=globals()[name], id=int(id))


# =========================== 写真 ===========================
@ticket.route("/picture/map", methods=["GET"])
def picture_index_view():
    return render_template("picture_index.html", contents_ticket=contents_ticket)


@ticket.route("/picture/<pref_name>", methods=["GET"])
def picture_view(pref_name):
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
    image_info = response.json()

    if pref_name == "全国":
        centerCoordinates = [{"coords": [35.68, 139.75]}]
        markers = [marker for key in image_info.keys() for marker in image_info[key]["markers"]]
    else:
        centerCoordinates = image_info[pref_name]["centerCoordinates"]
        markers = image_info[pref_name]["markers"]
        pref_name = pref_name.split("_")[1]
    return render_template("picture.html", contents_ticket=contents_ticket, pref_name=pref_name, centerCoordinates=centerCoordinates, markers=markers)


# =========================== 駅名標 ===========================
@ticket.route("/station", methods=["GET"])
def station_view():
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
    image_info = response.json()

    station = []
    for key in image_info.keys():
        tmp_station = [[key.split("_")[1], ""]]

        for marker in image_info[key]["markers"]:
            if "駅名標_" in marker["title"]:
                tmp_station.append([marker["title"].split("駅名標_")[1], marker["photo"]])

        if len(tmp_station) > 1:
            station.append(tmp_station)

    return render_template("station.html", contents_ticket=contents_ticket, station=station)


# =========================== 駅舎 ===========================
@ticket.route("/station2", methods=["GET"])
def station2_view():
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
    image_info = response.json()

    station = []
    for key in image_info.keys():
        tmp_station = [[key.split("_")[1], ""]]

        for marker in image_info[key]["markers"]:
            if "駅舎_" in marker["title"]:
                tmp_station.append([marker["title"].split("駅舎_")[1], marker["photo"]])

        if len(tmp_station) > 1:
            station.append(tmp_station)

    return render_template("station.html", contents_ticket=contents_ticket, station=station)


# =========================== 城 ===========================
@ticket.route("/castles", methods=["GET"])
def castles_view():
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/castles/castles.json")
    image_info = response.json()

    castle_list = [[["日本100名城", ""]]]
    for castle_name in image_info.keys():
        for info in image_info[castle_name]:
            castle_list[0].append([castle_name + "(" + info["city"] + ")", info["photo"]])

    return render_template("station.html", contents_ticket=contents_ticket, station=castle_list)


# =========================== 経県値 ===========================
@ticket.route("/prefecturalEconomicValue", methods=["GET"])
def prefecturalEconomicValue_view():
    return render_template("prefecturalEconomicValue.html", contents_ticket=contents_ticket)

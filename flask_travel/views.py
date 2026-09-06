from flask import render_template, Blueprint, request, redirect, url_for, flash
import requests

from flask_travel.travel.R0_Conference import conference, conference_images, conference_stations
from flask_travel.travel.R0_Tokyo import tokyo, tokyo_images, tokyo_stations
from flask_travel.travel.R1_Tokaido import tokaido, tokaido_images, tokaido_stations
from flask_travel.travel.R3_Ise import ise, ise_images, ise_stations
from flask_travel.travel.R3_Sanyo_Kyushu import sanyo_kyushu, sanyo_kyushu_images, sanyo_kyushu_stations
from flask_travel.travel.R4_Bousou_Nagano import bousou_nagano, bousou_nagano_images, bousou_nagano_stations
from flask_travel.travel.R4_Hokkaido import hokkaido, hokkaido_images, hokkaido_stations
from flask_travel.travel.R4_Tohoku_Ou import tohoku_ou, tohoku_ou_images, tohoku_ou_stations
from flask_travel.travel.R5_Hokuriku import hokuriku, hokuriku_images, hokuriku_stations
from flask_travel.travel.R5_Internship import internship, internship_images, internship_stations
from flask_travel.travel.R5_Nara import nara, nara_images, nara_stations
from flask_travel.travel.R5_Shikoku import shikoku, shikoku_images, shikoku_stations
from flask_travel.travel.R6_Kusatsu import kusatsu, kusatsu_images, kusatsu_stations
from flask_travel.travel.R6_Kyushu import kyushu, kyushu_images, kyushu_stations
from flask_travel.travel.R6_Okinawa import okinawa, okinawa_images, okinawa_stations
from flask_travel.travel.R6_Sanin import sanin, sanin_images, sanin_stations
from flask_travel.travel.R7_Kii import kii, kii_images, kii_stations
from flask_travel.travel.R7_Nakasendo import nakasendo, nakasendo_images, nakasendo_stations
from flask_travel.travel.R7_Takayama import takayama, takayama_images, takayama_stations
from flask_travel.travel.R7_Tohoku_Uetsu import tohoku_uetsu, tohoku_uetsu_images, tohoku_uetsu_stations
from flask_travel.travel.R7_Tokai import tokai, tokai_images, tokai_stations
from flask_travel.travel.R7_Tottori import tottori, tottori_images, tottori_stations
from flask_travel.travel.R7_Yamanashi import yamanashi, yamanashi_images, yamanashi_stations

from flask_travel.travel import contents_travel, regions


travel = Blueprint("travel", __name__, template_folder="templates_travel", static_folder="static_travel")


@travel.route("/")
def index_view():
    return render_template("index_travel.html", contents_travel=contents_travel)


# =========================== 切符 ===========================
@travel.route("/<name>")
def ticket_index_view(name):
    page_id = request.args.get("page_id")
    if page_id is None:
        return redirect(url_for("travel.ticket_index_view", name=name, page_id=0))
    else:
        page_id = int(page_id)

    NUM = 6  # 1ページに表示するチケットの数
    min_id = page_id * NUM
    if (min_id < 0 or min_id > len(globals()[name])):
        return redirect(url_for("travel.ticket_index_view", name=name, page_id=0))

    max_id = min_id + NUM
    if (max_id > len(globals()[name])):
        max_id = len(globals()[name])
        page_id = int(max_id / NUM)

    return render_template("ticket_index.html", contents_travel=contents_travel, name=name, disp_contents=globals()[name], min_id=min_id, max_id=max_id, page_id=page_id)


@travel.route("/<name>/img<id>")
def ticket_view(name, id):
    return render_template("ticket.html", contents_travel=contents_travel, name=name, disp_contents=globals()[name], id=int(id))


@travel.route("/<name>/slideShow")
def slideShow_view(name):
    images = globals()[name + "_images"]
    stations = globals()[name + "_stations"]
    return render_template("slideShow.html", contents_travel=contents_travel, images=images, stations=stations)


# =========================== 写真 ===========================
@travel.route("/picture/map")
def picture_index_view():
    return render_template("picture_index.html", contents_travel=contents_travel)


@travel.route("/picture/<pref_name>")
def picture_view(pref_name):
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
    image_info = response.json()

    # pref_nameに応じて表示するマーカーを選択
    if pref_name == "全国":  # 全国
        markers = [marker for key in image_info.keys() for marker in image_info[key]["markers"]]
    elif pref_name in regions:  # 地方
        markers = [marker for key in regions[pref_name] for marker in image_info[key]["markers"]]
    elif pref_name in image_info:  # 都道府県
        markers = image_info[pref_name]["markers"].copy()
        pref_name = pref_name.split("_")[1]
    else:
        flash("地域または都道府県の名前が正しくありません。")
        return redirect(url_for("travel.picture_index_view"))

    # 駅名標と駅舎を非表示にする
    display_station = request.args.get("display_station", "true") == "true"
    if not display_station:
        markers = [marker for marker in markers if "駅名標_" not in marker["title"] and "駅舎_" not in marker["title"]]

    return render_template("picture.html", contents_travel=contents_travel, pref_name=pref_name, display_station=display_station, markers=markers)


# =========================== 駅名標 ===========================
@travel.route("/station")
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

    return render_template("station.html", contents_travel=contents_travel, station=station, title="駅名標")


# =========================== 駅舎 ===========================
@travel.route("/station2")
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

    return render_template("station.html", contents_travel=contents_travel, station=station, title="駅舎")


# =========================== PA/SA ===========================
@travel.route("/PASA")
def PASA_view():
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
    image_info = response.json()

    station = []
    for key in image_info.keys():
        tmp_station = [[key.split("_")[1], ""]]

        for marker in image_info[key]["markers"]:
            if "PA" in marker["title"] or "SA" in marker["title"] or "道の駅" in marker["title"]:
                tmp_station.append([marker["title"].replace("_", " "), marker["photo"]])

        if len(tmp_station) > 1:
            station.append(tmp_station)

    return render_template("station.html", contents_travel=contents_travel, station=station, title="パーキングエリア・サービスエリア・道の駅")


# =========================== 城 ===========================
@travel.route("/castles")
def castles_view():
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/castles/castles.json")
    image_info = response.json()

    unvisited_castle_cnt = image_info["unvisited_castle_cnt"]
    visited_castle_cnt = 100 - unvisited_castle_cnt
    del image_info["unvisited_castle_cnt"]

    station = []
    for key in image_info.keys():
        tmp_station = [[key + " ({}/{})".format(image_info[key]["visited"], image_info[key]["visited"] + image_info[key]["unvisited"]), ""]]

        for marker in image_info[key]["castle"]:
            tmp_station.append([marker["title"], marker["photo"]])

        if len(tmp_station) > 1:
            station.append(tmp_station)

    title = "日本100名城 (訪問済: {}/100, 未訪問: {}/100)".format(visited_castle_cnt, unvisited_castle_cnt)
    return render_template("station.html", contents_travel=contents_travel, station=station, title=title)


# =========================== 経県値 ===========================
@travel.route("/prefecturalEconomicValue")
def prefecturalEconomicValue_view():
    return render_template("prefecturalEconomicValue.html", contents_travel=contents_travel)

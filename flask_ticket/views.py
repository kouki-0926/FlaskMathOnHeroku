from flask import Blueprint, render_template, request, redirect, url_for
import requests

from flask_ticket.ticket.R0_Conference import conference
from flask_ticket.ticket.R0_Tokyo import tokyo
from flask_ticket.ticket.R1_Toukaido import toukaido
from flask_ticket.ticket.R3_Ise import ise
from flask_ticket.ticket.R3_Sanyou_Kyuusyu import sanyou_kyuusyu
from flask_ticket.ticket.R4_Bousou_Nagano import bousou_nagano
from flask_ticket.ticket.R4_Hokkaido import hokkaido
from flask_ticket.ticket.R4_Tohoku import tohoku
from flask_ticket.ticket.R5_Hokuriku import hokuriku
from flask_ticket.ticket.R5_Internship import internship
from flask_ticket.ticket.R5_Nara import nara
from flask_ticket.ticket.R5_Shikoku import shikoku
from flask_ticket.ticket.R6_Kusatsu import kusatsu
from flask_ticket.ticket.R6_Kyuusyu import kyuusyu
from flask_ticket.ticket.R6_Okinawa import okinawa
from flask_ticket.ticket.R6_Sanin import sanin

from flask_ticket.ticket import contents_ticket


ticket = Blueprint("ticket", __name__, template_folder='templates_ticket', static_folder="static_ticket")


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", contents_ticket=contents_ticket)


# =========================== 切符 ===========================
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


# =========================== 写真 ===========================
@ticket.route("/blog/map", methods=["GET"])
def map_view():
    return render_template("japan_map.html", contents_ticket=contents_ticket)


@ticket.route("/blog/<pref_name>", methods=["GET"])
def blog_view(pref_name):
    response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/blog/image_info.json")
    image_info = response.json()

    if pref_name == "全国":
        centerCoordinates = [{"coords": [35.68, 139.75]}]
        markers = [marker for key in image_info.keys() for marker in image_info[key]["markers"]]
    else:
        centerCoordinates = image_info[pref_name]["centerCoordinates"]
        markers = image_info[pref_name]["markers"]
        pref_name = pref_name.split("_")[1]
    return render_template("blog.html", contents_ticket=contents_ticket, pref_name=pref_name, centerCoordinates=centerCoordinates, markers=markers)


# =========================== 下車駅 ===========================
@ticket.route("/station", methods=["GET"])
def station_view():
    station = [["東海道本線",
                ["JO28", "#007ac1", "千葉駅"],
                ["JT01", "#f68b1e", "東京駅"],
                ["JT07", "#f68b1e", "大船駅"],
                ["JT16", "#f68b1e", "小田原駅"],
                ["JT18", "#f68b1e", "根府川駅"],
                ["CA00", "#f68b1e", "熱海駅"],
                ["CA02", "#f68b1e", "三島駅"],
                ["CA03", "#f68b1e", "沼津駅"],
                ["CA14", "#f68b1e", "清水駅"],
                ["CA17", "#f68b1e", "静岡駅"],
                ["CA37", "#f68b1e", "弁天島駅"],
                ["CA42", "#f68b1e", "豊橋駅"],
                ["CA68", "#f68b1e", "名古屋駅"],
                ["CA77", "#f68b1e", "大垣駅"],
                ["A12", "#0071be", "米原駅"],
                ["A13", "#0071be", "彦根駅"],
                ["A31", "#0071be", "京都駅"],
                ["A47", "#0071be", "大阪駅"],
                ["A63", "#0071be", "神戸駅"]]]
    return render_template("station.html", station=station)


# =========================== 旅行記録 ===========================
@ticket.route("/timeLine", methods=["GET"])
def timeLine_index_view():
    return render_template("timeLine_index.html")


@ticket.route("/timeLine/<name>", methods=["GET"])
def timeLine_view(name):
    return render_template("timeLine.html", disp_contents=globals()[name], name=name)

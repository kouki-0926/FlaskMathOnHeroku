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


# =========================== 動画 ===========================
@ticket.route("/slideShow", methods=["GET"])
def slideShow_view():
    images = ["東北一周旅行(東北・羽越)",
              [# 千葉駅
               ["R7/2/25", "12_千葉県/駅舎_千葉駅.jpg", "千葉駅 駅舎"],
               ["R7/2/25", "12_千葉県/駅名標_千葉駅_総武本線.jpg", "千葉駅 総武快速線"],
               # 東京駅
               ["R7/2/25", "13_東京都/駅名標_東京駅_在来線_地下ホーム.jpg", "東京駅 総武快速線"],
               ["R7/2/25", "13_東京都/駅舎_東京駅.jpg", "東京駅 駅舎"],
               ["R7/2/25", "13_東京都/駅名標_東京駅_東北新幹線.jpg", "東京駅 東北新幹線"],
               # 郡山駅
               ["R7/2/25", "07_福島県/駅名標_郡山駅_新幹線.jpg", "郡山駅 東北新幹線"],
               ["R7/2/25", "07_福島県/駅舎_郡山駅.jpg", "郡山駅 駅舎"],
               ["R7/2/25", "07_福島県/駅名標_郡山駅_在来線.jpg", "郡山駅 磐越西線"],
               # 会津若松駅
               ["R7/2/25", "07_福島県/駅名標_会津若松駅.jpg", "会津若松駅 磐越西線"],
               ["R7/2/25", "07_福島県/駅舎_会津若松駅.jpg", "会津若松駅 駅舎"],
               ["R7/2/25", "07_福島県/会津若松城.jpg", "会津若松城"],
               ["R7/2/25", "07_福島県/茶室麟閣.jpg", "茶室麟閣"],
               # 七日町駅
               ["R7/2/25", "07_福島県/駅舎_七日町駅.jpg", "七日町駅 駅舎"],
               ["R7/2/25", "07_福島県/駅名標_七日町駅.jpg", "七日町駅 只見線"],
               # 会津若松駅
               ["R7/2/25", "07_福島県/駅名標_会津若松駅.jpg", "会津若松駅 只見線"],
               ["R7/2/25", "07_福島県/駅舎_会津若松駅.jpg", "会津若松駅 駅舎"],
               ["R7/2/25", "07_福島県/駅名標_会津若松駅.jpg", "会津若松駅 磐越西線"],
               ["R7/2/25", "07_福島県/磐梯山.jpg", "磐梯山"],
               # 郡山駅
               ["R7/2/25", "07_福島県/駅名標_郡山駅_在来線.jpg", "郡山駅 磐越西線"],
               ["R7/2/25", "07_福島県/駅舎_郡山駅.jpg", "郡山駅 駅舎"],
               ["R7/2/25", "07_福島県/駅名標_郡山駅_新幹線.jpg", "郡山駅 東北新幹線"],
               # 福島駅
               ["R7/2/25", "07_福島県/駅名標_福島駅_新幹線.jpg", "福島駅 東北新幹線"],
               ["R7/2/25", "07_福島県/駅舎_福島駅.jpg", "福島駅 駅舎"],
               ["R7/2/25", "07_福島県/駅名標_福島駅_新幹線.jpg", "福島駅 東北新幹線"],
               # 仙台駅
               ["R7/2/25", "04_宮城県/駅名標_仙台駅_新幹線.jpg", "仙台駅 東北新幹線"],
               ["R7/2/25", "04_宮城県/駅舎_仙台駅_昼.jpg", "仙台駅 駅舎"],
               ["R7/2/25", "04_宮城県/AER展望テラス.jpg", "AER展望テラス"],
               ["R7/2/25", "04_宮城県/駅名標_仙台駅_新幹線.jpg", "仙台駅 東北新幹線"],
               # 新青森駅
               ["R7/2/25", "02_青森県/駅名標_新青森駅_新幹線.jpg", "新青森駅 東北新幹線"],
               ["R7/2/25", "02_青森県/駅舎_新青森駅.jpg", "新青森駅 駅舎"],
               ["R7/2/25", "02_青森県/駅名標_新青森駅_在来線.jpg", "新青森駅 奥羽本線"],
               # 青森駅
               ["R7/2/25", "02_青森県/駅名標_青森駅.jpg", "青森駅 東北新幹線"],
               ["R7/2/25", "02_青森県/駅舎_青森駅.jpg", "青森駅 駅舎"],
               ["R7/2/25", "02_青森県/青森駅_青森ベイブリッジ.jpg", "青森駅 青森ベイブリッジ"],
               ["R7/2/25", "02_青森県/駅名標_青森駅.jpg", "青森駅 奥羽本線"],
               # 新青森駅
               ["R7/2/25", "02_青森県/駅名標_新青森駅_在来線.jpg", "新青森駅 奥羽本線"],
               ["R7/2/25", "02_青森県/駅舎_新青森駅.jpg", "新青森駅 駅舎"],
               ["R7/2/25", "02_青森県/りんご自販機.jpg", "新青森駅 りんご自販機"],
               ["R7/2/25", "02_青森県/駅名標_新青森駅_新幹線.jpg", "新青森駅 東北新幹線"],
               # 盛岡駅
               ["R7/2/25", "03_岩手県/駅名標_盛岡駅_東北新幹線.jpg", "盛岡駅 東北新幹線"],
               ["R7/2/25", "03_岩手県/駅舎_盛岡駅.jpg", "盛岡駅 駅舎"],
               ["R7/2/26", "03_岩手県/駅名標_盛岡駅_秋田新幹線.jpg", "盛岡駅 秋田新幹線"],
               # 角館駅
               ["R7/2/26", "05_秋田県/駅名標_角館駅.jpg", "角館駅 秋田新幹線"],
               ["R7/2/26", "05_秋田県/駅舎_角館駅.jpg", "角館駅 駅舎"],
               ["R7/2/26", "05_秋田県/角館武家屋敷通り.jpg", "角館武家屋敷通り"],
               ["R7/2/26", "05_秋田県/河原田家.jpg", "河原田家"],
               ["R7/2/26", "05_秋田県/駅名標_角館駅.jpg", "角館駅 秋田新幹線"],
               # 秋田駅
               ["R7/2/26", "05_秋田県/駅名標_秋田駅_新幹線.jpg", "秋田駅 秋田新幹線"],
               ["R7/2/26", "05_秋田県/駅舎_秋田駅.jpg", "秋田駅 駅舎"],
               ["R7/2/26", "05_秋田県/駅名標_秋田駅_在来線.jpg", "秋田駅 羽越本線"],
               # 酒田駅
               ["R7/2/26", "06_山形県/駅名標_酒田駅.jpg", "酒田駅 羽越本線"],
               ["R7/2/26", "06_山形県/駅舎_酒田駅.jpg", "酒田駅 駅舎"],
               ["R7/2/26", "06_山形県/山居倉庫.jpg", "山居倉庫"],
               ["R7/2/26", "06_山形県/本間家旧本邸.jpg", "本間家旧本邸"],
               ["R7/2/26", "06_山形県/駅名標_酒田駅.jpg", "酒田駅 羽越本線"],
               ["R7/2/26", "15_新潟県/笹川流れ.jpg", "笹川流れ"],
               # 新発田駅
               ["R7/2/26", "15_新潟県/駅名標_新発田駅.jpg", "新発田駅 羽越本線"],
               ["R7/2/26", "15_新潟県/駅舎_新発田駅.jpg", "新発田駅 駅舎"],
               ["R7/2/26", "15_新潟県/新発田城.jpg", "新発田城"],
               ["R7/2/26", "15_新潟県/駅名標_新発田駅.jpg", "新発田駅 羽越本線"],
               # 新潟駅
               ["R7/2/26", "15_新潟県/駅名標_新潟駅_在来線.jpg", "新潟駅 羽越本線"],
               ["R7/2/26", "15_新潟県/駅舎_新潟駅.jpg", "新潟駅 駅舎"],
               ["R7/2/26", "15_新潟県/駅名標_新潟駅_新幹線.jpg", "新潟駅 上越新幹線"],
               # 東京駅
               ["R7/2/26", "13_東京都/駅名標_東京駅_東北新幹線.jpg", "東京駅 上越新幹線"],
               ["R7/2/26", "13_東京都/駅舎_東京駅.jpg", "東京駅 駅舎"],
               ["R7/2/26", "13_東京都/駅名標_東京駅_在来線_地下ホーム.jpg", "東京駅 総武快速線"],
               # 千葉駅
               ["R7/2/26", "12_千葉県/駅名標_千葉駅_総武本線.jpg", "千葉駅 総武快速線"],
               ["R7/2/26", "12_千葉県/駅舎_千葉駅.jpg", "千葉駅 駅舎"]]]
    return render_template("slideShow.html", images=images, contents_ticket=contents_ticket)

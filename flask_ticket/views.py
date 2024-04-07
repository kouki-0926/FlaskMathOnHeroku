import os
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
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


def get_gps_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif_data_decoded = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}

    gps_info = exif_data_decoded['GPSInfo']
    gps_data = {GPSTAGS.get(tag, tag): value for tag, value in gps_info.items()}

    latitude  = gps_data.get('GPSLatitude', None)
    longitude = gps_data.get('GPSLongitude', None)

    latitude  = float( latitude[0] +  latitude[1] / 60 +  latitude[2] / 3600)
    longitude = float(longitude[0] + longitude[1] / 60 + longitude[2] / 3600)
    return latitude, longitude


@ticket.route("/blog/<pref_name>", methods=["GET"])
def blog_view(pref_name):
    # 画像のパスを取得
    path = "flask_ticket/static_ticket/images/blog/" + pref_name + "/"
    file_list = os.listdir(path)
    path_list = [path + fileName for fileName in file_list]

    # 画像のGPS情報を取得
    coordinates_list = [get_gps_data(fileName) for fileName in path_list]
    centerCoordinates = [{"coords": [sum([coordinates_list[i][0] for i in range(len(coordinates_list))]) / len(coordinates_list),
                                     sum([coordinates_list[i][1] for i in range(len(coordinates_list))]) / len(coordinates_list)]}]
    markers = [{"title":  file_list[i].split(".")[0],
                "coords": coordinates_list[i],
                "photo":  path_list[i].replace("flask_ticket", "/ticket")} for i in range(len(path_list))]
    return render_template("blog.html", contents_ticket=contents_ticket, pref_name=pref_name, file_list=file_list, markers=markers, centerCoordinates=centerCoordinates)

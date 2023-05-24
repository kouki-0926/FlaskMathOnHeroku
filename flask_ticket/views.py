from flask import request, redirect, url_for, render_template, flash, Blueprint, session
from math import ceil
from flask_ticket.ticket.tokyo import tokyo
from flask_ticket.ticket.kobe import kobe
from flask_ticket.ticket.ise_bousou_nagano import ise, bousou, nagano
from flask_ticket.ticket.kagoshima import kagoshima
from flask_ticket.ticket.tohoku import tohoku
from flask_ticket.ticket.hokaido import hokaido
from flask_ticket.ticket.hokuriku import hokuriku


ticket = Blueprint("ticket", __name__,
                   template_folder='templates_ticket', static_folder="static_ticket")

# ===============================================================================
A = [tokyo, kobe, ise, kagoshima, bousou, nagano, tohoku, hokaido, hokuriku]
Date, Caption, imgNames = [[], [], []]
for i in range(len(A)):
    Date += A[i][0]
    Caption += A[i][1]
    imgNames += A[i][2]
ID = range(len(Date))

num = 7
maxPage = ceil(len(ID)/num)
# ===============================================================================
titles = ["東海道本線全線乗り通し",
          "伊勢神宮参拝",
          "山陽鹿児島本線全線乗り通し",
          "房総半島一周旅行",
          "長野旅行",
          "東北一周旅行",
          "北海道一周旅行",
          "北陸旅行"]
period = ["令和元年9月17日-9月21日",
          "令和3年8月25日",
          "令和3年9月11日-9月17日",
          "令和3年2月11日",
          "令和3年2月12日",
          "令和4年3月1日-3月8日",
          "令和4年8月30日-9月7日",
          "令和5年3月29日-4月2日"]
names = ["kobe", "ise", "kagoshima", "bousou",
         "nagano", "tohoku", "hokaido", "hokuriku"]
# ===============================================================================


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", titles=titles, period=period, names=names, CARD_NUM=len(titles), maxPage=maxPage)


@ticket.route("/<name>", methods=["GET"])
def list_view(name):
    return render_template("list_ticket.html", name=name, disp_info=globals()[name], maxPage=maxPage)


@ticket.route("/<name>/img<id>", methods=["GET"])
def ticket_view(name, id):
    return render_template("ticket.html", name=name, disp_info=globals()[name], id=int(id), maxPage=maxPage)

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

A = [tokyo, kobe, ise, kagoshima, bousou, nagano, tohoku, hokaido, hokuriku]
Date, Caption, imgNames = [[], [], []]
for i in range(len(A)):
    Date += A[i][0]
    Caption += A[i][1]
    imgNames += A[i][2]
ID = range(len(Date))

num = 7
maxPage = ceil(len(ID)/num)


@ticket.route("/")
def index_view():
    try:
        page = int(request.args.get("page"))
    except:
        page = 0

    if page < 0 or num*page > len(ID):
        return redirect(url_for("ticket.index_view"))

    if page == 0:
        prePage = 0
    else:
        prePage = page-1
    if page == maxPage-1:
        nextPage = page
        id2 = range(num*page, len(ID))
    else:
        nextPage = page+1
        id2 = range(num*page, num*nextPage)

    return render_template("index_ticket.html", ID=id2, Date=Date, Caption=Caption, imgNames=imgNames, prePage=prePage, page=page, nextPage=nextPage, maxPage=maxPage)


@ticket.route("/ticket")
def ticket_view():
    try:
        id = int(request.args.get("id"))
        return render_template("ticket.html", id=id, preid=id-1, nextid=id+1, maxid=len(Date)-1, Date=Date, Caption=Caption, imgName=imgNames[id], maxPage=maxPage)
    except:
        flash("id error")
        return redirect(url_for("ticket.index_view"))


@ticket.route("/title")
def title_view():
    titles = ["東海道本線全線乗り通し",
              "山陽本線鹿児島本線全線乗り通し",
              "東北1周旅行",
              "北海道1周旅行",
              "北陸旅行",
              "伊勢神宮参拝",
              "房総半島一周旅行",
              "長野旅行",
              "首都圏日帰り旅行"]
    period = ["令和元年9月17日-9月21日",
              "令和3年9月11日-9月17日",
              "令和4年3月1日-3月8日",
              "令和4年8月30日-9月7日",
              "令和5年3月29日-4月2日"]
    name = ["kobe", "kagoshima", "tohoku", "hokaido", "hokuriku",
            "ise", "bousou", "nagano", "tokyo"]
    return render_template("title.html", titles=titles, period=period, name=name, CARD_NUM=len(titles), maxPage=maxPage)

from flask import request, redirect, url_for, render_template, flash, Blueprint, session
from math import ceil
from flask_ticket.ticket.kagoshima import kagoshima
from flask_ticket.ticket.hokaido import hokaido
from flask_ticket.ticket.tohoku import tohoku

ticket = Blueprint("ticket", __name__,
                   template_folder='templates_ticket', static_folder="static_ticket")

Date = kagoshima[0]+tohoku[0]+hokaido[0]
Caption = kagoshima[1]+tohoku[1]+hokaido[1]
imgNames = kagoshima[2]+tohoku[2]+hokaido[2]
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

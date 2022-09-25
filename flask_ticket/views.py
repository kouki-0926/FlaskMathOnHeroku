from socket import IP_DROP_MEMBERSHIP
from flask import request, redirect, url_for, render_template, flash, Blueprint, session
from math import ceil

ticket = Blueprint("ticket", __name__,
                   template_folder='templates_ticket', static_folder="static_ticket")

kagoshima = [["R30911-R30915",
              "R30914",
              "R30914",
              "R30915",
              "R30916",
              "R30911"],
             ["山陽本線鹿児島本線1枚目 東千葉->八代",
              "山陽本線鹿児島本線2枚目 門司->門司港(往復(ゆき))",
              "山陽本線鹿児島本線3枚目 門司港->門司(往復(かえり))",
              "山陽本線鹿児島本線4枚目 肥薩おれんじ鉄道 八代->川内",
              "山陽本線鹿児島本線5枚目 川内->鹿児島",
              "山陽本線鹿児島本線6枚目 東海道山陽新幹線自由席特急券 東京->新神戸"],
             ["kagoshima/kagoshima"+str(i)+".jpg" for i in range(6)]]

tohoku = [["R40301-R40303",
          "R40303-R40308",
           "R40301",
           "R40301"],
          ["東北一周旅行1枚目 東千葉->陸前山王",
           "東北一周旅行2枚目 陸前山王->東千葉",
           "東北一周旅行3枚目 宇都宮->日光(往復(ゆき))",
           "東北一周旅行4枚目 日光->宇都宮(往復(かえり))"],
          ["tohoku/tohoku"+str(i)+".jpg" for i in range(4)]]

hokaido = [["R40830",
            "R40830",
            "R40831-R40906",
            "R40907",
            "R40907"],
           ["北海道一周旅行1枚目 千葉->空港第2ビル",
            "北海道一周旅行2枚目 新千歳空港->札幌",
            "北海道一周旅行3枚目 北海道フリーパス",
            "北海道一周旅行4枚目 札幌->新千歳空港",
            "北海道一周旅行5枚目 空港第2ビル->千葉"],
           ["hokaido/hokaido"+str(i)+".jpg" for i in range(5)]]

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
    else:
        nextPage = page+1

    return render_template("index_ticket.html", ID=range(num), Date=Date[num*page:num*(page+1)], Caption=Caption[num*page:num*(page+1)], prePage=prePage, page=page, nextPage=nextPage)


@ticket.route("/ticket")
def ticket_view():
    try:
        id = int(request.args.get("id"))
        return render_template("ticket.html", id=id, preid=id-1, nextid=id+1, maxid=len(Date)-1, Date=Date, Caption=Caption, imgName=imgNames[id])
    except:
        id = 0
        flash("id error")
        return redirect(url_for("ticket.index_view"))

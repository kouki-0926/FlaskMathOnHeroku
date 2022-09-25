from flask import request, redirect, url_for, render_template, flash, Blueprint, session

ticket = Blueprint("ticket", __name__,
                   template_folder='templates_ticket', static_folder="static_ticket")

kagoshima = [["R30911-R30915",
              "R30914",
              "R30914"],
             ["山陽本線鹿児島本線1枚目 東千葉->八代",
              "山陽本線鹿児島本線2枚目 門司->門司港(往復(ゆき))",
              "山陽本線鹿児島本線3枚目 門司港->門司(往復(かえり))"],
             ["kagoshima/kagoshima"+str(i)+".jpg" for i in range(3)]]

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


@ticket.route("/")
def index_view():
    return render_template("index_ticket.html", ID=ID, Date=Date, Caption=Caption)


@ticket.route("/ticket")
def ticket_view():
    id = int(request.args.get("id"))
    return render_template("ticket.html", id=id, preid=id-1, nextid=id+1, maxid=len(Date)-1, Date=Date, Caption=Caption, imgName=imgNames[id])

from flask import request, redirect, send_file, url_for, render_template, flash, Blueprint, session
from flask_game.Game import *
from PIL import Image, ImageDraw, ImageFont
import io


game = Blueprint("game", __name__, template_folder="templates_game", static_folder="static_game")


@game.route("/")
def index_view():
    return render_template("index_game.html")


@game.route("/janken")
def janken_view():
    n = request.args.get("n")
    type = request.args.get("type")
    if (type == "ml" or type == "rm"):
        if (n == "init"):
            session["result_ml"] = [0, 0, 0]
            session["result_rm"] = [0, 0, 0]
            return render_template("janken.html", type=type)
        elif (n == "reset"):
            session["result_ml"] = [0, 0, 0]
            session["result_rm"] = [0, 0, 0]
            flash("正常に勝敗結果が初期化されました")
            return render_template("janken.html", type=type)
        elif (n == "1" or n == "2" or n == "3"):
            if (type == "ml"):
                Anser = janken_ml.janken_ml(int(n), session.get("result_ml", "aaa"))
                session["result_ml"] = Anser[2]
            elif (type == "rm"):
                Anser = janken.janken(int(n), session.get("result_rm", "aaa"))
                session["result_rm"] = Anser[2]
            return render_template("janken.html", type=type, n=Anser[0][0], nc=Anser[0][1], Anser=Anser[1])
        else:
            return redirect(url_for("game.janken_view", type=type, n="init"))
    else:
        flash("Error:type")
        return redirect(url_for("game.janken_view", type="rm", n="init"))


@game.route("/box")
def box_view():
    return render_template("box.html")


@game.route("/bike")
def bike_view():
    return render_template("bike.html")


@game.route("/draw", methods=["GET", "POST"])
def draw_view():
    return render_template("draw.html")


@game.route("/draw_png", methods=["POST"])
def draw_png():
    file = request.files["draw_num"]
    image_data = file.read()

    # 数字認識
    result = recog_num.recog_num(image_data)

    # 認識結果を表示
    image = Image.open(io.BytesIO(image_data))
    output = Image.new("RGB", (image.width * 2, image.height), "white")
    output.paste(image, (0, 0))

    draw = ImageDraw.Draw(output)
    draw.text((image.width + image.width/2 - 50, image.height/2 - 100), str(result), fill="black", font=ImageFont.truetype("arial.ttf", 200))

    # PNGで返す
    output_data = io.BytesIO()
    output.save(output_data, format="PNG")
    output_data.seek(0)

    return send_file(output_data, mimetype="image/png")

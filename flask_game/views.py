from flask import request, redirect, send_file, url_for, render_template, flash, Blueprint, session, jsonify
from flask_game.Game import *
from PIL import Image, ImageDraw, ImageFont
import os, io
import base64


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


@game.route("/recog_num")
def recog_num_view():
    return render_template("recog_num.html")


@game.route("/recog_num_png", methods=["POST"])
def recog_num_png():
    file = request.files["draw_num"]
    image_data = file.read()

    # 前処理
    resized_image, image_array = recog_num.pre_process_image(image_data)

    # 数字認識
    result_nn, result_svm = recog_num.recog_num(image_array)

    # 認識結果を表示
    image = Image.open(io.BytesIO(image_data))
    output = Image.new("RGB", (image.width * 2, image.height), "white")
    output.paste(image, (0, 0))
    output.paste(resized_image.resize(image.size, Image.Resampling.NEAREST), (image.width, 0))

    # フォントのパスを指定
    FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static_game/fonts/LiberationSans-Regular.ttf")

    # テキストを描画
    draw = ImageDraw.Draw(output)
    draw.text((image.width * 0, 0), "original image", fill="black", font=ImageFont.truetype(FONT_PATH, 20))
    draw.text((image.width * 1, 0), "input image",    fill="black", font=ImageFont.truetype(FONT_PATH, 20))

    # 認識結果と画像をJSONで返す
    output_data = io.BytesIO()
    output.save(output_data, format="PNG")
    image_base64 = base64.b64encode(output_data.getvalue()).decode("utf-8")

    return jsonify({
        "image": image_base64,
        "result_nn": [[int(number), float(probability)] for number, probability in result_nn],
        "result_svm": [[int(number), float(probability)] for number, probability in result_svm]
    })

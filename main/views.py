from flask import render_template,flash,Blueprint

main=Blueprint("main",__name__,template_folder='templates_main',static_folder="static_main")

@main.route("/")
def index_view():
    return render_template("index_main.html")

@main.app_errorhandler(404)
def non_existant_route(error):
    flash("エラーコード：404　申し訳ございません. アクセスしたページは表示できません.")
    return render_template("404_error.html")

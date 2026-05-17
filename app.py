import sys
sys.dont_write_bytecode = True

import colorama
colorama.init()

from flask import Flask
app = Flask(__name__)
app.config.from_object("config")

from main.views import main
from flask_math.views import Math
from flask_tools.views import tools
from flask_game.views import game
from flask_travel.views import travel

app.register_blueprint(main)
app.register_blueprint(Math, url_prefix="/math")
app.register_blueprint(tools, url_prefix="/tools")
app.register_blueprint(game, url_prefix="/game")
app.register_blueprint(travel, url_prefix="/travel")


if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)

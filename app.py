import sys
sys.dont_write_bytecode = True

import colorama
colorama.init()

from flask import Flask
app = Flask(__name__)
app.config.from_object("config")

from main.views import main
from flask_math.views import Math
from flask_CPU.views import cpu
from flask_game.views import game
from flask_ticket.views import ticket

app.register_blueprint(main)
app.register_blueprint(Math, url_prefix="/math")
app.register_blueprint(cpu, url_prefix="/CPU")
app.register_blueprint(game, url_prefix="/game")
app.register_blueprint(ticket, url_prefix="/ticket")


if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)

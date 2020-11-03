import sys
sys.dont_write_bytecode = True
from flask import Flask

from flask_CPU.views import cpu
from flask_math.views import Math
from main.views import main

app=Flask(__name__)

app.config.from_object("config")
app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")

if __name__=="__main__":
    app.run()

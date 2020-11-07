import sys 
from flask import Flask

sys.dont_write_bytecode=True

from main.views import main
from flask_math.views import Math
from flask_CPU.views import cpu

app=Flask(__name__)

app.config.from_object("config")
app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")

if __name__=="__main__":
    app.run()

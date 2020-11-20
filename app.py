import sys 
from flask import Flask

sys.dont_write_bytecode=True

from main.views import main
from flask_math.views import Math
from flask_CPU.views import cpu
from flask_arduino.views import arduino

app=Flask(__name__)

app.config.from_object("config")
app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")
app.register_blueprint(arduino,url_prefix="/flask_arduino")

if __name__=="__main__":
    # app.run()
    app.run(host="0.0.0.0",port=5000)

from apscheduler.schedulers.background import BackgroundScheduler
import sys
sys.dont_write_bytecode = True
from flask import Flask

from flask_CPU.CPU.weather import update_weather
from flask_CPU.CPU.CPU import update_CPU
from flask_CPU.views import cpu
from flask_math.views import Math
from main.views import main

sched = BackgroundScheduler(standalone=True, coalesce=True)
sched.add_job(update_weather, 'interval', minutes=10)
sched.add_job(update_CPU, 'interval', minutes=10)
sched.start()

app=Flask(__name__)
app.config.from_object("config")

app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")

if __name__=="__main__":
    update_weather()
    app.run()

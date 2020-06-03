import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.moth == 1 and now.day == 1
    new_yaer = True
    return render_template("index.html", new_year=new_year)
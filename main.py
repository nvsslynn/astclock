from flask import Flask, url_for, render_template, jsonify
from datetime import datetime as dt

app = Flask(__name__)
_host = "0.0.0.0"

@app.route("/")
def index():
    return render_template("index.html", hour=22, min=31)

@app.route("/raw")
def rawpage():
    now = dt.now()
    return jsonify({
        "hour": now.strftime("%H"),
        "mins": now.strftime("%M"),
        "secs": now.strftime("%S")
    })


app.run(host=_host, port=5000)

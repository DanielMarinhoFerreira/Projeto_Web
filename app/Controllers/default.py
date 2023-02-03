from app import app
from flask import render_template
import os
from flask import send_from_directory

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    return render_template('Index.html')

@app.route("/Dashboard")
def dashboard():
    return render_template('Dashboard.html')
       
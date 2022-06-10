import os

from flask import Flask,flash, session, render_template,redirect, request
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
from flask_session import Session

import requests

load_dotenv()

app = Flask(__name__)


app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nombrevisual",methods=["POST" , "GET"])
def nombrevisual():

    if request.method == "POST":

        if not request.form.get("nombre"):
            flash("Llenar el campo solicitado")
            return render_template("nombrevisual.html")

            usuarios = request.form.get("nombre")
        
    else:
        return "hi"

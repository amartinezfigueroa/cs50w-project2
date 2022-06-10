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

lista_user= []

@app.route("/")
def index():
    return render_template("index.html")

#servidor
#@socketio.on('my event')
#def handle_message(data):
  #  print('received message: ' + data)
   # emit('my response', data)

@socketio.on('senduser')
def recibir_usuario(nombre):
    
    if nombre in lista_user:
        print(nombre)
        emit('Mensajes de alerta', "Este usuario ya existe")
    else:
        lista_user.append(nombre)
        emit('Registrar usuario', nombre)
    


if __name__ == '__main__':
    socketio.run(app)
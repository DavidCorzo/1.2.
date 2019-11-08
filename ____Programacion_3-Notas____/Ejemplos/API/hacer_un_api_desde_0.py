# Flask
from flask import Flask, jsonfy
import requests

app = Flask(__name__)

alumnos = {
    "Andrea": 19,
    "Katy": 17,
    "Fabricio": 18
}


# @app.route("/")
# @app.route("/estudiantes")
# def home():
#     return "<h1>ok</h1><br><h2>otro título"
# def home():
#     return jsonfy(estudiantes)
# def home():
#     return hacer_un_api_desde_0.send_static_file("index.html")

if __name__ == "__main__":
    # accesamos a la clase Flask y posteriormente al método run
    hacer_un_api_desde_0.run(host="0.0.0.0", debug=True)

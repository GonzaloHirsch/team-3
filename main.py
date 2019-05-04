from flask import Flask
from flask import render_template

import sys
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title = 'Projects')

@app.route("/feed/<career>")
def feed(career):
    if career=="sistemas":
        return json.dumps({"title": "Mi Dia Como Programador",
                            "body": "Hoy tuve una reunion muy interesante con el equipo de desarollo en el que definimos el modelo de la base de datos.",
                            "user": "juancito92",
                            "comments": {
                                "content": "Como se define una base de datos???",
                                "user": "pepito99"
                            }})
    if career=="economia":
        return json.dumps({"title": "Evento de Economia",
                            "body": "Hoy tuvimos un dia duro, cayo la bolsa y se perdieron 1.3 millones de dolares",
                            "user": "jorge23",
                            "comments": {
                                "content": "Que fue lo que paso??",
                                "user": "pepe49"
                            }})
    return []

@app.route("/wiki/<career>")
def wiki(career):
    if career=="sistemas":
        return json.dumps({"title": "Ingenieria en Sistemas",
                           "body": "Las facultades que tienen ingenieria en sistemas en argentina son ITBA, UBA, UTN, UCA y Austral."
        })

    return []

@app.route("/profile/<username>")
def profile(username):
    if username=="juancito92":
        return json.dumps({"user": "juancito92",
                            "posts": []
        })

    if username=="pepito99":
        return json.dumps({"user": "pepito99",
                            "posts": []
        })

    return []

@app.route("/admin/data")
def admin(data):
    return json.dumps({"amount": "52"
        })

    return []

@app.route("/user/<points>")
def user(points):
    if points=="low":
        return json.dumps({"amount": "50"
        })

    if points=="high":
        return json.dumps({"amount": "100"
        })

    return []

def initialize_server():
    app.run(host= '0.0.0.0') #,ssl_context='adhoc'

if __name__ == "__main__":
    initialize_server()
from flask import Flask
from flask import render_template

import sys
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")

@app.route("/feed/<career>")
def feedCareer(career):
    path_to_json = 'Jsons/' + career
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    jsons = {"posts":[]}
    for i in range(0,len(json_files)):  
        jsons["posts"].append(json.load(open(os.getcwd() + "\\Jsons\\" + str(career) + "\\" + json_files[i],"r")))
    return json.dumps(jsons)




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


def initialize_server():
    app.run(host= '0.0.0.0',debug=True) #,ssl_context='adhoc'

if __name__ == "__main__":
    initialize_server()


 
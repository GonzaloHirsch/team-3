from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    body = db.Column(db.String, unique=True, nullable=False)
    userID = db.Column(db.Integer, unique=True, nullable=False)

class WikiInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    career = db.Column(db.String, unique=True, nullable=False)
    info = db.Column(db.String, unique=True, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

db.session.add(User(name="Agus Osimani", email="agusosimani@itba.edu.ar"))
db.session.add(User(name="Gonza Hirsch", email="gonzahirsch@itba.edu.ar"))
db.session.add(Post(title="Dia de un ingeniero en informatica", body="Hoy fui mentor en una hackathon", userID="1"))
db.session.add(Post(title="Trabajo como ingeniero", body="Hoy ayude a organizar una hackathon", userID="2"))
db.session.add(WikiInfo(career="Ingenieria en informatica", info="Se estudia en ITBA, UBA, UTN y UADE"))
db.session.add(WikiInfo(career="Economia", info="Se estudia en UBA y UADE"))
db.session.add(WikiInfo(career="Medicina", info="Se estudia en CEMIC, UBA y Austral"))

db.session.commit()

def GetAllUsers():
	return User.query.all()

def GetAllWiki():
	return User.query.all()

def GetAllPosts():
	return User.query.all()
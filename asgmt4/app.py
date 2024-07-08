from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class rps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, primary_key=False)
    computer_choice = db.Column(db.String, primary_key=False)
    result = db.Column(db.String, primary_key=False)
    odds = db.Column(db.Integer, primary_key=False)

with app.app_context():
    db.create_all()

# 게임의 입출력을 Flask, HTML을 이용하도록

# DB에 게임 데이터 저장

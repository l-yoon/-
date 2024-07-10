from flask import Flask, render_template, request, redirect, url_for
import os
import random
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Rps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, primary_key=False)
    computer_choice = db.Column(db.String, primary_key=False)
    result = db.Column(db.String, primary_key=False)

with app.app_context():
    db.create_all()

options = ['가위', '바위', '보']

def get_computer_choice():
    return random.choice(options)

def winner(player_choice, computer_choice):
    if (player_choice == '가위' and computer_choice == '보') or \
        (player_choice == '바위' and computer_choice == '가위') or \
        (player_choice == '보' and computer_choice == '바위'):
        return '승리'
    elif player_choice == computer_choice:
        return '무승부'
    else:
        return '패배'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_choice = request.form['choice']
        computer_choice = get_computer_choice()
        result = winner(player_choice, computer_choice)

        game = Rps(user_choice=player_choice, computer_choice=computer_choice, result=result)
        db.session.add(game)
        db.session.commit()

        return redirect(url_for('result'))
    
    return render_template('index.html')

@app.route('/result')
def result():
    games = Rps.query.all()
    win = len(Rps.query.filter_by(result='승리').all())
    lose = len(Rps.query.filter_by(result='패배').all())
    draw = len(Rps.query.filter_by(result='무승부').all())

    stats = {
        '승리': win,
        '패배': lose,
        '무승부': draw
    }

    recent_games = Rps.query.order_by(Rps.id.desc()).limit(5).all()

    return render_template('result.html', stats=stats, recent_games=recent_games)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os
import random
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


# game logic
options = ['가위', '바위', '보']

get_computer_choice = random.choice(options)


def winner(player_choice, computer_choice):
    if (
        (player_choice == '가위' and computer_choice == '보')
            or (player_choice == '바위' and computer_choice == '가위')
            or (player_choice == '보' and computer_choice == '바위')):
        return '이겼음'

    elif player_choice == computer_choice:
        return '비겼음'

    else:
        return '졌음'

# 게임의 입출력을 Flask, HTML을 이용하도록
# 메인 페이지


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        player_choice = request.form['choice']
        computer_choice = get_computer_choice()
        result = winner(player_choice, computer_choice)

        if result == '이겼음':
            odds = 1
        elif result == '비겼음':
            odds = 0
        else:
            odds = -1

        game = rps(user_choice=player_choice,
                computer_choice=computer_choice, result=result, odds=odds)
        db.session.add(game)
        db.session.commit()

        return render_template('1page.html', player_choice=player_choice, computer_choice=computer_choice, result=result)

    return render_template('1page.html')


@app.route('/history')
def history():
    games = rps.query.all()
    return render_template('history.html', games=games)


if __name__ == "__main__":
    app.run(debug=True)

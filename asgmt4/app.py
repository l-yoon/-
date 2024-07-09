from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

import os
from flask_sqlalchemy import SQLAlchemy
import random

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Rps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.String, primary_key=False)
    computer_choice = db.Column(db.String, primary_key=False)
    result = db.Column(db.String, primary_key=False)
    odds = db.Column(db.Integer, primary_key=False)

with app.app_context():
    db.create_all()



# 게임의 입출력을 Flask, HTML을 이용하도록
@app.route("/main/", methods=['POST'])
def page1():        # 게임하는 창 + 모달

    # 버튼 to user_choice
    data = request.get_json()
    button_type = data['buttonType']

    if button_type == '가위':        # 수정
        user_choice = '가위'
    elif button_type == '바위':
        user_choice = '바위'
    else:
        user_choice = '보'

    # 페이지
    ## 조건문
    options = ['가위', '바위', '보']
    computer_choice = random.choice(options)

    if (
        (user_choice == '가위' and computer_choice == '보')
            or (user_choice == '바위' and computer_choice == '가위')
            or (user_choice == '보' and computer_choice == '바위')):
        result = "승리"
    elif user_choice == computer_choice:
        result = "무승부"
    else:
        result = "패배"

    ## 승률 구하기
    odds = (sum(len(Rps.query.filter_by(result='승리').all())) // len(Rps.query.filter_by(result).all()))*100       # 수정

    ## form에서 보낸 데이터 받아오기, DB에 저장
    rps = Rps(user_choice=user_choice, computer_choice=computer_choice, result=result, odds=odds)
    db.session.add(rps)
    db.session.commit()
    
    # 모달창
    # ## HTML 결과창 중앙 글씨 및 양쪽 짤(result에 따라 바꾸기) / JS로 하는게 더 나을듯
    # if result == '승리':
    #     pass
    # elif result == '패배':
    #     pass
    # else:
    #     pass



    ## 통계창으로 이동 버튼
    data = request.get_json()
    button_type = data['buttonType']

    if button_type == '통계':      # 수정
        return redirect(url_for('result'))

    ## retry 버튼
    if button_type == '다시하기':       # 수정
        return redirect(url_for('main'))


    pass

@app.route("/result/")       # 수정 / 통계창, 괄호 안 2page에 파일명 적기 / index.html이라면 index와 같은 방식
def page2():        # 기존 DB에서 꺼내오는 방식? or 라이브러리 추가 사용?
    # page2의 승무패 데이터 준비
    win = len(Rps.query.filter_by(result='승리').all())
    lose = len(Rps.query.filter_by(result='패배').all())
    draw = len(Rps.query.filter_by(result='무승부').all())

    context = {
        "win": win,
        "lose": lose,
        "draw": draw,
    }

    # 통계 보여주기

    # 다시하기 버튼
    data = request.get_json()
    button_type = data['buttonType']

    if button_type == '다시하기':        # 수정
        return redirect(url_for('main'))
    
    # HTML에 던져주기
    return render_template('result.html', context)


if __name__ == "__main__":
    app.run(debug=True)
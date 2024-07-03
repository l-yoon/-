class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


def create_member():
    name = input("이름을 입력하세요: ")
    uesrname = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    return Member(name, uesrname, password)


member = []

while True:
    question = input("새 회원을 등록하시겠습니까? (y/n): ")
    if question.lower() != 'y':
        break
    member = create_member()
    print(f"{member.name} 회원이 등록되었습니다.")

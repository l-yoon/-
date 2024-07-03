class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


def create_member():
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    return Member(name, username, password)


member = []

while True:
    question = input("새 회원을 등록하시겠습니까? (y/n): ")
    if question.lower() != 'y':
        break
    member = create_member()
    print(f"{member.name} 회원이 등록되었습니다.")


class Post():
    # __init__ = special methods.
    def __init__(self, username, title, content):
        self.author = username  # 인스턴스 변수 author
        self.title = title  # 인스턴스 변수 title
        self.content = content  # 인스턴스 변수 content

        while True:
            author_name = input("이름을 작성해주세요.")
            title_name = input("제목을 작성해주세요.")
            content_detail = input("내용을 작성해주세요.")
            if author_name == "" or title_name == "" or content_detail == "":  # 작성자, 제목, 내용 중 1개라도 입력이 안되어 있을 때 다시 입력하기
                print("내용을 입력안한 곳이 있습니다. 내용을 입력해주세요")
                continue  # 다시 input으로 되돌아감

            else:  # 작성자, 제목, 내용을 다 입력한 경우 출력됨
                print('글을 작성하셨습니다.')
                print(f"{self.author}:" + author_name)
                print(f"{self.title}:" + title_name)
                print(f"{self.content}:" + content_detail)
                break  # 반복문 종료


post = Post('작성자', '제목', '내용입력')
# post = self, Post = 객체, ()안에 있는 내용들은 init 메소드

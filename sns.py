import hashlib

#class
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")

class Post:
    def __init__(self, username, title, content):
        self.author = username  # 인스턴스 변수 author
        self.title = title  # 인스턴스 변수 title
        self.content = content  # 인스턴스 변수 content

    def display(self):
        print(f"아이디: {self.author}, 타이틀: {self.title}")

#input formulas 
def create_member():
    while True:
        name = input("이름을 입력하세요: ").strip()
        if name:  # Checks if 'name' is not empty
            break
        print("이름을 입력해주세요!")

    while True:
        username = input("아이디를 입력하세요: ").strip()
        if username:  # Checks if 'username' is not empty
            break
        print("아이디를 입력해주세요!")

    while True:
        password = input("비밀번호를 입력하세요: ").strip()
        if password:  # Checks if 'password' is not empty
            break
        print("비밀번호를 입력해주세요!")

    # 비밀번호 해시화
    passwd = hashlib.sha256()
    passwd.update(password.encode())
    encoded_pwd = passwd.hexdigest()
    return Member(name, username, encoded_pwd)

def create_post(author_name):
    while True:
        title_name = input("제목을 작성해주세요: ").strip()
        if title_name:
            break
        print("제목을 작성해주세요!")

    while True:
        content_detail = input("내용을 작성해주세요: ").strip()
        if content_detail:
            break
        print("내용을 작성해주세요!")
    
    return Post(author_name, title_name, content_detail)

# lists
members = []
posts = []

# members instances
members.append(Member("승원", "one1122", "qw1122"))
members.append(Member("원빈", "beanone", "bboo1122"))
members.append(Member("지민", "ming22", "password98"))
members.append(Member("리나", "rina0000", "qwerty@"))


# 맴버 추가 반복문
while True:
    question = input("새 회원을 등록하시겠습니까? (y/n): ").lower()
    if question == 'y':
        new_member = create_member()
        members.append(new_member)
        new_member.display()

        # 새 회원에게 세 개의 게시글 작성 요청
        for i in range(3):
            print(f"\n새 게시물 {i+1}/3 작성")
            new_post = create_post(new_member.username)
            posts.append(new_post)
            print('글을 작성하셨습니다.')
            print(f"작성자: {new_post.author}")
            print(f"제목: {new_post.title}")
            print(f"내용: {new_post.content}")
    elif question == 'n':
        print("다음단계")
        break
    else:
        print("올바른 값을 입력하세요!")

# 게시물 추가 반복문
while True:
    question = input("새 게시물을 등록하시겠습니까? (y/n): ").lower()
    if question == 'y':
        author_name = input("작성자 이름을 입력하세요: ").strip()
        new_post = create_post(author_name)
        posts.append(new_post)
        # 작성자, 제목, 내용을 다 입력한 경우 출력됨
        print('글을 작성하셨습니다.')
        print(f"작성자: {new_post.author}")
        print(f"제목: {new_post.title}")
        print(f"내용: {new_post.content}")

    elif question == 'n':
        print("다음 단계")
        break
    else:
        print("올바른 값을 입력하세요!")

# print 회원, 글 목록
print("회원 목록")
for member in members:
    member.display()

print("게시물 목록")
for post_list in posts:
    post_list.display()

# 특정 유저 작성 게시글 '제목'을 모두 프린트
def user_title():
    user_post = input('조회할 유저 아이디를 검색해주세요: ').strip()
    for post in posts:
        if post.author == user_post:
            print(post.title)

# 특정 단어가 content에 포함된 게시글의 '제목'을 모두 프린트
def keyword():
    word_post = input('조회할 특정 단어 게시글 조회: ').strip()
    for post in posts:
        if word_post in post.content:
            print(post.title)

#검색 반복문 
while True:
    k = input("유저 아이디를 검색하려면 a / 특정단어를 검색하고 싶으면 b 입력 / 취소(아무 키 입력):") # a 입력하면 특정유저가 작성한 게시글의 제목할 수 있는 페이지로 이동
    # b 입력하면 '특정 단어'가 내용에 포함된 게시글의 제목 출력

    if k == 'a': # 특정 유저 조회
        user_post = input('조회할 유저 아이디를 검색해주세요: ')
        for post in posts:
            if post.author == user_post:
                print(post.title)
        continue
    
    elif k == 'b':
        word_post = input('조회할 특정 단어 게시글 조회: ')
        for post in posts:
            if word_post in post.content:
                print(post.title)
        continue
    else:
        print("입력한 단어와 관련된 내용이 없습니다.")
        break

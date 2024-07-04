import hashlib


class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self.hash_password(password)

    def display(self):
        print(f"이름: {self.name}, 아이디: {self.username}")

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


class Post():
    def __init__(self, username, title, content):
        self.author = username  # 인스턴스 변수 author
        self.title = title  # 인스턴스 변수 title
        self.content = content  # 인스턴스 변수 content


def create_member():
    name = input("이름을 입력하세요: ")
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    return Member(name, username, password)

# def create_post(author):   # 경민님이 작성한 원래 코드
#     author_name = input("이름을 작성해주세요:")
#     title_name = input("제목을 작성해주세요:")
#     content_detail = input("내용을 작성해주세요:")
#     return Post(author_name, title_name, content_detail)


def create_post(author):   # 새로 변경 코드 밑에서 '아이디 = username' 를 입력 받아서 그 아이디에 해당하는 '작성자 = author'를 받아와 그 '작성자 = author'의 새 게시물이 작성할꺼임
    title_name = input("제목을 작성해주세요:")
    content_detail = input("내용을 작성해주세요:")
    return Post(author, title_name, content_detail)


# member instance
member1 = Member("승원", "one1122", "qw1122")
member2 = Member("원빈", "beanone", "bboo1122")
member3 = Member("지민", "ming22", "password98")
member4 = Member("리나", "rina0000", "qwerty@")

# member list
members = []

# member add
members.append(member1)
members.append(member2)
members.append(member3)
members.append(member4)


# 맴버 추가 반복문
while True:
    question = input("새 회원을 등록하시겠습니까? (y/n): ").lower()
    if question.lower() == 'y':
        member = create_member()
        members.append(member)
        print(f"{member.name} 회원이 등록되었습니다.")

    elif question.lower() == 'n':
        break
    else:
        print("y 또는 n을 다시 입력해주세요.")

print("\n회원 목록:")
for member in members:
    member.display()


# post list
posts = []

# post 추가 반복문 (경민님이 작성한 원래 코드)
# while True:
#     question = input("새 게시물을 등록하시겠습니까? (y/n): ").lower()
#     if question == 'y':
#         new_post = create_post()
#         posts.append(new_post)
#         # 작성자, 제목, 내용을 다 입력한 경우 출력됨
#         print('글을 작성하셨습니다.')
#         print(f"작성자: {new_post.author}")
#         print(f"제목: {new_post.title}")
#         print(f"내용: {new_post.content}")
#         break  # 반복문 종료

# 위 코드로 했을 경우 결과값
# 회원 목록:
# 이름: 승원, 아이디: one1122
# 이름: 원빈, 아이디: beanone
# 이름: 지민, 아이디: ming22
# 이름: 리나, 아이디: rina0000
# 이름: 홍길동, 아이디: 아이디
# 새 게시물을 등록하시겠습니까? (y/n): y
# 이름을 작성해주세요:홍길동 친구
# 제목을 작성해주세요:제목
# 내용을 작성해주세요:내용
# 글을 작성하셨습니다.
# 작성자: 홍길동 친구
# 제목: 제목
# 내용: 내용
# 회원 목록에 없는 새로운 이름으로 게시물이 생성
# 그래서 아래와 같이 변경
while True:    # 새로 작성한 코드
    response = input("\n새 게시글을 작성하시겠습니까? (y/n): ")
    if response.lower() != 'y':     # "새 게시글을 작성하시겠습니까?"의 물음에 y'가 아니면 멈춤
        break
    username = input("작성자의 아이디를 입력하세요: ")  # "새 게시글을 작성하시겠습니까?"의 물음에 'y'면 출력
    # 102 line 에서 '아이디=username'를 '입력'받고, member 리스트(member for member in members)안에 만약 입력받은 '아이디'에 해당하는 이름이 있으면 (if member.username == username) 'author'로 저장하고 없으면 'None'으로 반환 ( next(..., None) )
    author = next(
        (member for member in members if member.username == username), None)
    if author:                      # author인지, None인지 확인하고
        # author이면 새 게시글 작성하고,  # post는 위에 있는 create_post를 호출해서 게시글을 작성   ## 이 부분에서 author로 작성된 post 생성
        post = create_post(author.username)
        posts.append(post)                     # 작성된 post는 posts 리스트에 추가할꺼야
        print(f"'{post.title}' 게시글이 작성되었습니다.")
    else:
        # None 이면 해당 문구 출력  ## 입력한 '아이디=username'에 해당하는 이름을 찾을 수가 없음을
        print("해당 아이디의 회원을 찾을 수 없습니다.")

    # 특정 유저가 작성한 게시글 제목 출력
# 특정 유저 = 작성자의 아이디 = username 를 입력 받고,
username = input("\n게시글을 확인할 작성자의 아이디를 입력하세요: ")
# 특정 유저 = username이 작성한 게시글을 출력할꺼야.
print(f"\n{username}이(가) 작성한 게시글:")
for post in posts:                                                 # posts 리스트 안에서
    if post.author == username:                                    # 만약 위에서 입력한 username에 해당하는 author의 게시물이 있으면,
        # 게시물(post)의 제목(title)을 출력해
        print(post.title)

# 특정 단어가 포함된 게시글 제목 출력
# 특정 단어 = keyword를 입력받고
keyword = input("\n검색할 키워드를 입력하세요: ")
# 특정 단어가 포함된 게시글을 출력해
print(f"\n'{keyword}'가 포함된 게시글:")
for post in posts:                                                    # posts 리스트 안에서
    if keyword in post.content:                                       # 만약 게시글의 내용안에 keyword가 들어 있으면
        # 게시물(post)의 제목(title)을 출력해
        print(post.title)

    # 여기서 문제는 위에서 작성한 코드(경민님이 작성한 코드)

    #      def create_post(author):
    # title_name = input("제목을 작성해주세요:")
    # content_detail = input("내용을 작성해주세요:")
    # return Post(author, title_name, content_detail)

    # 이렇게 입력을 받았는데  title_name 또는  content_detail 를

    # if post.author == username:
    #     print(post.title_name)
    # if keyword in post.content:
    #     print(post.title)

    # 위와 같이 입력하면 작동이 안됨

    # 그리고
# member1 = Member("승원", "one1122", "qw1122")
# member2 = Member("원빈", "beanone", "bboo1122")
# member3 = Member("지민", "ming22", "password98")
# member4 = Member("리나", "rina0000", "qwerty@")

# 이 멤버들을
# 새 게시글을 작성하시겠습니까? (y/n): y
# 작성자의 아이디를 입력하세요: 승원         # 이 단계에서 입력하면
# 해당 아이디의 회원을 찾을 수 없습니다.     # 찾을 수가 없음

# 이건 내일 해야G.

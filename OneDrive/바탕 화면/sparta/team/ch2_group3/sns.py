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
        self.username = username  # 인스턴스 변수 username     # author 대신 username 사용하여 일관성 유지
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

def create_post(username):                              # 외부에서 '아이디 = username' 를 입력 받아서 그 아이디에 해당하는 작성자(name) 받아와 새 게시물 작성
    title_name = input("제목을 작성해주세요:")
    content_detail = input("내용을 작성해주세요:")
    return Post(username, title_name, content_detail)


# # member instance
# member1 = Member("승원", "one1122", "qw1122")
# member2 = Member("원빈", "beanone", "bboo1122")
# member3 = Member("지민", "ming22", "password98")
# member4 = Member("리나", "rina0000", "qwerty@")

# # member list
# members = []

# # member add
# members.append(member1)
# members.append(member2)
# members.append(member3)
# members.append(member4)

members = []                                            #위 코드 간소화 
members.append(Member("승원", "one1122", "qw1122"))
members.append(Member("원빈", "beanone", "bboo1122"))
members.append(Member("지민", "ming22", "password98"))


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

# (추가) 각 회원이 3개 이상의 게시글이 자동으로  작성하도록 수정
# 'members' 리스트에 있는 각 회원을 차례대로 하나씩 꺼내서 'member'에 저장
for member in members:
    for i in range(3):                                                                                                    # 'range(3)'은 숫자 0,1,2 생성. 이 반복문은 3번 반복  # 'i'는 첫번째 반복에서 '0'값을 갖고, 두번째 반복에서 '1', '세번째 반복에서는 '2'의 값을 가짐  # 따라서 각 회원마다 3번 반복하면서 3개의 게시글을 작성
        post = Post(                                                                                                      # 'member.username'은 새로운 게시글의 작성자 아이디이며, 이 아이디는 순회중인 'member'의 아이디를 사용.  # f"{member.username}의 게시글 제목 {i+1}"는 게시글의 제목. 예를 들어, i가 0일 때는 "회원아이디의 게시글 제목 1". #f"{member.username}의 게시글 내용 {i+1}"는 게시글의 내용. 예를 들어, i가 0일 때는 "회원아이디의 게시글 내용 1".
            member.username, f"{member.username}의 게시글 제목 {i+1}", f"{member.username}의 게시글 내용 {i+1}")            # 이렇게 하면 각 회원마다 3개의 서로 다른 제목과 내용을 가진 게시글이 생성.
        posts.append(post)

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

# 새로 작성한 게시물 작성 코드
while True:    
    response = input("\n새 게시글을 작성하시겠습니까? (y/n): ")
    if response.lower() == 'y':                                      # "새 게시글을 작성하시겠습니까?"의 물음에 'y'면 출력
        username = input("작성자의 아이디를 입력하세요: ")             # '아이디=username'를 '입력'받고,
        author = next(
            (member for member in members if member.username == username), None)
        if author:                                                  # author인지, None인지 확인해서  author이면 새 게시글 작성하고,  # post는 위에 있는 create_post를 호출해서 게시글을 작성   ## 이 부분에서 author로 작성된 post 생성
            post = create_post(author.username)
            posts.append(post)                                      # 작성된 post는 posts 리스트에 추가할꺼야
            print(f"'{post.title}' 게시글이 작성되었습니다.")
        else:
            print("해당 아이디의 회원을 찾을 수 없습니다.")           # None 이면 해당 문구 출력  ## 입력한 '아이디=username'에 해당하는 이름을 찾을 수가 없음을
    elif response.lower() == 'n':
        break
    else:
        print("y 또는 n을 다시 입력해주세요.")                       # 해당 부분 추가함으로써 '새 게시글을 작성하시겠습니까? (y/n): 1' 이렇게 입력되면 '게시글을 확인할 작성자의 아이디를 입력하세요:' 이렇게 출력되는 문제 해결

# 특정 유저가 작성한 게시글 제목 출력
username = input("\n게시글을 확인할 작성자의 아이디를 입력하세요: ")  # 특정 유저 = 작성자의 아이디 = username 를 입력 받고,
print(f"\n{username}이(가) 작성한 게시글:")                         # 특정 유저 = username이 작성한 게시글을 출력할꺼야.
for post in posts:                                                 # posts 리스트 안에서
    if post.username == username:                                   # 만약 위에서 입력한 입력받은 username과 동일한 username이 있으면,
        print(post.title)                                           # 게시물(post)의 제목(title)을 출력해

# 특정 단어가 포함된 게시글 제목 출력
# 특정 단어 = keyword를 입력받고
keyword = input("\n검색할 키워드를 입력하세요: ")                       # 특정 단어가 포함된 게시글을 출력해
print(f"\n'{keyword}'가 포함된 게시글:")
for post in posts:                                                    # posts 리스트 안에서
    if keyword in post.content:                                       # 만약 게시글의 내용안에 keyword가 들어 있으면
        print(post.title)                                             # 게시물(post)의 제목(title)을 출력해

    ## 'title_name'과 'content_detail'로 입력받은 값이 Post 객체의 'title'과 'content' 인스턴스 변수에 저장되는 이해하기 ## 

    # def create_post(username):                                  # 외부에서 받은 'username'의 이름으로 게시물을 작성
    #     title_name = input("제목을 작성해주세요:")                # 여기서 입력은 제목을 'title_name'에 저장
    #     content_detail = input("내용을 작성해주세요:")            # 여기서 입력 받은 내용을 'content_detail'에 저장
    #     return Post(username, title_name, content_detail)        # Post 클래스의 생성자를 호출하여 새로운 Post 객체를 만듭니다.

    # class Post:
    #     def __init__(self, username, title, content):            # Post 생성자의 __init__ 메서드가 호출되면서 다음과 같은 인자가 전달. 
    #         self.username = username  # 작성자의 아이디           # Post 클래스의 생성자(__init__ 메서드)가 'title_name'과 'content_detail'로 입력받은 값이 Post 객체의 'title'과 'content' 인스턴스 변수에 저장되도록 설계되었기 때문에
    #         self.title = title        # 게시글 제목               # 'title_name'과 'content_detail'은 create_post 함수 내에서 사용되는 변수명이고, 'title'과 'content'는 Post 클래스의 인스턴스 변수명.
    #         self.content = content    # 게시글 내용


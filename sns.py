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

def create_post():
    author_name = input("이름을 작성해주세요:")
    title_name = input("제목을 작성해주세요:")
    content_detail = input("내용을 작성해주세요:")
    return Post(author_name, title_name, content_detail)


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

print("추가된 회원 목록")
for member in members:
    member.display()

# 맴버 추가 반복문
while True:
    question = input("새 회원을 등록하시겠습니까? (y/n): ").lower()
    if question.lower() != 'y':
            break
    member = create_member()
    members.append(member)
    print(f"{member.name} 회원이 등록되었습니다.")
        

print("추가된 회원 목록")
for member in members:
    member.display()

# post list
posts = []

# post 추가 반복문
while True:
    question = input("새 게시물을 등록하시겠습니까? (y/n): ").lower()
    if question == 'y':
        new_post = create_post()
        posts.append(new_post)
        # 작성자, 제목, 내용을 다 입력한 경우 출력됨
        print('글을 작성하셨습니다.')
        print(f"작성자: {new_post.author}")
        print(f"제목: {new_post.title}")
        print(f"내용: {new_post.content}")
        break  # 반복문 종료



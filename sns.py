class Member:
    def __init__(self, name, member_id, password):
        self.name = name
        self.member_id = member_id
        self.password = password

    def display(self):
        print(f"NAME: {self.name}")
        print(f"ID: {self.member_id}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"제목: {self.title}")
        print(f"내용: {self.content}")
        print(f"작성자: {self.author.name}")


# ----- 코드 실행 ------
members = []
posts = []


# 멤버 추가
members.append(Member("회원 이름", "회원 ID", "보안 비밀번호"))

# 포스트 추가
posts.append(Post("첫 번째 글", "첫 번째 글입니다.", members[0]))

# 멤버 정보 출력
for member in members:
    member.display()
    print()

# 포스트 정보 출력
for post in posts:
    post.display()
    print()

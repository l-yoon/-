class Member:
    def __init__(self, name = [], username = [], password = [], members = []):
        self.name = name
        self.username = username
        self.password = password
        self.members = members
    
    def member_add(self):
        self.name.append(input('회원 이름을 입력해주세요: '))
        self.username.append(input('아이디를 입력해주세요: '))
        self.password.append(input('비밀번호를 입력해주세요: '))

    def display(self):
        # TODO : 코드 구현이 필요합니다.
        pass

    # members = [[이름1, 아이디1, 비번1], [이름2, 아이디2, 비번2]...]
    def mems_append(self):
        for i in range(len(self.name)):
            self.members.append([self.name[i], self.username[i], self.password[i]])

    # members 리스트를 돌면서 회원들의 이름을 모두 프린트
    def mems_print(self):
        for x in range(len(self.members)):
            print(self.members[x][0])


class Post:
    def __init__(self, title = [], content = [], author = [], posts = []):
        self.title = title
        self.content = content
        self.author = author
        self.posts = posts

    def post_add(self):
        self.title.append(input('피드 제목을 입력해주세요: '))
        self.content.append(input('피드 내용을 입력해주세요: '))



    # 각각 회원이 게시글 세개 이상 작성하게 하기
    def three_post(self):
        unique_author = set(self.author)

        # 중복제거이름 list에서 아이디(중복제거X)의 count 구하기

        while True:     # 이걸 class 안에 넣는다면?
            for z in unique_author:
                if self.author.count(z) < 3:
                    print(f"{z}의 게시글이 부족합니다. 추가해주세요")
                    # 다시 입력하게 하기
                    self.author.append(z)
                    self.title.append(input('피드의 제목을 입력: '))
                    self.content.append(input('피드의 내용을 입력: '))
                    break
            else:
                break

    # posts = [[제목1, 내용1, 이름1], [제목2, 내용2, 이름2]...]
    def posts_append(self):
        for j in range(len(self.title)):
            self.posts.append([self.title[j], self.content[j], self.author[j]])


    # 특정 유저 작성 게시글 '제목'을 모두 프린트
    def user_title(self):
        user_post = input('조회할 유저 아이디를 검색해주세요: ')

        for a in self.posts:
            if str(user_post).strip().lower() in str(a[2]).strip().lower():
                print(a[0])

    # 특정 단어가 content에 포함된 게시글의 '제목'을 모두 프린트
    def word_title(self):
        word_post = input('조회할 특정 단어 게시글 조회: ')

        for b in self.posts:
            if str(word_post).strip().lower() in str(b[1]).strip().lower():
                print(b[0])


# ----- 코드 실행 ------
m = Member()
p = Post()

p.author = m.username

m.member_add()
m.mems_append()
m.mems_print()

p.post_add()
p.three_post()
p.posts_append()

p.user_title()
p.word_title()
class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


#member instance
member1 = Member("승원","one1122","qw1122")
member2 = Member("원빈","beanone", "bboo1122")
member3 = Member("지민","ming22","password98")
member4 = Member("리나","rina0000","qwerty@")

members = []

members.append(member1)
members.append(member2)
members.append(member3)
members.append(member4)

for member in members:
    print(member.name)
class 학생:
    def __init__(self, 이름, 나이, 학과):
        self.이름 = 이름
        self.나이 = 나이
        self.학과 = 학과

    def 소개(self):
        print(f"저는 {self.이름}입니다. 나이는 {self.나이}살이고, 학과는 {self.학과}입니다.")

학생1 = 학생("홍길동", 20, "컴퓨터공학과")
학생2 = 학생("임종현", 28, "응용통계학과")
학생1.소개()
학생2.소개()

print("hi")
print("bye")
'''
robot1_name = "R1"
robot1_pos = 0


def robot1_move():
    global robot1_pos  # 전역변수 호출
    robot1_pos = robot1_pos + 1
    print("{0} position: {1}".format(robot1_name, robot1_pos))


robot2_name = "R2"
robot2_pos = 10


def robot2_move():
    global robot2_pos  # 전역변수 호출
    robot2_pos = robot2_pos + 1
    print("{0} position: {1}".format(robot2_name, robot2_pos))


robot1_move()
robot2_move()

할때마다 만들 순 없음, 비효율적 -> 클래스 생성
'''


class Robot():
    # 초기화 함수(인스턴스메소드)
    def __init__(self, name, pos):
        # 인스턴스 변수
        self.name = name
        self.pos = pos

    def move(self):
        self.pos = self.pos + 1
        print("{0} position:{1}".format(self.name, self.pos))


robot1 = Robot("R1", 1)
robot2 = Robot("R2", 11)

robot1.move()
robot2.move()

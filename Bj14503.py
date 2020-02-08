# 14503 로봇 청소기 https://www.acmicpc.net/problem/14503
# 29284 KB, 60 ms

# 로봇 청소기
class RobotCleaner:
    def __init__(self, r, c, d):
        self.cleanNum = 0
        self.r = r
        self.c = c
        self.d = d  # 0: 북, 1: 동, 2: 남, 3: 서

    # 현재 위치가 빈 칸이면 청소
    def clean(self):
        if room[self.r][self.c] == 0:
            self.cleanNum += 1
            room[self.r][self.c] = -1

    # 왼쪽으로 회전
    def turn_left(self):
        self.d = (self.d + 3) % 4

    # 한 칸 전진
    def moveFront(self):
        r = self.r
        c = self.c
        if self.d == 0: # 북
            r -= 1
        elif self.d == 1: # 동
            c += 1
        elif self.d == 2: # 남
            r += 1
        elif self.d == 3: # 서
            c -= 1
        if room[r][c] == 0:
            self.r = r
            self.c = c
            return 1
        else:
            return -1

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우
    def moveBack(self):
        r = self.r
        c = self.c
        if self.d == 0: # 북
            r += 1
        elif self.d == 1: # 동
            c -= 1
        elif self.d == 2: # 남
            r -= 1
        elif self.d == 3: # 서
            c += 1
        if room[r][c] == 1: # 벽인 경우
            return -1
        else: # 후진
            self.r = r
            self.c = c
            return 1

    def get_clean_num(self):
        return self.cleanNum

if __name__ == '__main__':
    N, M = map(int, input().split())  # 3 <= N, M <= 50
    r, c, d = map(int, input().split())
    global room
    room = []  # 0: 빈 칸, 1: 벽
    for _ in range(N):
        room.append(list(map(int, input().split())))

    robot = RobotCleaner(r, c, d)
    isKeep = True
    while(isKeep):
        robot.clean() # 1
        for i in range(4): # 2
            robot.turn_left()
            if robot.moveFront() == 1:
                break
            if i == 3 and robot.moveBack() == -1:
                isKeep = False
    print(robot.get_clean_num())
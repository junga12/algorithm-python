# https://www.acmicpc.net/problem/15683
# 29380 KB, 3860 ms

class Cctv:
    def __init__(self, x, y, type):
        self.position_x = x
        self.position_y = y
        self.type = type
        self.direction = 0
        if self.type == 2:
            self.last_direction = 2
        else:
            self.last_direction = 4

    def monitor(self, room):
        if self.type == 1:
            if self.direction == 0:
                monitor_left(self.position_x, self.position_y, room)
            elif self.direction == 1:
                monitor_down(self.position_x, self.position_y, room)
            elif self.direction == 2:
                monitor_right(self.position_x, self.position_y, room)
            else: # direction == 3
                monitor_up(self.position_x, self.position_y, room)
        elif self.type == 2:
            if self.direction == 0:
                monitor_left(self.position_x, self.position_y, room)
                monitor_right(self.position_x, self.position_y, room)
            else: # direction == 1:
                monitor_down(self.position_x, self.position_y, room)
                monitor_up(self.position_x, self.position_y, room)
        elif self.type == 3:
            if self.direction == 0:
                monitor_up(self.position_x, self.position_y, room)
                monitor_right(self.position_x, self.position_y, room)
            elif self.direction == 1:
                monitor_right(self.position_x, self.position_y, room)
                monitor_down(self.position_x, self.position_y, room)
            elif self.direction == 2:
                monitor_down(self.position_x, self.position_y, room)
                monitor_left(self.position_x, self.position_y, room)
            else:  # direction == 3
                monitor_left(self.position_x, self.position_y, room)
                monitor_up(self.position_x, self.position_y, room)
        else: # type == 4
            if self.direction == 0:
                monitor_up(self.position_x, self.position_y, room)
                monitor_right(self.position_x, self.position_y, room)
                monitor_left(self.position_x, self.position_y, room)
            elif self.direction == 1:
                monitor_right(self.position_x, self.position_y, room)
                monitor_down(self.position_x, self.position_y, room)
                monitor_up(self.position_x, self.position_y, room)
            elif self.direction == 2:
                monitor_down(self.position_x, self.position_y, room)
                monitor_left(self.position_x, self.position_y, room)
                monitor_right(self.position_x, self.position_y, room)
            else:  # direction == 3
                monitor_left(self.position_x, self.position_y, room)
                monitor_up(self.position_x, self.position_y, room)
                monitor_down(self.position_x, self.position_y, room)

    def next(self):
        self.direction += 1

    def isLast(self):
        if self.direction >= self.last_direction:
            return True
        else:
            return False

    def reset_direction(self):
        self.direction = 0

def monitor_up(x, y, room):
    x -= 1
    while x >= 0 and room[x][y] != 6:
        if room[x][y] <= 0:
            room[x][y] -= 1
        x -= 1

def monitor_down(x, y, room):
    x += 1
    while x < n and room[x][y] != 6:
        if room[x][y] <= 0:
            room[x][y] -= 1
        x += 1

def monitor_right(x, y, room):
    y += 1
    while y < m and room[x][y] != 6:
        if room[x][y] <= 0:
            room[x][y] -= 1
        y += 1

def monitor_left(x, y, room):
    y -= 1
    while y >= 0 and room[x][y] != 6:
        if room[x][y] <= 0:
            room[x][y] -= 1
        y -= 1

def monitor_cctv5(x, y, room):
    monitor_up(x, y, room)
    monitor_down(x, y, room)
    monitor_right(x, y, room)
    monitor_left(x, y, room)

def check(room):
    count = 0
    for rl in room:
        for r in rl:
            if r == 0:
                count += 1
    global answer
    if answer > count:
        answer = count

def dfs(cur, room): # dfs + brute force
    if cur == cctv_length:
        check(room)
    else:
        import copy
        while not cctv_list[cur].isLast():
            room2 = copy.deepcopy(room)
            cctv_list[cur].monitor(room2)
            dfs(cur+1, room2)
            for i in range(cur+1, cctv_length): # direction 초기화
                cctv_list[i].reset_direction()
            cctv_list[cur].next()

if __name__ == '__main__':
    answer = 64
    n, m = map(int, input().split()) # 1 ≤ N, M ≤ 8
    room = [list(map(int, input().split())) for _ in range(n)]
    cctv_list = [] # 5번을 제외한 cctv 리스트
    for i in range(n):
        for j in range(m):
            if room[i][j] == 5:
                monitor_cctv5(i, j, room)
            elif 0 < room[i][j] < 5:
                cctv_list.append(Cctv(i, j, room[i][j]))
    cctv_length = len(cctv_list)

    dfs(0, room)
    print(answer)
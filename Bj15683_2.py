# https://www.acmicpc.net/problem/15683
# 29380 KB, 4000 ms

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

def isLast(cctv):
    if cctv[2] == 2: # 2번 CCTV는 방향이 두 종류
        if cctv[3] == 2:
            return True
        else:
            return False
    else: # 나머지는 방향이 4종류
        if cctv[3] == 4:
            return True
        else:
            return False

def monitor(cctv, room):
    if cctv[2] == 1:
        if cctv[3] == 0:
            monitor_left(cctv[0], cctv[1], room)
        elif cctv[3] == 1:
            monitor_down(cctv[0], cctv[1], room)
        elif cctv[3] == 2:
            monitor_right(cctv[0], cctv[1], room)
        else: # cctv[3] == 3
            monitor_up(cctv[0], cctv[1], room)
    elif cctv[2] == 2:
        if cctv[3] == 0:
            monitor_left(cctv[0], cctv[1], room)
            monitor_right(cctv[0], cctv[1], room)
        else: # cctv[3] == 1:
            monitor_down(cctv[0], cctv[1], room)
            monitor_up(cctv[0], cctv[1], room)
    elif cctv[2] == 3:
        if cctv[3] == 0:
            monitor_up(cctv[0], cctv[1], room)
            monitor_right(cctv[0], cctv[1], room)
        elif cctv[3] == 1:
            monitor_right(cctv[0], cctv[1], room)
            monitor_down(cctv[0], cctv[1], room)
        elif cctv[3] == 2:
            monitor_down(cctv[0], cctv[1], room)
            monitor_left(cctv[0], cctv[1], room)
        else: # cctv[3] == 3
            monitor_left(cctv[0], cctv[1], room)
            monitor_up(cctv[0], cctv[1], room)
    else: # cctv[2] == 4
        if cctv[3] == 0:
            monitor_up(cctv[0], cctv[1], room)
            monitor_right(cctv[0], cctv[1], room)
            monitor_left(cctv[0], cctv[1], room)
        elif cctv[3] == 1:
            monitor_right(cctv[0], cctv[1], room)
            monitor_down(cctv[0], cctv[1], room)
            monitor_up(cctv[0], cctv[1], room)
        elif cctv[3] == 2:
            monitor_down(cctv[0], cctv[1], room)
            monitor_left(cctv[0], cctv[1], room)
            monitor_right(cctv[0], cctv[1], room)
        else: # cctv[3] == 3
            monitor_left(cctv[0], cctv[1], room)
            monitor_up(cctv[0], cctv[1], room)
            monitor_down(cctv[0], cctv[1], room)

def dfs(cur, room): # dfs + brute force
    if cur == cctv_length:
        check(room)
    else:
        import copy
        while not isLast(cctv_list[cur]):
            room2 = copy.deepcopy(room)
            monitor(cctv_list[cur], room2)
            dfs(cur+1, room2)
            for i in range(cur+1, cctv_length): # direction 초기화
                cctv_list[i][3] = 0
            cctv_list[cur][3] += 1

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
                cctv_list.append([i, j, room[i][j], 0])
    cctv_length = len(cctv_list)
    dfs(0, room)
    print(answer)
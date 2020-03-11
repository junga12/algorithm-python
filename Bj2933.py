# 2933 미네랄 https://www.acmicpc.net/problem/2933
# 런타임에러

'''
height = 막대를 던지는 높이
direction = 막대를 던지는 방향. True = 왼쪽, False = 오른쪽
'''
def removeCluster(height, direction):
    height = r - height
    # 클러스터 제거
    if direction:  # 막대 방향 = 왼쪽
        for i in range(c):
            if cave[height][i]:
                cave[height][i] = False
                break
    else:  # 막대 방향 = 오른쪽
        for i in range(c - 1, -1, -1):
            if cave[height][i]:
                cave[height][i] = False
                break

    # 클러스터 떨어뜨리기
    global isFloat
    isFloat = [[False] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if cave[i][j]:
                isFloat[i][j] = True
    isClusterInAir = False
    for i in range(c):
        if isFloat[r - 1][i]:
            check(r - 1, i)
            isClusterInAir = True
    if isClusterInAir:
        downCluster()

def downCluster():
    bottom = 0
    # 떨어뜨려야 하는 클러스터를 없앤다
    for i in range(r):
        for j in range(c):
            if isFloat[i][j]:
                cave[i][j] = False
                bottom = i
    # 내려야하는 칸 수 구하기
    isKeep = True
    downCount = 0
    while isKeep and bottom + downCount + 1 < r:
        downCount += 1  # 클러스터를 한 칸 내린다
        # 내릴 수 없으면 멈춘다
        for i in range(r):
            for j in range(c):
                if isKeep and isFloat[i][j] and cave[i + downCount][j]:
                    isKeep = False
                    downCount -= 1
                    break
    # 클러스터 내리기
    for i in range(r):
        for j in range(c):
            if isFloat[i][j]:
                cave[i + downCount][j] = True

# 공중에 떠있는 클러스터 검사
def check(x, y):
    isFloat[x][y] = False
    if x - 1 >= 0 and isFloat[x - 1][y]:
        check(x - 1, y)
    if x + 1 < r and isFloat[x + 1][y]:
        check(x + 1, y)
    if y - 1 >= 0 and isFloat[x][y - 1]:
        check(x, y - 1)
    if y + 1 < c and isFloat[x][y + 1]:
        check(x, y + 1)

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)

    r, c = map(int, input().split())
    cave = []  # True = 클러스터, False = 비어있음
    for _ in range(r):
        a = input()
        b = [False] * c
        for j in range(c):
            if a[j] == 'x':
                b[j] = True
        cave.append(b)

    n = int(input())
    throwHeights = list(map(int, input().split()))

    isFloat = []
    for i in range(n):
        removeCluster(throwHeights[i], i % 2 == 0)

    for i in cave:
        for j in i:
            if j:
                print('x', end='')
            else:
                print('.', end='')
        print()
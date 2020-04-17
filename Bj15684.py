# 15684 사다리 조작 https://www.acmicpc.net/problem/15684

def check():
    for i in range(1, n+1):
        cur = i
        for j in range(1, h+1):
            if cur > 0 and ladder[j][cur-1]:
                cur -= 1
            elif cur < n and ladder[j][cur]:
                cur += 1
        if cur != i:
            return False
    return True

def dfs(count, target_num): # count: 현재 개수, target_num: 추가할 선의 개수
    global answer
    if answer != -1:
        return

    if count == target_num:
        if check():
            answer = count
        return

    for i in range(1, h+1): # Todo: to next
        for j in range(1, n):
            if not ladder[i][j]: # and not ladder[i][j-1]:
                if j > 1 and ladder[i][j-1]: # Todo: edit to better way
                    continue
                if j+1 < n and ladder[i][j+1]:
                    continue
                ladder[i][j] = True
                dfs(count+1, target_num)
                ladder[i][j] = False


def printLadder():
    print("="*50)
    for i in ladder[1:]:
        for j in i:
            if j:
                print('O', end=' ')
            else:
                print('X', end=' ')
        print()

if __name__ == '__main__':
    n, m, h = map(int, input().split()) # 2 <= n <= 10, 0 <= m <= (n-1)*h, 1 <= h <= 30
    ladder = [[0] * n] + [[False] * n for _ in range(h)] # 가로선
    for _ in range(m):
        a, b = map(int, input().split()) # 1 <= a <= h, 1 <= b <= n-1
        ladder[a][b] = True

    MAX_NUM = 3
    answer = -1
    for i in range(MAX_NUM+1): # 추가할 선의 개수
        dfs(0, i)
        if (answer != -1):
            break
    print(answer)


# 9663 N-Queen https://www.acmicpc.net/problem/9663
# 159288 KB, 25260 ms

def check(x, y):
    ai = x - min(x, y)
    aj = y - min(x, y)
    bi = x + min(x, y)
    bj = y - min(x, y)
    for k in range(n):
        # 왼쪽 위에서 오른쪽 아래 방향
        if ai + k < n and aj + k < n and board[ai + k][aj + k] and ai + k != x:
            return False
        # 오른쪽 위에서 왼쪽 아래 방향
        if n > bi - k >= 0 and bj + k < n and board[bi - k][bj + k] and bi - k != x:
            return False
    return True

def dfs(a, s):
    global answer
    if a == n: # 퀸이 N개인 경우
        answer += 1
    else:
        for j in range(n):
            if isUsed[j] is False:
                isUsed[j] = True
                board[a][j] = True
                if check(a, j):
                    dfs(a + 1, s + 1)
                board[a][j] = False
                isUsed[j] = False

if __name__ == '__main__':
    n = int(input())
    board = [[False] * n for _ in range(n)]
    isUsed = [False] * n # 열
    answer = 0
    dfs(0, 1)
    print(answer)

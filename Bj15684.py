# 15684 사다리 조작 https://www.acmicpc.net/problem/15684
# 123720 KB, 1392 ms (PyPy3)

def check(): # 출력 조건오 부합하는지 검사
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

def dfs(curi, count, target_num): # count: 현재 개수, target_num: 추가할 선의 개수
    global answer
    if answer != -1:
        return
    if count == target_num:
        if check():
            answer = count
        return
    for i in range(curi, h+1):
        for j in range(1, n):
            if not ladder[i][j] and not ladder[i][j-1] and not ladder[i][j+1]:
                ladder[i][j] = True
                dfs(i, count+1, target_num)
                ladder[i][j] = False

if __name__ == '__main__':
    n, m, h = map(int, input().split()) # 2 <= n <= 10, 0 <= m <= (n-1)*h, 1 <= h <= 30
    ladder = [[False] * (n+1) for _ in range(h+1)] # 가로선
    for _ in range(m):
        a, b = map(int, input().split()) # 1 <= a <= h, 1 <= b <= n-1
        ladder[a][b] = True
    answer = -1
    for i in range(4):
        dfs(1, 0, i)
        if (answer != -1):
            break
    print(answer)


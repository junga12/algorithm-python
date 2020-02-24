# 14889 스타트와 링크 https://www.acmicpc.net/problem/14889
# 29284 KB, 6584 ms

def solve(cur, cnt):
    global mini
    if cnt == n/2:
        startScore, linkScore = 0, 0
        for i in range(n):
            for j in range(n):
                if startTeam[i] and startTeam[j]:
                    startScore += statsList[i][j]
                if not startTeam[i] and not startTeam[j]:
                    linkScore += statsList[i][j]
        if mini > abs(linkScore-startScore):
            mini = abs(linkScore-startScore)
    for i in range(cur+1, n):
        if startTeam[i] is False:
            startTeam[i] = True
            solve(i, cnt+1)
            startTeam[i] = False

if __name__ == '__main__':
    n = int(input()) # 4 <= n <= 20
    statsList = [list(map(int, input().split())) for _ in range(n)]
    mini = 100*20
    startTeam = [False] * n
    solve(0, 0)
    print(mini)
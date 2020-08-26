# #https://www.acmicpc.net/problem/13023
# 29380 KB, 1304 ms

def dfs(left, count, isVisited):
    global have_chain
    if not have_chain:
        if count == 4:
            have_chain = True
        else:
            isVisited[left] = True
            for f in friendship[left]:
                if not isVisited[f]:
                    dfs(f, count+1, isVisited)
                    isVisited[f] = False

if __name__ == '__main__':
    n, m = map(int, input().split()) # 5 <= n <= 20, 1 <= m <= 2000
    friendship = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        friendship[a].append(b)
        friendship[b].append(a)

    have_chain = False
    isVisited = [False] * n
    for i in range(n):
        dfs(i, 0, isVisited)
        isVisited[i] = False
        if have_chain:
            break

    if have_chain:
        print(1)
    else:
        print(0)
# https://www.acmicpc.net/problem/1260
# 29556 KB, 476 ms

def dfs(cur):
    global answer_dfs, is_visited
    answer_dfs.append(cur)
    is_visited[cur] = True
    for a in lines[cur]:
        if not is_visited[a]:
            dfs(a)

def bfs(start):
    is_visited = [False] * (n + 1)
    is_visited[start] = True
    answer_bfs = [v]
    queue = [start]
    while len(queue) != 0:
        cur = queue.pop(0)
        for a in lines[cur]:
            if not is_visited[a]:
                is_visited[a] = True
                queue.append(a)
                answer_bfs.append(a)
    return answer_bfs

if __name__ == '__main__':
    n, m, v = map(int, input().split()) # 1 <= n <= 1000, 1 <= m <= 10000
    lines = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        lines[a].append(b)
        lines[b].append(a)
    for i in range(n+1):
        lines[i] = sorted(list(set(lines[i])))
    answer_dfs, is_visited = [], [False] * (n + 1)
    dfs(v)
    print(*answer_dfs)
    print(*bfs(v))

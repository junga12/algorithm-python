# https://www.acmicpc.net/problem/1260
# 29380 KB, 496 ms

def dfs(start):
    is_visited = [False] * (n + 1)
    stack = [start]
    answer_dfs = []
    while stack:
        cur = stack.pop()
        if not is_visited[cur]:
            is_visited[cur] = True
            answer_dfs.append(cur)
            stack += reversed(lines[cur])
            # for a in reversed(lines[cur]):
            #     if not is_visited[a]:
            #         stack.append(a)
    return answer_dfs

def bfs(start):
    is_visited = [False] * (n + 1)
    is_visited[start] = True
    answer_bfs = [v]
    queue = [start]
    while queue:
        cur = queue.pop(0)
        for a in lines[cur]:
            if not is_visited[a]:
                is_visited[a] = True
                queue.append(a)
                answer_bfs.append(a)
    return answer_bfs

if __name__ == '__main__':
    import sys
    n, m, v = map(int, sys.stdin.readline().split()) # 1 <= n <= 1000, 1 <= m <= 10000
    lines = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        lines[a].append(b)
        lines[b].append(a)
    lines = list(map(lambda x : sorted(x), lines))
    print(*dfs(v))
    print(*bfs(v))

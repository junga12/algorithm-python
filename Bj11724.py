# https://www.acmicpc.net/problem/11724
# 62796 KB, 828 ms

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_visited = [False] * (n+1)
    answer = 0
    for start in range(1, n+1):
        if not is_visited[start]:
            is_visited[start] = True
            stack = [start]
            answer += 1
            while stack:
                cur = stack.pop()
                for g in graph[cur]:
                    if not is_visited[g]:
                        stack.append(g)
                        is_visited[g] = True
    print(answer)
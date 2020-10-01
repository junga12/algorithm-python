# https://www.acmicpc.net/problem/1325
# pypy3

import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    trust_relation = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        trust_relation[b].append(a)

    max = 0
    answer = []
    for num in range(1, n+1):
        q = [num]
        count = 0
        is_visited = [False] * (n+1)
        is_visited[num] = True
        while q:
            count += 1
            cur = q.pop()
            for tr in trust_relation[cur]:
                if not is_visited[tr]:
                    is_visited[tr] = True
                    q.append(tr)

        if count > max:
            max = count
            answer = [num]
        elif count == max:
            answer.append(num)

    answer.sort()
    print(*answer)
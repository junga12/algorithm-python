# https://www.acmicpc.net/problem/1916
# 42460 KB, 268 ms

import sys
import heapq
INF = 100000000

if __name__ == '__main__':
    n = int(sys.stdin.readline())  # 도시의 개수
    m = int(sys.stdin.readline())  # 버스의 개수
    distances = [[] for _  in range(n)]
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        distances[a-1].append((b-1, c))
    start, end = map(lambda x: int(x)-1, sys.stdin.readline().split())

    destination = [INF] * n
    destination[start] = 0
    hq = [(0, start)]
    while hq:
        dis, v = heapq.heappop(hq)
        if v == end: break
        if dis > destination[v]: continue
        for next, d in distances[v]:
            w = dis + d
            if w < destination[next]:
                destination[next] = w
                heapq.heappush(hq, (w, next))
    print(destination[end])
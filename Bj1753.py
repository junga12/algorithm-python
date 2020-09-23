# https://www.acmicpc.net/problem/1753
# 57904 KB, 696 ms

import sys
import heapq
INF = 200000000  # 문제에 나온 조건보다 큰 수

def make_string(list):
    return "\n".join(map(lambda x:"INF" if x == INF else str(x), vertexs))

if __name__ == '__main__':
    v, e = map(int, sys.stdin.readline().split())
    k = int(sys.stdin.readline()) - 1
    vertexs = [INF] * v
    vertexs[k] = 0

    edges = [{} for _ in range(v)]
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())
        if b-1 in edges[a - 1]:
            edges[a - 1][b - 1] = min(edges[a - 1][b - 1], c)
        else:
            edges[a - 1][b - 1] = c

    hq = [(0, k)]  # 최소힙. [거리, 정점]
    while hq:
        distance, selected = heapq.heappop(hq) # 가장 가까운 거리에 있는 정점을 선택
        if distance > vertexs[selected]: continue
        for _v, _w in edges[selected].items():
            if vertexs[_v] > distance + _w:
                vertexs[_v] = distance + _w
                heapq.heappush(hq, (vertexs[_v], _v))

    print(make_string(vertexs))

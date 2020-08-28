# https://www.acmicpc.net/problem/5014
# 70260KB, 764 ms

if __name__ == '__main__':
    import sys
    from collections import deque
    f, s, g, u, d = map(int, sys.stdin.readline().split()) # 1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000
    reachable_floors = [-1] * (f + 1)
    reachable_floors[s] = 0
    floors = deque([s])
    while floors:
        cur = floors.popleft()
        # if cur == g: break
        next1, next2 = cur + u, cur - d
        if next1 <= f and reachable_floors[next1] == -1:
            reachable_floors[next1] = reachable_floors[cur] + 1
            floors.append(next1)
        if next2 > 0 and reachable_floors[next2] == -1:
            reachable_floors[next2] = reachable_floors[cur] + 1
            floors.append(next2)
    if reachable_floors[g] != -1:
        print(reachable_floors[g])
    else:
        print("use the stairs")

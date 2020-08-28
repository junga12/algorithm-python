# https://www.acmicpc.net/problem/5014
# 37192 KB, 772 ms

def next_floor():
    global floors
    next_floor = []
    for floor in floors:
        next1, next2 = floor + u, floor - d
        if next1 <= f and not reachable_floors[next1]:
            next_floor.append(next1)
            reachable_floors[next1] = True
        if next2 > 0 and not reachable_floors[next2]:
            next_floor.append(next2)
            reachable_floors[next2] = True
    floors = next_floor
    return not reachable_floors[g] and bool(next_floor)

if __name__ == '__main__':
    import sys
    f, s, g, u, d = map(int, sys.stdin.readline().split()) # 1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000
    if s == g:
        print(0)
    else:
        reachable_floors = [False] * (f+1)
        reachable_floors[s] = True
        floors = [s]
        answer = 1
        while next_floor():
            answer += 1
        if reachable_floors[g]:
            print(answer)
        else:
            print("use the stairs")
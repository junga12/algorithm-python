# https://www.acmicpc.net/problem/2606

import sys

# 인접리스트
def solution1():
    computer_length = int(sys.stdin.readline())
    network_length = int(sys.stdin.readline())
    network = [[] for _ in range(computer_length)]
    for _ in range(network_length):
        a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
        network[a].append(b)
        network[b].append(a)
    isVisited = [True] + [False] * (computer_length-1)
    worm_virus = [0]  # 1번 컴퓨터가 감염
    answer = 0
    while worm_virus:
        wormed_computer = worm_virus.pop()
        for n in network[wormed_computer]:
            if not isVisited[n]:
                worm_virus.append(n)
                isVisited[n] = True
                answer += 1
    print(answer)


# 인접행렬
def solution2():
    computer_length = int(sys.stdin.readline())
    network_length = int(sys.stdin.readline())
    network = [[False]*computer_length for _ in range(computer_length)]
    for _ in range(network_length):
        a, b = map(lambda x: int(x)-1, sys.stdin.readline().split())
        network[a][b] = network[b][a] = True
    isVisited = [True] + [False] * (computer_length-1)
    worm_virus = [0]  # 1번 컴퓨터가 감염
    answer = 0
    while worm_virus:
        wormed_computer = worm_virus.pop()
        for i in range(computer_length):
            if not isVisited[i] and network[wormed_computer][i]:
                worm_virus.append(i)
                isVisited[i] = True
                answer += 1
    print(answer)

if __name__ == '__main__':
    solution2()

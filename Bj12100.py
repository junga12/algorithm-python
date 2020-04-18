# 12100 2048(Easy) https://www.acmicpc.net/problem/12100
# 29380	KB, 1064 ms

def move():
    import copy
    movingBoard = copy.deepcopy(board)
    for o in order:
        if o == 0: # 상
            for i in range(n):
                preNums = [0] * n
                k = 0
                for j in range(n):
                    if movingBoard[j][i] != 0:  # 0이 아니면
                        preNums[k] = movingBoard[j][i]
                        k += 1

                k = 0
                for j in range(n):
                    if k < n - 1 and preNums[k] == preNums[k + 1]:
                        movingBoard[j][i] = preNums[k] * 2
                        k += 2
                    else:
                        if k < n:
                            movingBoard[j][i] = preNums[k]
                            k += 1
                        else:
                            movingBoard[j][i] = 0
        elif o == 1: # 하
            for i in range(n):
                preNums = [0] * n
                k = 0
                for j in range(n-1, -1, -1):
                    if movingBoard[j][i] != 0:  # 0이 아니면
                        preNums[k] = movingBoard[j][i]
                        k += 1
                k = 0
                for j in range(n-1, -1, -1):
                    if k < n - 1 and preNums[k] == preNums[k + 1]:
                        movingBoard[j][i] = preNums[k] * 2
                        k += 2
                    else:
                        if k < n:
                            movingBoard[j][i] = preNums[k]
                            k += 1
                        else:
                            movingBoard[j][i] = 0
        elif o == 2: # 좌
            for i in range(n):
                preNums = [0] * n
                k = 0
                for j in range(n):
                    if movingBoard[i][j] != 0:  # 0이 아니면
                        preNums[k] = movingBoard[i][j]
                        k += 1

                k = 0
                for j in range(n):
                    if k < n-1 and preNums[k] == preNums[k+1]:
                        movingBoard[i][j] = preNums[k] * 2
                        k += 2
                    else:
                        if k < n:
                            movingBoard[i][j] = preNums[k]
                            k += 1
                        else:
                            movingBoard[i][j] = 0
        else: # 우
            for i in range(n):
                preNums = [0] * n
                k = 0
                for j in range(n-1, -1, -1):
                    if movingBoard[i][j] != 0:  # 0이 아니면
                        preNums[k] = movingBoard[i][j]
                        k += 1

                k = 0
                for j in range(n-1, -1, -1):
                    if k < n - 1 and preNums[k] == preNums[k + 1]:
                        movingBoard[i][j] = preNums[k] * 2
                        k += 2
                    else:
                        if k < n:
                            movingBoard[i][j] = preNums[k]
                            k += 1
                        else:
                            movingBoard[i][j] = 0

    global answer
    for i in range(n):
        for j in range(n):
            if answer < movingBoard[i][j]:
                answer = movingBoard[i][j]

def solution(count):
    if count == 5:
        move()
        return
    for i in range(4):
        order[count] = i
        solution(count + 1)

if __name__ == '__main__':
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    answer = 0
    order = [0] * 5  # 0:상, 1:하, 2:좌, 3:우
    solution(0)
    print(answer)
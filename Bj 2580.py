# 2580 스도쿠 https://www.acmicpc.net/problem/2580
# 122940 KB, 984 ns (Pypy3)

def printSudoku():
    print("-"*30)
    for i in sudoku:
        for j in i:
            print(j, end=' ')
        print()

def checkHorizontal(x, y): # 가로
    check = [False] * 10
    for i in range(9):
        check[sudoku[x][i]] = True
    for i in range(1, 10):
        if not check[i]:
            return i

def checkVirtical(x, y):  # 세로
    check = [False] * 10
    for i in range(9):
        check[sudoku[i][y]] = True
    for i in range(1, 10):
        if not check[i]:
            return i

def checkSquare(x, y):  # 3 x 3
    a, b = x // 3, y // 3
    cnt = 0
    check = [False] * 10
    for i in range(3):
        _x = a*3+i
        for j in range(3):
            _y = b*3+j
            check[sudoku[_x][_y]] = True
            if sudoku[_x][_y] == 0:
                cnt += 1
    if cnt == 1:
        for i in range(1, 10):
            if not check[i]:
                return i
    else:
        return -1

def findZero():
    zeroList = []
    horizontalCnt, virticalCnt = [0 for _ in range(9)], [0 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                zeroList.append([i, j])
                horizontalCnt[i] += 1
                virticalCnt[j] += 1
    return zeroList, horizontalCnt, virticalCnt

def dfs(cnt):
    if cnt == blankMaxNum:
        printSudoku()
        return True

    x, y = zeroList[cnt]
    isUsed = [False] * 10
    for i in range(9):
        isUsed[sudoku[x][i]] = True
        isUsed[sudoku[i][y]] = True
    for i in range(3):
        for j in range(3):
            isUsed[sudoku[(x//3)*3+i][(y//3)*3+j]] = True
    for i in range(1, 10):
        if not isUsed[i]:
            sudoku[x][y] = i
            if dfs(cnt+1):
                return True
            sudoku[x][y] = 0


if __name__ == '__main__':
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    zeroList, horizontalCnt, virticalCnt = findZero()

    pre = 0
    while(len(zeroList) != 0 and pre != len(zeroList)):
        pre = len(zeroList)
        for i, j in zeroList:
            if horizontalCnt[i] == 1:
                sudoku[i][j] = checkHorizontal(i, j)
            elif virticalCnt[j] == 1:
                sudoku[i][j] = checkVirtical(i, j)
            else:
                s = checkSquare(i, j)  # 3*3
                if s != -1:
                    sudoku[i][j] = s
            if sudoku[i][j] != 0:
                zeroList.remove([i, j])
                horizontalCnt[i] -= 1
                virticalCnt[j] -= 1

    blankMaxNum = len(zeroList)
    if blankMaxNum == 0:
        printSudoku()
    else:
        dfs(0)

'''
8 0 0 0 0 0 0 0 0
0 0 3 6 0 0 0 0 0
0 7 0 0 9 0 2 0 0
0 5 0 0 0 7 0 0 0
0 0 0 0 4 5 7 0 0
0 0 0 1 0 0 0 3 0
0 0 1 0 0 0 0 6 8
0 0 8 5 0 0 0 1 0
0 9 0 0 0 0 4 0 0
'''
'''
1. 확실한건 먼저 정하고, dps한다.
2. 3차원배열을 만들어서, boolean으로 직접참조해보기
'''
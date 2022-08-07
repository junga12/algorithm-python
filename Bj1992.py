# 0 = 전부 흰색
# 1 = 전부 검은색
# -1 = 섞여있음음
def getColor(x1, y1, x2, y2):
    allWhite = True
    allBlack = True
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if allBlack and board[i][j] == '0':
                allBlack = False
            elif allWhite and board[i][j] == '1':  # 1
                allWhite = False
            if not allBlack and not allWhite:
                return -1
    if allWhite:
        return 0
    return 1  # allBlack


def Compression(x1, y1, x2, y2):
    color = getColor(x1, y1, x2, y2)
    if color == -1:
        mid = (x2 - x1) // 2
        if mid == 0:  # 사이즈가 2*2로 더이상 나눌 수 없는 경우
            return '(' + str(board[x1][y1]) + str(board[x1][y2]) + str(board[x2][y1]) + str(board[x2][y2]) + ')'
        return '(' + Compression(x1, y1, x1 + mid, y1 + mid) + Compression(x1, y1 + mid + 1, x1 + mid, y2) + \
               Compression(x1 + mid + 1, y1, x2, y1 + mid) + Compression(x1 + mid + 1, y1 + mid + 1, x2, y2) + ')'
    else:
        return str(color)


if __name__ == '__main__':
    n = int(input())
    board = [input() for _ in range(n)]
    print(Compression(0, 0, n - 1, n - 1))
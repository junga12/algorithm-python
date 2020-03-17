# 1987 알파벳 https://www.acmicpc.net/problem/1987
# 148900 KB, 4788 ms (PyPy3)

def charToNum(c):
    return ord(c) - ord('A')

def isAnswer(cnt):
    global answer
    if cnt > answer:
        answer = cnt

def next(x, y, cnt):
    if 0 <= x < r and 0 <= y < c:
        ctn = charToNum(alphabets[x][y])
        if not isUsed[ctn]:
            isUsed[ctn] = True
            next(x, y+1, cnt+1)
            next(x, y-1, cnt+1)
            next(x-1, y, cnt+1)
            next(x+1, y, cnt+1)
            isUsed[ctn] = False
        else:
            isAnswer(cnt)
    else:
        isAnswer(cnt)

if __name__ == '__main__':
    r, c = map(int, input().split())  # 1 <= r, c <= 20
    alphabets = [list(input()) for _ in range(r)]
    isUsed = [False] * 26
    answer = 0
    next(0, 0, 0)
    print(answer)
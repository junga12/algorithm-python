# 1987 알파벳 https://www.acmicpc.net/problem/1987
# 145768 KB, 5112 ms (PyPy3)

def charToNum(c):
    return ord(c) - ord('A')

def next(x, y, cnt):
    global answer
    if 0 <= x < r and 0 <= y < c and not isUsed[charToNum(alphabets[x][y])]:
        isUsed[charToNum(alphabets[x][y])] = True
        next(x, y+1, cnt+1)
        next(x, y-1, cnt+1)
        next(x-1, y, cnt+1)
        next(x+1, y, cnt+1)
        isUsed[charToNum(alphabets[x][y])] = False
    else:
        if cnt > answer:
            answer = cnt

if __name__ == '__main__':
    r, c = map(int, input().split())  # 1 <= r, c <= 20
    alphabets = [list(input()) for _ in range(r)]
    isUsed = [False] * 26
    answer = 0
    next(0, 0, 0)
    print(answer)

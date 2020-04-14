# 1759 암호 만들기 https://www.acmicpc.net/problem/1759
# 29380 KB, 84 ms

def dfs(start, sum, aeiou):
    if sum == l:
        if aeiou > 0 and l-aeiou > 1: # 모음 1개 이상, 자음 2개 이상
            for i in range(c):
                if isVisited[i]:
                    print(alphabets[i], end='')
            print()
        return
    for i in range(start, c):
        if not isVisited[i]:
            isVisited[i] = True
            if alphabets[i] in AEIOU:
                aeiou += 1
            dfs(i+1, sum+1, aeiou)
            if alphabets[i] in AEIOU:
                aeiou -= 1
            isVisited[i] = False

if __name__ == '__main__':
    AEIOU = ['a', 'e', 'i', 'o', 'u'] # 모음
    l, c = map(int, input().split())  # 3 <= l <= c <= 15
    alphabets = sorted(list(map(str, input().split())))
    isVisited = [False] * c
    dfs(0, 0, 0)
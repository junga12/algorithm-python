# https://www.acmicpc.net/problem/16937
# 29380 KB, 76 ms

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    h, w = map(int, input().split())
    n = int(input())
    stickers = []
    for _ in range(n):
        r, c = map(int, input().split())
        sticker = []
        if h >= r and w >= c:
            sticker.append([r, c])
        if r != c and h >= c and w >= r:
            sticker.append([c, r])
        if sticker:
            stickers.append(sticker)
    from itertools import combinations
    from itertools import product
    stickers_combination = list(combinations(stickers, 2))
    answer = 0
    for sticker1, sticker2 in stickers_combination:
        sticker_product = list(product(sticker1, sticker2))
        for a, b in sticker_product:
            if a[0] + b[0] <= h or a[1] + b[1] <= w:
                answer = max(answer, (a[0]*a[1]) + (b[0]*b[1]))
    print(answer)

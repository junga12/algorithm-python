# https://www.acmicpc.net/problem/16917
# 29380 ms, 64 ms

if __name__ == '__main__':
    import sys
    a, b, c, x, y = map(int, sys.stdin.readline().split())
    m = min(x, y)
    print(min(2 * m * c + a * (x-m) + b * (y - m), max(x, y) * 2 * c, x * a + y * b))
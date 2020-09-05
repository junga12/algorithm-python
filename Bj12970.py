# https://www.acmicpc.net/problem/12970
# 29380 KB, 60 ms

if __name__ == '__main__':
    import sys
    n, k = map(int, sys.stdin.readline().split())
    a, b = 0, n # A의 개수, B의 개수
    while (k > a*b and b > 0):
        a += 1
        b -= 1
    if b == 0:
        print(-1)
    elif a == 0:
        print("B"*b)
    else:
        remain = k - (b * (a-1))
        print("A"*(a-1)+"B"*(b-remain)+"A"+"B"*remain)
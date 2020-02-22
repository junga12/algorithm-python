# 9095 1, 2, 3 더하기 https://www.acmicpc.net/problem/9095
# 29284 KB, 56 ms

if __name__ == '__main__':
    t = int(input())
    num = [0, 1, 2, 4] + [0] *7
    for i in range(4, 11):
        num[i] = sum(num[i-3:i])
    for _ in range(t):
        print(num[int(input())])
# https://www.acmicpc.net/problem/1463
# 68592 KB, 716 ms

if __name__ == '__main__':
    n = int(input())
    answer = [i-1 for i in range(n+1)]
    for i in range(3, n+1):
        answer[i] = min(answer[i-1]+1, answer[i//3]+1 if i%3==0 else n, answer[i//2]+1 if i%2==0 else n)
    print(answer[n])


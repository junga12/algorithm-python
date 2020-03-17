# 10819 차이를 최대로 https://www.acmicpc.net/problem/10819
# 29284 KB, 276 ms

def dfs(cur, cnt):
    global order, answer
    if cnt == n: # 순열 완성
        s = 0
        for j in range(n-1):
            s += abs(order[j] - order[j+1])
        if s > answer:
            answer = s
    for i in range(n):
        if not isUsed[i]:
            order.append(nums[i])
            isUsed[i] = True
            dfs(cur+1, cnt+1)
            order = order[:-1]
            isUsed[i] = False

if __name__ == '__main__':
    n = int(input()) # 3 <= n <= 8
    nums = list(map(int, input().split()))
    order = []
    isUsed = [False] * n

    answer = 0
    dfs(0, 0)
    print(answer)
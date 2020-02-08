# 2529 부등호 https://www.acmicpc.net/problem/2529
# 29284 KB, 208 ms

def check(op, a, b):
    if op == '<':
        return a < b
    else:
        return a > b

def findMin(cnt, nums):
    global maxNum, minNum
    if cnt == k+1:
        if not minNum:
            minNum = nums
        maxNum = nums
        return
    for i in range(10):
        if not isUsed[i]:
            if cnt == 0 or check(ops[cnt-1], nums[-1], str(i)):
                isUsed[i] = True
                findMin(cnt+1, nums + str(i))
                isUsed[i] = False

if __name__ == '__main__':
    k = int(input()) # 2 <= k <= 9
    ops = list(map(str, input().split()))
    isUsed = [False for _ in range(10)]
    maxNum, minNum = "", ""
    findMin(0, "")
    print(maxNum)
    print(minNum)


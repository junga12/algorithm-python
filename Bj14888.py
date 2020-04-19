# 14888 연산자 끼워넣기 https://www.acmicpc.net/problem/14888
# 122384 KB, 2620 ms

def dfs(val, cur, count, opCount):
    global maxAnswer, minAnswer
    print(count)
    if count == N-1:
        if val < minAnswer:
            minAnswer = val
        if val > maxAnswer:
            maxAnswer = val
    else:
        for i in range(0, N-1):
            if isVisited[i] is False:
                isVisited[i] = True
                if op[i] == 0:  # 덧셈
                    dfs(val + A[count + 1], cur+1, count + 1, opCount)
                elif op[i] == 1:  # 뺄셈
                    dfs(val - A[count + 1], cur+1, count + 1, opCount)
                elif op[i] == 2:  # 곱셈
                    dfs(val * A[count + 1], cur+1, count + 1, opCount)
                else:  # 나눗셈
                    if val < 0 and A[i + 1] > 0:
                        dfs(val * (-1) // A[count + 1] * (-1), cur+1, count + 1, opCount)
                    else:
                        dfs(val // A[count + 1], cur+1, count + 1, opCount)
                isVisited[i] = False

if __name__ == '__main__':
    N = int(input()) # 2 <= n <= 11
    A = list(map(int, input().split())) # 1 <= A <= 100
    opCount = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈의 개수
    op = []
    for i in range(4):
        op += [i for _ in range(opCount[i])]
    maxAnswer, minAnswer = -100000000, 100000000
    isVisited = [False for _ in range(N-1)]
    dfs(A[0], 0, 0, opCount)
    print(maxAnswer)
    print(minAnswer)




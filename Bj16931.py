# https://www.acmicpc.net/problem/16931
# 29380 KB, 68 ms

if __name__ == '__main__':
    import sys
    n, m = map(int, sys.stdin.readline().split())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, sys.stdin.readline().split())))

    answer = n * m * 2
    # for i in range(n):
    #     answer += paper[i][0] + paper[i][m-1]
    #     for j in range(1, m):
    #         answer += abs(paper[i][j]-paper[i][j-1])
    # for j in range(m):
    #     answer += paper[0][j] + paper[n-1][j]
    #     for i in range(1, n):
    #         answer += abs(paper[i][j]-paper[i-1][j])
    # print(answer)
    for row in paper + [*zip(*paper)]:
        answer += row[0] + row[-1]
        for i in range(len(row)-1):
            answer += abs(row[i] - row[i+1])
    print(answer)
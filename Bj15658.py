# https://www.acmicpc.net/problem/15658

def solution(add, sub, mul, div, sum, result):
    global max_answer, min_answer
    if sum == n - 1:
        if result < min_answer:
            min_answer = result
        if result > max_answer:
            max_answer = result
        return
    else:
        if add < ops[0]:
            solution(add + 1, sub, mul, div, sum + 1, result + a[sum + 1])
        if sub < ops[1]:
            solution(add, sub + 1, mul, div, sum + 1, result - a[sum + 1])
        if mul < ops[2]:
            solution(add, sub, mul + 1, div, sum + 1, result * a[sum + 1])
        if div < ops[3]:
            if result < 0:
                result = ((-1) * result // a[sum + 1]) * (-1)
            else:
                result //= a[sum + 1]
            solution(add, sub, mul, div + 1, sum + 1, result)

if __name__ == '__main__':
    max_answer, min_answer = -1000000000, 1000000000
    n = int(input())  # 2 <= n <= 11
    a = list(map(int, input().split())) # 1 < A <= 100
    ops = list(map(int, input().split()))  # +, -, *, /
    solution(0, 0, 0, 0, 0, a[0])
    print(max_answer)
    print(min_answer)

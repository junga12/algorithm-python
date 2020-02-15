# 1339 단어 수학 https://www.acmicpc.net/problem/1339
# 29284 KB, 56 ms

if __name__ == '__main__':
    n = int(input()) # 1 <= n <= 10
    values = {}
    for _ in range(n):
        word = input()
        value = pow(10, len(word)-1)
        for w in word:
            if not values.get(w):
                values[w] = value
            else:
                values[w] = values[w] + value
            value /= 10

    valuesList = list(values.items())
    valuesList.sort(reverse=True, key=lambda x:x[1])

    answer = 0
    num = 9
    for _, v in valuesList:
        answer += v * num
        num -= 1
    print(int(answer))

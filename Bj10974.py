# 10974 모든 순열 https://www.acmicpc.net/problem/10974
# 29924 KB, 288 ms

# nList의 a번째 위치와 b번째 위치를 변경
def swap(a, b):
    l = nList.copy()
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l

if __name__ == '__main__':
    n = int(input())
    nList = list(range(1, n+1))

    isKeep = True
    while(isKeep):
        for i in nList:
            print(i, end=' ')
        print()

        right = n - 1
        left = right - 1
        while (nList[left] > nList[left + 1]):
            left -= 1
        if left == -1:
            isKeep = False
        else:  # 교환
            while (True):
                next = swap(left, right)
                if next > nList:
                    break
                right -= 1
            # 오른쪽 부분 정렬
            l = next[left + 1:]
            l.sort()
            next = next[:left + 1] + l
            nList = next
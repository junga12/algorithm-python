# 10972 다음 순열 https://www.acmicpc.net/problem/10972
# 29776 KB, 64 ms

'''
N=4 일 때,
1 2 3 4
1 2 / 4 3
1 3 2 4
1 3 / 4 2
1 4 2 3
1 / 4 3 2
2 1 3 4
2 1 / 4 3
2 3 1 4
2 3 / 4 1
2 4 1 3
2 / 4 3 1
3 1 2 4
3 1 / 4 2
3 2 1 4
3 2 / 4 1
3 4 1 2
3 4 / 2 1
4 1 2 3
4 1 / 3 2
4 2 1 3
4 2 / 3 1
4 3 1 2
/ 4 3 2 1
'''

# nList의 a번째 위치와 b번째 위치를 변경
def swap(a, b):
    l = nList.copy()
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
    return l

if __name__ == '__main__':
    n = int(input())
    nList = list(map(int, input().split()))

    # 두 부분으로 나누기
    right = n-1
    left = right-1
    while(nList[left] > nList[left+1]):
        left -= 1

    if left == -1:
        print(-1)
    else:  # 교환
        while(True):
            next = swap(left, right)
            if next > nList:
                break
            right -= 1
        # 오른쪽 부분 정렬
        l = next[left+1:]
        l.sort()
        next = next[:left+1] + l
        for i in next:
            print(i, end=' ')
# 14890 경사로 https://www.acmicpc.net/problem/14890
# 29284 KB, 64 ms

def isSlop(height):
    slop = [False for _ in range(n)]
    for i in range(n-1):
        if abs(height[i] - height[i+1]) > 1: # 높이 차이가 1이면 경사로를 놓을 수 없다
            return False
        if height[i] - height[i+1] == 1: # 경사로가 오른쪽에 놓임
            cnt = l
            h = height[i+1]
            while (i+1<n and cnt>0):
                if h != height[i+1] or slop[i+1] is True:
                    return False
                cnt -= 1
                slop[i+1] = True
                i += 1
            if cnt != 0:
                return False
        elif height[i+1] - height[i] == 1: # 경사로가 왼쪽에 놓임
            cnt = l
            h = height[i]
            while (i>=0 and cnt>0):
                if (h != height[i]) or slop[i] is True:
                    return False
                cnt -= 1
                slop[i] = True
                i -= 1
            if cnt != 0:
                return False
    return True

if __name__ == '__main__':
    n, l = map(int, input().split()) # 2 <= n <= 100, 1 <= l <= n
    mymap = []
    for _ in range(n):
        mymap.append(list(map(int, input().split())))

    answer = 0
    for i in range(2):
        for mm in mymap:
            if isSlop(mm):
                answer += 1
        if i == 0:
            mymap = list(zip(*mymap))

    print(answer)
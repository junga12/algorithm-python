# https://www.acmicpc.net/problem/16988
# 29380 KB, 64 ms

import sys
input = sys.stdin.readline
n, m = map(int, input().split())  # 3 <= n, 3 <= 20
board = []  # 0=빈칸, 1=나, 2=상대
for _ in range(n):
    board.append(list(map(int, input().split())))
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]
is_visited, my_need, ai_count = [[False for _ in range(m)] for _ in range(n)], [], []

def check(i, j, ai_type):
    if not is_visited[i][j]:
        is_visited[i][j] = True
        if len(ai_count) == ai_type:
            ai_count.append(1)
        else:
            ai_count[ai_type] += 1
        for k in range(4):
            x, y = i + di[k], j + dj[k]
            if 0 <= x < n and 0 <= y < m:
                if board[x][y] == 2 and not is_visited[x][y]:
                    check(x, y, ai_type)
                elif board[x][y] == 0:
                    if len(my_need) == ai_type:
                        my_need.append({(x, y)})
                    else:
                        my_need[ai_type].add((x, y))


if __name__ == '__main__':
    ai_type, answer = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and not is_visited[i][j]:
                check(i, j, ai_type)
                ai_type += 1
    length = len(ai_count)
    one_list, one_dict = [], {}
    for i in range(length):
        if len(my_need[i]) == 2:
            count = ai_count[i]
            for j in range(i+1, length):
                if len(my_need[j]) < 3:
                    is_eat = True
                    for mn in my_need[j]:
                        if mn not in my_need[i]:
                            is_eat = False
                    if is_eat:
                        count += ai_count[j]
            if count > answer:
                answer = count
        elif len(my_need[i]) == 1:
            one_list.append(i)
    for ol in one_list:
        key = str(my_need[ol])
        if one_dict.get(key):
            one_dict[key] = one_dict[key] + ai_count[ol]
        else:
            one_dict[key] = ai_count[ol]
    dict_values = sorted(list(one_dict.values()), reverse=True)
    if len(dict_values) == 1:
        if answer < dict_values[0]:
            answer = dict_values[0]
    elif len(dict_values) >= 2:
        if answer < dict_values[0] + dict_values[1]:
            answer = dict_values[0] + dict_values[1]
    print(answer)
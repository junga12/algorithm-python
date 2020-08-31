# https://www.acmicpc.net/problem/16235
# 136600 KB, 356 ms (PyPy3)

class land:
    def __init__(self):
        self.nutrient = 5
        self.tree_age_list = []
        self.add_nutrient = 0
        self.breed_num = 0

    def set_add_nutrient(self, n):
        self.add_nutrient = n

    def add_tree(self, age):
        self.tree_age_list.append(age)

    def get_alive_tree_num(self):
        return len(self.tree_age_list)

    def year(self):
        if self.get_alive_tree_num() == 0:
            self.nutrient += self.add_nutrient  # 양분추가
            return 0
        count = 0
        for ta in reversed(self.tree_age_list):  # 자신의 나이만큼 양분을 먹는다
            if self.nutrient >= ta:
                self.nutrient -= ta
                count += 1
            else:
                break
        l = len(self.tree_age_list) - count
        for ta in self.tree_age_list[:l]:  # 죽은 나무가 양분으로 변한다
            self.nutrient += ta // 2
        self.tree_age_list = self.tree_age_list[l:]  # 양분을 못먹으면 죽는다
        breed_num = 0  # 번식해야하는 나무의 수
        for i in range(count):  # 나이 1 증가
            self.tree_age_list[i] += 1
            if self.tree_age_list[i] % 5 == 0:
                breed_num += 1
        self.nutrient += self.add_nutrient  # 양분추가
        return breed_num

    def set_breed_tree_num(self, num):
        self.breed_num += num

    def add_new_tree(self):
        self.tree_age_list += [1 for _ in range(self.breed_num)]
        self.breed_num = 0


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    lands = [[land() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _nut = list(map(int, input().split()))
        for j in range(n):
            lands[i][j].set_add_nutrient(_nut[j])
    for _ in range(m):
        x, y, z = map(int, input().split())
        lands[x - 1][y - 1].add_tree(z)
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    for y in range(k):
        for i in range(n):
            for j in range(n):
                breed_num = lands[i][j].year()
                if breed_num != 0:
                    for d in range(8):
                        di = i + dr[d]
                        dj = j + dc[d]
                        if 0 <= di < n and 0 <= dj < n:
                            lands[di][dj].set_breed_tree_num(breed_num)
        for i in range(n):
            for j in range(n):
                if lands[i][j].breed_num != 0:
                    lands[i][j].add_new_tree()
    answer = 0
    for i in range(n):
        for j in range(n):
            answer += lands[i][j].get_alive_tree_num()
    print(answer)
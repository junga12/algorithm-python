# 양 https://www.acmicpc.net/problem/3184
import sys

xi, yi = [0, 0, 1, -1], [1, -1, 0, 0]  # 상하좌우


class Bj3184:

    def __init__(self, r, c, g):
        self.row = r
        self.col = c
        self.ground = g
        self.__visit = [[False] * c for _ in range(r)]
        self.setOutFence()
        self.__sheep = 0
        self.__wolf = 0

    def GetSheep(self):
        return self.__sheep

    def GetWolf(self):
        return self.__wolf

    # 울타리 밖 부분을 visit = True로 설정
    # 밖으로 나가는 것을 방지
    def setOutFence(self):
        for r in range(self.row):
            self._setNearVisit(r, 0)
            self._setNearVisit(r, self.col - 1)
        for c in range(self.col - 1):
            self._setNearVisit(0, c)
            self._setNearVisit(self.row - 1, c)

    def _setNearVisit(self, r, c):
        if self.isVisit(r, c) or self.ground[r][c] != '.':
            return

        self.__visit[r][c] = True
        q = [[r, c]]
        while len(q) != 0:
            x, y = q.pop()
            for i in range(4):
                _x = x + xi[i]
                _y = y + yi[i]
                if self.existRange(_x, _y) and not self.isVisit(_x, _y) and self.__visit[_x][_y] == '.':
                    self.__visit[_x][_y] = True
                    q.append([_x, _y])

    def existRange(self, r, c):
        return 0 <= r < self.row and 0 <= c < self.col

    def isVisit(self, r, c):
        return self.__visit[r][c]

    def NextDay(self):
        for r in range(1, self.row - 1):
            for c in range(1, self.col - 1):
                if not self.isVisit(r, c) and self.ground[r][c] != '#':
                    sheep, wolf = 0, 0

                    self.__visit[r][c] = True
                    q = [[r, c]]
                    while len(q) != 0:
                        x, y = q.pop()
                        if self.ground[x][y] == 'o':
                            sheep += 1
                        elif self.ground[x][y] == 'v':
                            wolf += 1

                        for i in range(4):
                            _x = x + xi[i]
                            _y = y + yi[i]
                            if not self.isVisit(_x, _y) and self.ground[_x][_y] != '#':
                                self.__visit[_x][_y] = True
                                q.append([_x, _y])

                    if sheep > wolf:
                        self.__sheep += sheep
                    else:
                        self.__wolf += wolf


def solution2(r, c, ground):
    g = Bj3184(r, c, ground)
    g.NextDay()
    return g.GetSheep(), g.GetWolf()


####################################

def solution1(row, col, ground):
    resultSheep = 0
    resultWolf = 0

    visit = [[False] * col for _ in range(row)]

    # 울타리 밖 부분을 visit = True로 하여 방문하지 않게 한다.
    for r in range(row):
        visitNear(r, 0, row, col, visit, ground)
        visitNear(r, col - 1, row, col, visit, ground)

    for c in range(1, col - 1):
        visitNear(0, c, row, col, visit, ground)
        visitNear(row - 1, c, row, col, visit, ground)

    for r in range(1, row - 1):
        for c in range(1, col - 1):
            if visit[r][c] is False and ground[r][c] != '#':
                sheep, wolf = 0, 0
                xi, yi = [0, 0, 1, -1], [1, -1, 0, 0]

                q = [[r, c]]

                while len(q) != 0:
                    x, y = q.pop()
                    if visit[x][y] is True:
                        continue
                    visit[x][y] = True
                    if ground[x][y] == 'o':
                        sheep += 1
                    elif ground[x][y] == 'v':
                        wolf += 1

                    for i in range(4):
                        _x = x + xi[i]
                        _y = y + yi[i]
                        if visit[_x][_y] is False and ground[_x][_y] != '#':
                            q.append([_x, _y])

                if sheep > wolf:
                    resultSheep += sheep
                else:
                    resultWolf += wolf

    return [resultSheep, resultWolf]


def visitNear(r, c, row, col, visit, ground):
    if visit[r][c] is True or ground[r][c] != '.':
        return

    xi, yi = [0, 0, 1, -1], [1, -1, 0, 0]
    q = [[r, c]]
    while len(q) != 0:
        x, y = q.pop()
        visit[x][y] = True
        for i in range(4):
            _x = x + xi[i]
            _y = y + yi[i]
            if 0 <= _x < row and 0 <= _y < col and visit[_x][_y] is False and ground[_x][_y] == '.':
                q.append([_x, _y])


if __name__ == '__main__':
    r, c = map(int, sys.stdin.readline().split())

    testCaseList = []
    for _ in range(r):
        testCaseList.append(sys.stdin.readline().strip())

    answer = solution2(r, c, testCaseList)
    print(' '.join(str(a) for a in answer))

# 3190 뱀 https://www.acmicpc.net/problem/3190
# 29284 KB, 76 ms

class Snack:
    def __init__(self):
        self.time = 0
        self.direction = 3 # 0: 상, 1: 좌, 2: 하, 3: 우
        self.row = 0 # 행 (머리)
        self.column = 0 # 열 (머리)
        self.location = [[0, 0]] # 뱀의 위치
    def turn(self, c):
        if c == 'L':
            self._turnLeft()
        else:
            self._turnRight()
    def _turnLeft(self):
        self.direction += 1
        if self.direction == 4:
            self.direction = 0
    def _turnRight(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3
    def go(self):
        if self.direction == 0: # 상
            self.row -=1
        elif self.direction == 1: # 좌
            self.column -= 1
        elif self.direction == 2: # 하
            self.row += 1
        else: # 우
            self.column += 1
        if self.column < 0 or self.row < 0 or self.column >= n or self.row >= n:
            return False
        if [self.row, self.column] in self.location:
            return False
        if not board[self.row][self.column]: # 사과가 없으면
            self.location.pop(0)
        else:
            board[self.row][self.column] = False
        self.location.append([self.row, self.column])
        return True
    def increaseTime(self):
        self.time += 1

if __name__ == '__main__':
    n = int(input()) # 2 <= n <= 100
    board = [[False] * n for _ in range(n)]
    k = int(input()) # 0 <= k <= 100
    for _ in range(k):
        r, c = map(int, input().split())
        board[r - 1][c - 1] = True 
    l = int(input()) # 1 <= l <= 100
    x, c = map(str, input().split())
    s = Snack()
    while (s.go()):
        s.increaseTime()
        if s.time == int(x):
            s.turn(c)
            l -= 1
            if l > 0:
                x, c = map(str, input().split())
    print(s.time + 1)
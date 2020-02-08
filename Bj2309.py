# 2309 일곱 난쟁이 https://www.acmicpc.net/problem/2309
# 29284 KB, 56ms

DWARF_NUM = 9

if __name__ == '__main__':
    heightList = []
    for i in range(DWARF_NUM):
        heightList.append(int(input()))

    heightList.sort()
    allSum = sum(heightList)

    first = 0
    second = 1
    while (allSum - heightList[first] - heightList[second] != 100):
        second += 1
        if second == DWARF_NUM:
            first += 1
            second = first + 1

    for i in range(DWARF_NUM):
        if i not in [first, second]:
            print(heightList[i])
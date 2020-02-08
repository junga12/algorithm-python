# # 2529 부등호 https://www.acmicpc.net/problem/2529
#
# def check(num):
#     if len(num) != k + 1:
#         num = '0' + num
#
#     if len(num) > len(set(num)):
#         return True
#
#     for i in range(k):
#         if inequalitys[i] == '<' and num[i] > num[i+1]:
#             return True
#         elif inequalitys[i] == '>' and num[i] < num[i+1]:
#             return True
#
#     return False
#
# def check1(num):
#     if len(num) != k + 1:
#         num = '0' + num
#
#     if len(num) > len(set(num)):
#         return True
#
#     for i in range(k):
#         if inequalitys[i] == '<' and int(num[i]) > int(num[i+1]):
#             return True
#         elif inequalitys[i] == '>' and int(num[i]) < int(num[i+1]):
#             return True
#
#     return False
#
# def check2(num):
#     if len(num) != k+1:
#         num = ['0'] + num
#     if len(num) != len(set(num)):
#         return True
#     for i in range(k):
#         if inequalitys[i] == '<' and num[i] > num[i+1]:
#             return True
#         elif inequalitys[i] == '>' and num[i] < num[i+1]:
#             return True
#     return False
#
# if __name__ == '__main__':
#     k = int(input()) # 2 <= k <= 9
#     inequalitys = list(map(str, input().split()))
#
#     minNum, maxNum = '', ''
#     for i in range(k+1):
#         minNum += str(i)
#         maxNum += str(9-i)
#     min = list(map(str, minNum))
#     max = list(map(str, maxNum))
#     while(check2(min)):
#         minNum = str(int(minNum) + 1)
#         min = list(map(str, minNum))
#     while(check2(max)):
#         maxNum = str(int(maxNum) -1)
#         max = list(map(str, maxNum))
#
#     # max = int(max)
#     # min = int(min)
#     # while(check1(max)):
#     #     max -= 1
#     # while(check1(min)):
#     #     min += 1
#
#     # while(check(max)):
#     #     max = str(int(max) - 1)
#     # while(check(min)):
#     #     min = str(int(min) + 1)
#
#     if len(minNum) != k+1:
#         minNum = '0' + minNum
#     print(maxNum)
#     print(minNum)

global max, min

def check(op, a, b):
    if op == '<':
        return a < b
    else:
        return a > b

def findMin(cnt, nums):
    if cnt == k+1:
        if min :
            min = nums
        max = nums
        print(nums)
        return nums
    for i in range(10):
        if not isUsed[i]:
            if cnt == 0 or check(ops[cnt-1], nums[-1], str(i)):
                isUsed[i] = True
                findMin(cnt+1, nums + str(i))
                isUsed[i] = False

# def findMax(cnt, nums):
#     if cnt == k+1:
#         print(nums)
#         return nums
#     for i in range(9, -1, -1):
#         if not isUsed[i]:
#             if cnt == 0 or check(ops[cnt-1], nums[-1], str(i)):
#                 isUsed[i] = True
#                 findMin(cnt+1, nums + str(i))
#                 isUsed[i] = False

if __name__ == '__main__':
    k = int(input()) # 2 <= k <= 9
    ops = list(map(str, input().split()))
    isUsed = [False for _ in range(10)]
    max, min = "", ""
    print(findMin(0, ""))
    # isUsed = [False for _ in range(10)]
    # print(findMax(0, ""))
    print(min)
    print(max)


# T = int(input())
# for tc in range(1,T+1):
#     col,row = map(int,input().split())
#     arr = [input() for _ in range(row)]
#

# T = 10
#
# result = []
# for i in range(T):
#     length = int(input())
#     testcase = []
#     for _ in range(8):
#         testcase.append(input())
#
#     count = 0
#     for i in range(8):
#         for j in range(8 - length + 1): #검사 할 인덱스 주의
#             #가로 검사
#             string = testcase[i][j:j+length] #가로의 경우 슬라이싱
#             if string == string[::-1]: #문자열 역순
#                 count += 1
#             #세로 검사
#             string = ''
#             for k in range(length):
#                 string += testcase[j + k][i] #세로의 경우 row 인덱스와 col 인덱스 주의
#             if string == string[::-1]:
#                 count += 1
#
#     result.append(count)
#
# for i in range(T):
#     print("#{} {}".format((i+1), result[i]))


def HM(col,row):
    cnt = 0
    for m in range(row):
        for i in range(col // 2):
            while arr[m][i] == arr[m][col - 1 - i]:
                cnt += 1
            if cnt == col // 2:
                cm = m
                return arr[cm]
            else:
                return 0

def SM(col,row):
    cnt = 0
    for m in range(col):
        for i in range(row // 2):
            while arr[i][m] == arr[row-1-i][m]:
                cnt += 1
            if cnt == row // 2:
                ci = i
                lst = []
                for k in range(row):
                    lst.append([ci][k])
                    return lst


T = int(input())
for tc in range(1,T+1):
    col,row = map(int,input().split())
    arr = [input() for _ in range(row)]
    if HM(col,row) != 0:
        print(HM(col,row))
    else:
        print(SM(col, row))
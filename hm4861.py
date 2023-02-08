# s= 'abcde'
# print(s[::-1])

# 배열을 만든다
# 행 탐색 리스트에 담음 뒤집은거랑 비교해서 같은지 확인
# 열 탐색


# T = int(input())
# for tc in range(1,T+1):
#     col,row = map(int,input().split())
#     arr = [input() for _ in range(row)]
#     lst = []
#     for m in range(row):
#         for i in range(col):
#             cnt = 0
#             while cnt < col//2:
#                 if arr[m][i] == arr[m][col-1-i]:
#                 print(arr[m][i])

T = int(input())
for tc in range(1,T+1):
    col,row = map(int,input().split())
    arr = [input() for _ in range(row)]
    lst = []
    for m in range(row):
        for i in range(col):
            while col <
            lst.append(arr[m][i])
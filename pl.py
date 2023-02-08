# T = int(input())
# for tc in range(1,T+1):
#     col,row = map(int,input().split())
#     arr = [input() for _ in range(row)]
#     lst = []
#     for m in range(row):
#         for i in range(col):
#             while col <
#             lst.append(arr[m][i])



# def ispelindrome(col):
#     lens = 0
#     for _ in col:
#         lens +=1
#     for idx in range(lens//2):
#         if s[idx] != s[lens-1-idx]:
#             return 0
#     return 1


# arr = [[1,2,3],[4,5,6],[7,8,9]]
# t= zip(*arr)
# for s in t:
#     print(s)




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

def check():
    for row in range(N):
        for st in range(N-M+1):
            temp = ''
            for col in range(N):
                temp = temp + arr[row][st+col]
            if ispa(temp):
                # res = temp
                return temp

            for col in range(N):
                temp = ''
                for row in range(N):
                    temp += arr[row][col]

                if ispa(temp):
                    return temp

# D3 1221 GNS
T = int(input())
for t in range(1, T + 1):
    N = input()
    # 각 개수를 저장하는 딕셔너리
    str_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    str_list = input().split()
    result = ''
    for s in str_list:
        # 각각 카운팅한다.
        str_dict[s] += 1
    # 각 원소가 몇개인지 나오기때문에 앞에서부터 개수만큼 생성한다.
    for key, value in str_dict.items():
        temp = ' '.join([key] * value)
        result += temp + ' '

    print("#{}".format(t))
    print(result[:len(result) - 1])

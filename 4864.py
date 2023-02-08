# T = int(input())
# for tc in range(T):
#     str1 = input()
#     str2 = input()
#     m = 0
#     i = 0
#     for i in range(len(str2)):
#             if str2[i] == str1[m]:
#                 while m < len(str2):
#                     m += 1



def BruteForce(search,arr):
    i = 0
    j = 0 
    while j < len(search) and i< len(arr) :
        if arr[i] != search[j]:
            i = i -j
            j = -1
        i = i+1
        j=  j+1
    if j == len(search) :
        return 1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    search = input()
    arr = input()
    sol = BruteForce(search,arr)
    print(f'#{tc} {sol}')



#? 브루트포스
#고지식한 패턴검색으로 본문의 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

arr = input()
search = input()
n = len(arr)
m = len(search)

def BruteForce(search,arr):
    i = 0
    j = 0 
    while j < m and i<n :
        if arr[i] != search[j]:
            i = i -j
            j = -1
        i = i+1
        j=  j+1
    if j == m :
        return i-m
    else:
        return -1
print(BruteForce(search,arr))
    
# def get_pi(P):
#     m= len(P)
#     pi = [0 for i in range(m)]
#     idx = 0
#     for i in range(1,m):
#         while idx>0 and pi[i] != P[idx]:
#             idx = pi[idx -1]
#         if P[i] == P[idx]:
#             idx += 1
#             pi[i] = idx
#     print(pi)

# get_pi('ababcacb')

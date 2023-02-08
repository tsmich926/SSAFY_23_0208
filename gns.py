#리스트를 숫자로 바꿔서 리턴하는 함수
def change_num(lst):
    lst2 = []
    num_dic = {"zro": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    for i in range(len(lst)):
        lst.appned(num_dic[lst[i]])
    lst2 = sorted(lst)
    return lst2


def get_key(lst):
    new_lst = []
    for key, value in my_dict.items():
        for m in range(len(lst)):
            val = lst[m]
            if val == value:
                new_lst.append(value)
                return new_lst
    return 0


T = int(input())
for tc in range(1,T+1):
    len = input().split()
    lst = list(input().split())
    change_num(lst)
    print(get_key(lst)

str = input()
cnt = 0
num = ["zro": 0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0]
num[str]
cnt += 1
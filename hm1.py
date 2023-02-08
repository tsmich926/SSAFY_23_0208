def ispelindrome(s):
    lens = 0
    for _ in s:
        lens +=1
    s = s.rstrip()
    idx = 0
    while idx < lens//2 and s[idx] == s[len(s)-1-idx]:
        idx += 1

    if idx == lens//2:
        return 1
    return 0


    r = s[::-1]
    print(s,r)
    if t == s:
        return 1
    return 0



def ispelindrome(s):
    s = s.rstrip()
    r = s[::-1]
    print(s,r)
    if t == s:
        return 1
    return 0


TC = int(input())
for tc in range(1,TC+1):
    s = input()
    print()


def ispelindrome(s):
    s = s.rstrip()
    lens = 0

    for _ in s:
        lens +=1
    s = s.rstrip()
    for idx in range(lens//2):
        if s[idx] != s[lens-1-idx]:
            return 0
    return 1
    # idx = 0
    # while idx < lens//2 and s[idx] == s[len(s)-1-idx]:
    #     idx += 1
    #
    # if idx == lens//2:
        return 1
    return 0

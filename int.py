#int함수 만들기
#ord() 문자의 아스키 값을 돌려준다
#chr() 아스키값에 해당하는 문자를 돌려준다

i = 0
num
for num in '123':
    i = i*10 + ord(num) - ord('0') #int(num)
print(i,type(i))

#int(123) 을 문자열로 바꾸기
def itoa(num):
    if num<0:
        isminus == True
        num *= (-1)
    s = ''
    while num>0 :
        asc = (num%10) + ord('0')
        num = num // 10
        s= chr(asc) + s
    if isminus:
        s= '-'+s
    print(s, type(s))
    return s
    # s = '3' 123%10를 하면 3이 나온다. 3은 0으로부터 3번째
    #0에 해당하는 문자에서 3칸 이동
    # asc = (num%10) + ord('0')
    # s= chr(asc)
    # s = '2'+s
    # s = '1'+s
    print(type(s))
    return s
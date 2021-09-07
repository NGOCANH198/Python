import math
def check2(s):
    for i in range(0,len(s)-2):
        if abs(int(s[i]) - int(s[i+1])) != 2: return 0
    return 1
test = int(input())
while(test != 0):
    test -=1
    s = input()
    sum =0
    for i in range(0,len(s)):
        sum += int(s[i])
    if sum%10 == 0 and check2(s)==1 : print("YES")
    else: print("NO")





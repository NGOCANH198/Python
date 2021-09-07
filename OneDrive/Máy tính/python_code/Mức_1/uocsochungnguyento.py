import math
def check(n):
    if(n<2): return 0
    for i in range(2,int(n**0.5+1)):
        if n%i == 0: return 0
    return 1
test = int(input())
while(test != 0):
    test -=1
    a,b = map(int,input().split())
    n = math.gcd(a,b)
    s= str(n)
    sum =0
    for i in s:
        sum += int(i)
    if(check(sum) == 1): print("YES")
    else: print("NO")




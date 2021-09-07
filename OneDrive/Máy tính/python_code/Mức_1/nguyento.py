import math

def check(n):
    if n<2: return 0
    for i in range(2,int(n ** 0.5 +1)):
        if n%i == 0 : return 0
    return 1
t = int(input())
while(t>0):
    t-=1
    n = int(input())
    count = 1
    for i in range(2,n):
        if math.gcd(i,n) == 1 : count += 1
    if check(count) == 1 : print("YES")
    else : print("NO")


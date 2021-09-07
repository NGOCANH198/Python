import math
def check(n):
    if n<2 : return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 : return 0
    return 1

x,n = map(int,input().split())
a=[]
for i in range(2,100000):
    if check(i) == 1:
        a.append(i)
b=[n]
k = n
for i in range(0,x):
    k +=a[i]
    b.append(k)
for i in b:
    print(i," ",end='')
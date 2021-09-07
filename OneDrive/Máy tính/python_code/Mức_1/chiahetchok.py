import math
a,k,n = map(int,input().split())
ok=0
n = int(n/k)+1
for i in range(n):
    x = i*k-a
    if x>0:
        ok +=1
        print(x," ",end='')
if ok == 0 : print("-1")
import math
a,b = map( int,input().split())
for i in range(10**(b-1),10**(b)-1):
    if math.gcd(a,i)==1: print(i," ",end='')

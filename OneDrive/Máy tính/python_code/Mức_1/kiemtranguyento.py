import math
def check(n):
    if n<2 : return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0 : return 0
    return 1

a=[]
n,m = map(int ,input().split())
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        print(check(a[i][j]), " ",end='')
    print("\n")
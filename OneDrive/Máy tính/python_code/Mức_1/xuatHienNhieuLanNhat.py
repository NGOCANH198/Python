def solve():
    ok = 0
    f = {}
    n = int(input())
    a = [int(i) for i in input().split()] 
    for i in a:
        if i in f:  f[i]+=1

        else: f[i] = 1

    for i in f:
        if (f[i] >= int(n/2)+1):
            print(i) ; ok = 1;break
    if ok == 0 : print("NO")

for i in range(int(input())): solve()        


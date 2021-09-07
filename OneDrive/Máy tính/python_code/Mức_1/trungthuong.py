def solve():
    f={}
    ans = 99999
    max = 1
    n = int(input())
    for i in range(n):
        x = int(input())
        if x in f: f[x]+=1
        else: f[x] = 1
    for i in f: 
        if f[i] > max: max = f[i]
    for i in f:
        if f[i] == max : ans = min(ans,i)
    print(ans)

for i in range(int(input())):
    solve()
    

def solve():
    s = input()
    n = len(s)
    count = 1
    for i in range(0,n-1,1):
        if s[i] == s[i+1] : count+=1
        else:
            print(count,s[i], sep='',end='')
            count=1
    print(count,s[n-1],sep='',end='')
    print()
for i in range(int(input())): solve()        


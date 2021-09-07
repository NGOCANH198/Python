def sumCS(n):
    s = str(n)
    sum = 0
    for i in s: sum += int(i)
    return sum
def tichCS(n):
    s=str(n)
    ans = 1
    for i in s: ans *= int(i)
    return ans
def solve():
    n = int(input())
    a=[int(i) for i in input().split()]
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(tichCS(a[j])<tichCS(a[i])) or (tichCS(a[i]) == tichCS(a[j]) and a[j]<a[i]):
                a[i],a[j] = a[j],a[i]
    for i in a: print(i," ",end='')
    print()
for i in range(int(input())) : solve()

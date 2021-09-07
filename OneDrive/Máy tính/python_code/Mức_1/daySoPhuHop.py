def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort() ; b.sort()
    ok = 0
    for i in range(n):
        if a[i]>b[i]: print("NO") ;ok = 1 ; break
    if ok == 0: print("YES")
for i in range(int(input())): solve()
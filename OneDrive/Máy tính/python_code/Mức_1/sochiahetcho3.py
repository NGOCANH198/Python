def sumCS(n):
    s = str(n)
    sum = 0
    for i in s: sum += int(i)
    return sum
for i in range(int(input())):
    n = int(input())
    if(sumCS(n) %3 == 0): print("YES")
    else: print("NO")
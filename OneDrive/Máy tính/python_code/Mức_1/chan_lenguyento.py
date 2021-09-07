def isprime(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
def solve(s):
    for i in range(len(s)):
        #vi tri le
        if i%2 == 0 and int(s[i])%2 !=0: return 0
        elif i%2 !=0 and int(s[i])%2 == 0: return 0
    return 1
def checkNT(s):
    sum = 0
    for i in s:
        sum += int(i)
    if isprime(sum) == 1: return 1
    return 0
for i in range(int(input())):
    n = input()

    if checkNT(n) == 1 and solve(n)== 1: print("YES")
    else: print("NO")
    
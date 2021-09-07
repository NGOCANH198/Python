def isprime(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
for i in range(int(input())):
    s = input()
    n =''
    n = s[-4]+s[-3]+s[-2]+s[-1]
    if isprime(int(n)) == 1: print("YES")
    else: print("NO")
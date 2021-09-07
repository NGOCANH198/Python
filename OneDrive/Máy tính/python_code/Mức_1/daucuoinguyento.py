def isprime(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
for i in range(int(input())):
    s = input()
    n1=''
    n2 =''
    n1= s[-3]+s[-2]+s[-1]
    n2 = s[0]+s[1]+s[2]
    if isprime(int(n1)) == 1 and isprime(int(n2)) == 1: print("YES")
    else: print("NO")
def isprime(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
for i in range(int(input())):
    s = input()
    count=0
    for i in s:
        if isprime(int(i)):
            count+=1
    if isprime(len(s)) and count>len(s)-count:
        print("YES")
    else:
        print("NO")


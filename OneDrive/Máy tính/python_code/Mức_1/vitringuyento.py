def isprime(n):
    if n<2: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
def solve(s):
    for i in range(len(s)):
        if (isprime(i) == 1 and isprime(int(s[i])) !=1) or (isprime(i) !=1 and isprime(int(s[i])) == 1):
            return 0
    return 1
for i in range( int(input())):
    s = input()
    if(solve(s)==1): print("YES")
    else: print("NO")

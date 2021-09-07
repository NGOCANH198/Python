def check(n):
    if n<2:return 0
    for i in range( 2,int(n**0.5)+1):
        if n%i == 0: return 0
    return 1
def checkTN(n):
    s= str(n)
    s1=s[::-1]
    if s1 == s: return 1
    return 0


for i in range( int(input())):
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    
    if check(sum) == 1 : print("YES")
    else: print("NO")
    
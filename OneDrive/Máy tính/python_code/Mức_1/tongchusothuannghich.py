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
    if sum>10:
        if checkTN(sum) == 1 and len(s)>2: print("YES")
        else: print("NO")
    else: print("NO")
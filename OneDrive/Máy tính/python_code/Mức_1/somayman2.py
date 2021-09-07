test = int(input())
while(test != 0):
    test -=1
    s = input()
    res = 0
    for i in s:
        if i == '4' or i =='7' : res+=1
    if res ==  len(s):
         print("YES")
    else: print("NO")



test = int(input())
while(test != 0):
    num = input()
    ok = 0
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]): 
            ok = 1
            break
    if ok == 1: print("NO")
    else: print("YES")
    test = test -1

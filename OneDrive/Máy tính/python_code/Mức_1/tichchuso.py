t = int(input())
while(t > 0):
    n = input()
    sum = 1
    for i in n:
        if int(i)!=0:
            sum *= int(i)
    print(sum)    
    t-=1    

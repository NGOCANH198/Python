t = int(input())
while(t>0):
    f=[0,1]
    a,b = map(int,input().split())
    for i in range(2,93):
        x = f[i-1] + f[i-2]
        f.append(x)
    for i in range(a,b+1,1):
        print(f[i]," ",end='')
    print("\n") 
    t-=1
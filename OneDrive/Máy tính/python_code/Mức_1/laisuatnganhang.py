t = int(input())
while(t!=0):
    n = input().split()
    dem = 0 
    a=float(n[0])  
    # lãi suất
    x=float(n[1])
    # số tiền ban đầu
    m=float(n[2])
    # số tiền đạt được
    dem=0
    while(a<m):
        x1=1+float(x/100)
        a=a*x1
        dem+=1
    print(dem)   
    t-=1
def Try(a,ans):
    if(a[0] ==a[1]==a[2] ==a[3]): return ans
    else:
        x = a[0];y =a[1]
        z = a[2];t=a[3]
        a[0] = abs(x-y)
        a[1] = abs(y-z)
        a[2] = abs(z-t)
        a[3] = abs(t-x)
        return Try(a,ans+1)
while 1:
    a=[int(i) for i in input().split()]
    if( a[0] == 0 and a[1] == 0 and a[2] == 0 and a[3] == 0) :break
    else: print(Try(a,0))
while 1:
    count = 1
    n = int(input())
    if n == 0: break
    else:
        while(n>1):
            if(n%2==0): n = n/2;count+=1
            else: n = n*3+1 ;count +=1
    print(count)
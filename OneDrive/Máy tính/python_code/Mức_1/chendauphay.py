s = input()
i = len(s)-1
ans =''
count = 0
while 1:
    count +=1
    ans=s[i]+ans
    if i==0: break
    if count == 3: 
        ans = ','+ans
        count = 0
    i-=1
print(ans)

test = int(input())
for n in range(0,test):
    str = input()
    s=''
    for i in range(0,len(str),2):
        s += str[i]*int(str[i+1])
    print(s)

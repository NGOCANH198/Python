def sumChan(s):
    s1 = str(s)
    sum = 0
    for i in range(len(s1)):
        if i%2!=0:sum += int(s1[i])
    return sum
def tichLe(s):
    s1= str(s)
    tich = 1
    for i in range(len(s1)):
        if i%2==0 and int(s1[i]) != 0: tich *= int(s1[i])
    return tich

for i in range( int(input())):
    s=input()
    print(tichLe(s),"",sumChan(s),end='')
    print()
def isThuanNghich(n):
    str1 = str(n)     # ep kieu so n thanh chuoi
    str2 = str1[::-1]  # dao nguoc chuoi str1
    if (str1 == str2):
        return True
    else:
        return False
def isChuSo(n):
    str1 = str(n) 
    if len(str1)%2==0:
        return True
    else:
        return False

def isFull_ChuSo(n):
    str1 = str(n)
    kt=1
    for i in range(len(str1)):
        if int(str1[i]) %2 !=0:
            kt=0
            break
    if kt==1:
        return True
    else:
        return False
t = int(input())
while(t!=0):
    sb=""
    num=int(input())
    for index in range(10, num):
        if isThuanNghich(index) == 1 and isChuSo(index) == 1 and isFull_ChuSo(index)==1:
            sb=sb+str(index)+" "
    print(sb)       
    t-=1
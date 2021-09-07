test = int(input())
while test != 0:
    test -=1
    s = input()
    l = len(s)
    check = 0
    if (ord(s[0]) == ord(s[l-2])) and (ord(s[1]) == ord(s[l-1])):
        check = 1
    if check == 0 :print("NO")
    else : print("YES")

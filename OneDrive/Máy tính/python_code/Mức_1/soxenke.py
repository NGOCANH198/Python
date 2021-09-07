def solve(s):
    if len(s) %2 == 0: return 0
    elif int(s[0]) == int(s[1]):return 0
    for i in range(2,len(s),2):
        if int(s[i]) != int(s[i-2]): return 0
    return 1
for i in range(int(input())):
    s = input()
    if solve(s) == 1: print("YES")
    else: print("NO")

import math
for _ in range(int(input())):
    s = input()
    n = int(s)
    i = len(s)
    if n > 10**(i-1):print( round(n,-(i-1)))
       
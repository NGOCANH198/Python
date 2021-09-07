str = input()
a,b = 0,0
for i in range(len(str)):
    if str[i].islower(): a+=1
    else: b+=1

if a>=b: print(str.lower())
else: print(str.upper())
# name = input()
# full = 'Hello '+name+'!'
# print(full)
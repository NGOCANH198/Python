n = int(input())
day = input()
arr = day.split()
dem = 0
for i in range(n-1):
    for j in range(i+1,n):
        if int(arr[j]) < int(arr[i]):
            dem+=1

print(dem)

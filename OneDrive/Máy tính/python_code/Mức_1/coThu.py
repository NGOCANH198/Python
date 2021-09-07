# # bai 1 : viết tất cả các phép cộng trừ nhân chia mà mỗi phép tính đều thỏa mãn cho kết quả là 8
# print(4*2)
# print(4+4)
# print(16/4)
# print(89%9)
# # bai2 : sử dụng 1 biến đại diện cho 1 con số yêu thích, sau đó, sử dụng biến, tại 1 tin nhắn và in ra tin nhăn đó , tiết lộ con số yêu thích:
# a = (int)input()
# print('số yêu thích là:' , a)

# # bai 3:có 2 số phức, tính tổng và hiệu của chúng
# a = 1+5J
# b = 5-6j
# print(a+b,a-b)
# str1 = input()
# str2 = input()
# mid = len(s)/2
# print(str1[:mid] + str2 +str1[k:])
# import math
# str = input()
# countT , countH,countN,count = 0,0,0,0
# for i in len(str):
#     if str[i].islower(): countT += 1
#     if str[i].isupper(): countH +=1
#     if str[i].isnumeric(): countN +=1
#     else: count+=1
# print(count,countT,countH,countN)

# List
# bai 1
# list1 = ['Anh',' Chung','Nguyen','Tran']
# list1.pop()
# print(list1)
# list1.insert(3,'TVC')
# print(list1)
# list1[0] = 'Python'
# print(list1)

# bai2: đảo giá trị
# list1[0], list1[-1] = list1[-1] , list1[0] 
# print(list1)
# bai 3: xoa phan tu chan
# list1 = [2,4,6,8]
# new_l =[]
# for i in list1:
#     if(i%2 == 0):
#         new_l.append(i)
# print(new_l)
# bai 4: tinh tong trung binh cua cac phan tu la so:
# a = [1,'a',2,4,5,'C']
# dem ,sum = 0,0
# for i in a:
#     if a(i).isnumeric():
#         dem+=1
#         sum += a[i]
# print(sum,sum/dem)   --dang bug--
# bai 5: chuyển thành bình phwuogn các mẳng
# a = [1,2,3,4,5]
# b = []
# for i in a:
#     b.append(i*i)
# b.sort(reverse = True)
# print(b)
#  bai6: dem các so xuat hien 1 lan trong mang
a2= [1,2,3,2,4,'a','b']
x = len(set(a2))
print(x)

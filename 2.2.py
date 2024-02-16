# a=[]
# count=0
# for i in range(77,136):
#     if i%6==0:
#         a.append(i)
#         count+=1
# print(a)
# print(count)
#
#
# a=[]
# count=0
# for i in range(96,1004):
#     if i%8==0:
#         a.append(i)
#         count+=1
# print(a)
# print(count)
#
#
#
# a=[]
# count=0
# for i in range(43,883):
#     if i%6==0:
#         if i%7==0:
#             a.append(i)
#             count+=1
# print(a)
# print(count)
#





lst=[]
for i in range(1000):
    lst.append(0)

for i in range(1,1001):
    if i%5==0:
        lst[i-1]+=1
    if i%7==0:
        lst[i-1]+=1
    if i%9==0:
        lst[i-1]+=1
    if i%12==0:
        lst[i-1]+=1



print("最多：{}".format(max(lst)))
print("最少：{}".format(min(lst)))
result=len(lst)-lst.count(3)
print("最后亮了：{}".format(result))

# # a=150-150/3-150/5+150/15*2
# # print(a)
#
# lst = []
# for i in range(150):
#     lst.append(1)
#
# for i in range(1, 151):
#     if i % 4 == 0:
#         lst[i - 1] = 0
#
#     if i % 5 == 0:
#         if lst[i - 1] == 0:
#             lst[i - 1] = 1
#         else:
#             lst[i - 1] = 0
# result = lst.count(1)
# print(result)
#
# for i in range(150):
#     if lst[i] == 1:
#         print(i + 1)


a = []
for i in range(150):
    a.append(0)

for i in range(1, 151):
    if i % 3 == 0:
        a[i - 1] += 1
    if i % 5 == 0:
        a[i - 1] += 1
    if i % 7 == 0:
        a[i - 1] += 1



for i in range(150):
    if a[i]==2 or a[i]==3:
        print(i+1)

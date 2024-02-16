# for a in range(1,1001):
#     for b in range(1,1001):
#         for c in range(1,1001):
#             for d in range(1001):
#                 if a ==21*b and a+c==19*(b+c)and a+c+d==17*(b+c+d):
#                     print(a,b,c,d)



lst1=[]
for a in range(1,1001):
    for b in range(1,1001):
        if a==21*b:
            lst1.append([a,b])
print(lst1)

lst2=[]
for i in lst1:
    a=i[0]
    b=i[1]
    for c in range(1,1001):
        if a+c==19*(b+c):
            lst2.append([a,b,c])
print(lst2)


lst3=[]
for i in lst2:
    a=i[0]
    b=i[1]
    c=i[2]
    for d in range(1,1001):
        if a+c+d==17*(b+c+d):
            lst3.append([a,b,c,d])
print(lst3)



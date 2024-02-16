
a = 1
b = []

while True:
    if (a % 3 == 0) and (a % 5 == 0):
        b.append(a)
    a += 1

    if a == 100:
        break
print(b)



#4
aa=[23,33,56,-78,97,2,-10,101,-20,120,133,189,231]
bb=[]
i=0
while True:
    if (aa[i]%2==1) and (aa[i]>0):
        bb.append(aa[i])
    i+=1
    if i==len(aa):
        break
print(sum(bb))



l=[]
for a in range(1,19):
    for b in range(1,19):
        for c in range(1,19):
            if a ==5*b and a+c==4*(b+c):
                l.append([a,b])
print(l)
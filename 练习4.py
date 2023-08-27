import random
while True:
    a={}
    for i in range(100):
        x = random.randint(1,9)
        if x in a:
            a[x]+=1
        else:
            a[x]=1
    print(a)

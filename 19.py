user=input("请输入一串数字")
zd={}
for i in user:
    if i in zd:
        zd[i]+=1
    else:
        zd[i]=1
    print(zd)






xie={"红细胞":"500万个","白细胞":"1万个","血小板":"30万个"}
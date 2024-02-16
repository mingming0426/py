s = ["strip", "join", "split", "replace"]
lst = [i.upper() for i in s]

print(lst)

f=open("info.txt","r")
lines=f.readlines()
low=[]
height=[]
for i in lines:
    low.append(i.split(";")[2])
    height.append(i.split(";")[3])
low=[int(i)for i in low]
height=[int(j.strip())for  j in height]
print(str(min((low))))
print(str(max((height))))



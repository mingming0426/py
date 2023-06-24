b = 0
a = ["a", "b", "c", "d"]
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

while True:
    if b >= len(a):
        break
    print(a[b])
    b += 1

lis = ["a","b","d","c","e","f","a","e","r","a","t","w","a","c","r","a","y","t","a"]
nl=lis[len(lis)-15:len(lis)]
nnl="".join(nl)
nnl.replace("a","w")
nnnl=lis[0:len(lis)-16]
nml="".join(nnnl)
m=nml+nnl
c=list(m)
print(c)


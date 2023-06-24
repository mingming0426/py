a="you and me"
b=a.split(" ")
for i in range(len(b)):
    c=b[i].capitalize()
    print(c,end="")

print()
d="abedtfs123"
e=""
for i in d:
    if i.isnumeric():
        continue
    else:
        e+=i
f=e.upper()
print(f)


g="wbre123!rtewq56"
v=g.split("!")
t=""
for i in v[1]:
    if i.isnumeric():
        continue
    else:
        t+=i
    n=t.upper()
print(n)

a = "23455"
b = list(a)
print(b)

#2
ab = ["s","g","t","r","n","m"]
ab.pop(3)
string = "".join(ab)
print(string)



a = ["print","break", "in", "continue", "input","while"]
b = []
i = 0
while True:
      if a[i] == "in":
           continue
      i +=1
      if i >= 5:
           break
      b.append(a[i])
print(b)
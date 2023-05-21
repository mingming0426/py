wordsOld=["print","input", "while", "break", "continue"]
wordsNew=[]
wordsNew.append(wordsOld[4])
wordsNew.append(wordsOld[3])
wordsNew.append(wordsOld[2])
wordsNew.append(wordsOld[1])
wordsNew.append(wordsOld[0])
print(wordsNew)

#第三题
flowers = ["月季","玫瑰","百合","杨树","兰花","牡丹","菊花","柳树", "荷花"]
a=[]
b=[]
a.append(flowers[0])
a.append(flowers[1])
a.append(flowers[2])
a.append(flowers[4])
a.append(flowers[5])
a.append(flowers[6])
a.append(flowers[8])
b.append(flowers[3])
b.append(flowers[7])
print(a)
print(b)

#第四题

c=[79,80,90,92,78,85,95,10,88,75,98,81]
d=[]
e=0
while True:
    e+=1
    if c[e]>=85:
        d.append(c[e])
    if e==11:
        break
print(d)


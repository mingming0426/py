a = range(5, 1000)
for i in a:
    if i % 3 == 0:
        print(i)
        i += 1
    else:
        i += 1

# 2
lst = ["我", "是", "小明", "今年", "10", "岁"]
print("".join(lst))

# 3
aa = '煮豆燃豆萁，豆在釜中泣。本是同根生，相见何太急？'

# 将字符串转化为列表
aal = list(aa)
e = aal.index("见")
# 检查并更正错误字
for i in range(len(aal)):
    if aal[i] == "见":
        aal[i] = "煎"

print("".join(aal))

# 4$
n = []
g = "欢迎来到小码王"
v = list(g)
for i in range(len(v)):
    n.append(v[i])
    n.append(str(i+1))

m="".join(n)
print(m)

# r是只读模式，这是默认模式
# a是追加模式，如果该文件已经存在，新的内容会被写入在原有内容之后。如果文件不存在，创建新文件进行写入
# 1、从C名单中获取间谍信息
# 1.1打开文件
C = open("C.txt", "r", encoding="utf-8")
# 1.2读取文件中的数据
listC = C.readlines()
# 1.3关闭文件
C.close()
stripListC=[i.strip()for i in listC]
spyListC=[]
for i in range(0,len(stripListC),4):
    spyListC.append(stripListC[i:i+4])


addressListC=[]
for i in spyListC:
    if i[1]=="入侵国家:Python"and i[3]not in addressListC:
        addressListC.append(i[3])
print(addressListC)



address=open("address.txt","w")
address.write(str(addressListC))
address.close()



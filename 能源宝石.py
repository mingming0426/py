# 编号范围
totalNumber = int(input("编号范围:"))
# 开始编号
startNumber = int(input("开始编号:"))
# 序号
orderNumber = int(input("序号:"))
# 删除序号
outNumber = int(input("删除序号："))
# 索引
index = startNumber - 1
# 构造编号列表
numList = [i for i in range(1, totalNumber + 1)]
while True:
    # 如果列表中只有一个数据，筛选结束
    if len(numList) == 1:
        break
    # 如果序号等于删除序号则删除该位置的数据
    if orderNumber == outNumber:
        numList.pop(index)
        orderNumber = 1
    # 否则在进入下一次筛选之前将索引和序号加1
    else:
        orderNumber += 1
        index += 1



    if index>=len(numList):
        index=0
print("最后的结果是：{}".format(numList[0]))
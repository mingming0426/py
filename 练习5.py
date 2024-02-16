# def fun(name, heght, age=10):
#     print("姓名：", name)
#     print("身高：", heght)
#     print("年龄：", age)


# fun(heght=0.8, name="小码君", age=11)
# fun("小明", 1.8)


# def summation(n,c,m,e):
#     su=c+m+e
#     av=su/3
#     print(n+"的总成绩:"+str(su))
#     print(n+"的平均成绩:"+str(av))
#
#
# summation("小明",45,30,25)
#


# def res(x,y):
#     a = 0
#     for i in range(x,y):
#         a+=i
#     print(a)
# res(1,99999999)
#
#
#
#
# a=5
# def test():
#     global b
#     b=10
#     print(a,b)
# test()
# print(a)
# print(b)


# a = int(input("第一个数（底数）："))
# b = int(input("第二个数（指数）："))
#
#
# def fun(c, d=2):
#     print(c ** d)
#
#
# fun(a, b)

# def fun(x, y):
#     a = x * y
#     print(str(round(a))+"元")


# a = int(input("单价："))
# b = int(input("重量："))
# fun(a,b)
# vd={"辣椒":5,"西红柿":8,"南瓜":6,"黄瓜":2,"葱":0.5,"土豆":3}
#
# ine=input("蔬菜名：")
# def fun(x):
#     n=vd[x]
#     print(str(n)+"元")
# fun(ine)


run=["1分10秒","1分15秒","2分01秒","1分30秒","1分5秒",]
a=int(input("学号："))
def fun(n):
    print(run[n-1])
fun(a)




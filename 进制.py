number = input("请输入要转换的数字：")


def tenToOther(number, jz):
    num = int(number)
    jz = int(jz)
    result = []
    chars = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    while num != 0:
        yu = num % jz
        num = num // jz
        if yu > 9:
            yu = chars[yu]
        result.append(str(yu))
    result = result[::-1]
    res = "".join(result)
    print("十进制的{}，转换成{}的结果为{}。".format(number, jz, res))


def toTen(number):
    reverseNum = number[::-1]
    res = 0
    for i in range(len(reverseNum)):
        n = int(reverseNum[i])
        res += n * int(jz) ** i
    print("{}进制的{}，转换为十进制的结果为{}".format(jz, number, res))


chance=input("请输入功能编号：1.十进制转换为其他进制 2.其他进制转换为十进制")
if chance=="1":
    jz=input("请输入要转换的进制(2,4,8,16)")
    tenToOther(number,jz)
elif chance=="2":
    jz = input("请输入进制(2,4,8,16)")
    toTen(number)
else:
    print("输入的信息有误~")

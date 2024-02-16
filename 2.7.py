# while True:
#     num = int(input("请输入要转换的十进制数"))
#     c=num
#     myList = []
#     while num != 0:
#         a = num % 2
#         num = num // 2
#         myList.append(a)
#     myList = myList[::-1]
#     result = "".join([str(i) for i in myList])
#     print("{}转换后的二进制数为：{}".format(c, result))
number = input("请输入要转换的数字：")
jz=input("请输入要转换的进制:")


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


tenToOther(number, jz)
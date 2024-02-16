number = input("请输入要转换的数字：")
jz = input("请输入要转换的进制(2,4,8,16)")


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


tenToOther(number,jz)

a = [1, 2, 3]
b = {1: 2, 2: 3, 3: 4}
c = a.pop(a.index(2))
d = b[2]
print(c)
print(d)

# 第二题
qian = {1: "壹", 2: "贰", 3: "叁", 4: "肆", 5: "伍", 6: "陆", 7: "柒", 8: "捌", 9: "玖", "十": "拾", "百": "佰",
        "千": "仟"}
user = input("输入数字、单位：")
if user == "1" or user == "2" or user == "3" or user == "4" or user == "5" or user == "6" or user == "7" or user == "8" or user == "9":
    user=int(user)

print(qian[user])

#第三题
tq={"周一":"🌤晴","周二":"多云","周三":"下小雨","周四":"下暴雨🌧","周五":"晴","周六":"多云","周日":"下小雨"}
user=input("星期几？：")
print(tq[user])
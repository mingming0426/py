import random

b = list(range(6, 67, 2))
print(b)

a = ["学生卡", "红领巾", "校徽", "身份证", "饭卡", "钢笔", "10元钱", "参展证"]
b = []
for i in range(3):
    c = a.pop(random.randint(0, len(a) - 1))
    b.append(c)
print("携带了" + b[0] + "," + b[1] + "," + b[2])
if "身份证" in b and "参展证" in b:
    print("欢迎来看展览！")
else:
    print("未经允许的外来人员，禁止入内")

a = input("第一位将军（进攻/不进攻）：")
b = input("第二位将军（进攻/不进攻）：")
c = input("第三位将军（进攻/不进攻）：")
d = input("第四位将军（进攻/不进攻）：")
if a == b == c == d == "进攻":
    print("发动进攻！")
else:
    print("暂不进攻！")

n = 0
while n <= 10:
    n *= 2
    n += 2
print(n)


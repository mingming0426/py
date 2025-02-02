import time
import string


def is_Chinese(words):
    for ch in words:
        if ord(ch) < 13312 or ord(ch) > 40956:
            return False
    else:
        return True


f = open("诗词库.txt")
computerstore = f.readlines()
f.close()
computerstore = [i.strip("\n") for i in computerstore]
computerstoreDel = []
for k in computerstore:
    for i in k:
        if i in string.punctuation:
            k = k.replace(i, "")
    computerstoreDel.append(k)
Dict=dict(zip(computerstoreDel,computerstore))
sharedStore = []
count = 3  # 超时
Round=5
while True:
    time_start = time.time()
    print("请说一句带月的诗词吧：（用空格将前后两句隔开哦）")  # 用户说诗句
    while True:
        user = input()
        user = ''.join(user.split())  # 将空格删掉
        n = len(user)
        if not is_Chinese(user):
            print("出现了汉字之外的字符哦，请再说一句吧：")
        elif n < 8:
            print("这句不完整哦，再补充下吧：")
        elif "月" not in user:
            print("要含有关键字“月”哦，检查一下再输入一次吧：")
        elif user in sharedStore:
            print("这句之前出现过了哦，说句新的吧：")
        elif user not in computerstoreDel:
            print("这句是诗词吗？不然再说一句吧：")
        else:
            break
    time_end = time.time()
    sharedStore.append(user)
    computerstoreDel.remove(user)
    output = computerstoreDel.pop(0)
    sharedStore.append(output)
    print(Dict[output])

    time_cost = time_end - time_start
    if time_cost > 30:
        count -= 1
        print("已超时，超时机会还剩{}次".format(count))
    if count < 0:
        print("很遗憾，你输了哦")
        break


    Round-=1
    print("剩余回合数:{}".format(Round))
    if Round==0:
        print("恭喜，你赢得了这此飞花令！")
        break

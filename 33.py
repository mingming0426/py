v = int(input("有多少铅笔："))
class Aa():
    def __init__(self, name, count):
        self.name = name
        self.count =v

    def add(self):
        a = int(input("进货多少："))
        self.count = a + self.count
        print("进货后的" + self.name, self.count)

    def sell(self):
        b = int(input("卖出多少："))
        self.count = self.count - b
        print("卖出后的" + self.name, self.count)


c = Aa("铅笔", v)
while True:

    d = int(input("""
    1、添加货物
    2、卖出货物"""))
    if d == 1:
        c.add()
    elif d == 2:
        c.sell()

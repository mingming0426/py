class Student():
    # 初始化方法
    def __init__(self, name, maths, chinese, english):
        self.name = name
        self.maths = maths
        self.chinese = chinese
        self.english = english
    def report(self):
        print(self.name,"的语文成绩是：",self.chinese)
        print(self.name,"的数学成绩是：",self.maths)
        print(self.name,"的英语成绩是：",self.english)

zhangsan = Student("张三 ",95,100,80)
zhangsan.report()
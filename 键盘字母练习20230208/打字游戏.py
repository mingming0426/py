"""
打字游戏
1. 声明列表word、xx(x坐标值)、yy（y坐标值）
2. 创建init()函数，初始化三个列表
3. 第四部分：paint ===>绘制字符
4. 第三部分：action ===>进行字母移动
5. 键盘监听事件  循环比对
"""
# 导入随机函数模块
import random
import time

import pygame
import sys
from playsound import playsound

"""
第零部分：游戏开始说明提示
"""


def tishi():
    # 初始化
    pygame.init()
    # 创建一个窗口
    screen = pygame.display.set_mode((800, 600))
    # 设置窗口标题
    pygame.display.set_caption('打字游戏')
    pygame.font.init()
    # 4.2 设置字体样式
    font = pygame.font.Font("msyh.ttf", 28)
    text = '游戏说明：\n' \
           '1，请根据画面提示输入对应字母；\n' \
           '2，每得分100会声音提示，并且字母下落会加速；\n' \
           '3，每正确1个字母得5分；\n' \
           '4，总共漏掉10个字母游戏自动结束；\n\n\n' \
           '请点击鼠标开始吧！'
    # 多行输出游戏说明
    blitlines(screen, text, font, (255, 255, 255), 200, 100)
    # 通过不断循环来侦听事件
    while True:
        screen.blit(back, (0, 0))
        blitlines(screen, text, font, (255, 255, 255), 100, 100)
        # get():获取事件的返回值
        for event in pygame.event.get():
            # 判断事件是否是退出事件，是则退出
            if event.type == pygame.QUIT:
                # 先退出pygame窗口，再退出程序
                pygame.quit()
                sys.exit()
            # 单击鼠标窗口 游戏开始
            if event.type == pygame.MOUSEBUTTONDOWN:
                init()
                menu()
            # 更新整个待显示的 Surface 对象到屏幕上
            pygame.display.flip()


# def tishi():
#     global shuoming
#     print(time.ctime())
#     # 4.1 初始化字体
#     pygame.font.init()
#     # 4.2 设置字体样式
#     font = pygame.font.Font("msyh.ttf", 28)
#     shuoming = font.render("游戏说明：", True, (0, 255, 0))
#     # 4.6 绘制游戏说明
#     screen.blit(shuoming, (20, 300))  # 将字符串绘制到该窗口上
#     # time.sleep(5)
"""
第一部分：主函数
"""


def menu():
    # 1.设置窗口标题
    pygame.display.set_caption("打字游戏")

    # 2.无限循环
    while True:
        # 3.设置背景颜色填充
        # screen.fill((255, 255, 255))
        # 绘制哪张图，以及起始点位置
        screen.blit(back, (0, 0))
        # 4.调用业务处理函数
        action()
        # 5.调用图形图案绘制函数
        paint()
        # 7.屏幕刷新延迟
        pygame.time.delay(speed)
        # 6.设置窗口刷新屏幕
        pygame.display.update()


"""
第二部分：变量声明初始化区域
"""
# 设置窗体
screen = pygame.display.set_mode((800, 600), 0, 0)
# 存储字母列表
word = []
# 存储字母坐标值列表
xx = []
yy = []
# 存储得分
score = 0
# 存储RGB颜色值
R = 0
G = 0
B = 0
# 存储速度
speed = 20
# 加载图片（选一张好看的图片作为背景）
back = pygame.image.load("打字游戏.png")
# 失败个数
failCount = 0
gk = 0

"""
第三部分：业务逻辑处理区域
"""


def action():
    global score
    global failCount
    global gk
    global speed
    # 4.1 循环迭代事件监听
    for event in pygame.event.get():
        # 4.2 判断是否退出系统
        if event.type == pygame.QUIT:
            sys.exit()
        # 4.4 循环比对
        if event.type == pygame.KEYDOWN:  # 键盘按下
            # 4.5 循环遍历与按键比较
            for i in range(0, 10):
                # 4.6 判断
                if event.key == word[i] + 32:
                    # 4.7 业务处理
                    word[i] = random.randint(65, 90)  # 使得word“消失”
                    xx[i] = random.randint(0, 800)  # xx坐标另产生一个随机数，表现为“消失”
                    # 使得yy坐标“消失”,yy坐标变负号，消失在屏幕看不见的位置
                    yy[i] = -random.randint(0, 600)
                    score += 5
                    if score % 100 == 0:
                        playsound("打字游戏-得分声音.wav")
                        gk += 1  # 关卡加一
                        speed -= 5  # 根据分数修改速度
                    # 4.8 退出比较，防止一次按键消失多个相同字母
                    break
    # 4.3 字母移动
    for i in range(0, 10):
        yy[i] += 1
        # 循环判断
        if yy[i] > 600:
            yy[i] = 0
            # 失败个数+1
            failCount += 1
            playsound("打字游戏-失败声音.wav")

    if failCount > 10:
        sys.exit()


"""
第四部分：图形图案绘制区域
"""


def paint():
    # 4.1 初始化字体
    pygame.font.init()
    # 4.2 设置字体样式
    font = pygame.font.Font("msyh.ttf", 28)
    # font = pygame.font.SysFont('微软雅黑', 27, bold=False, italic=False)
    # 4.3 循环迭代
    for i in range(0, 10):
        # 4.7 调用updateColor
        updateColor()
        # 4.4 设置绘制内容
        fontRead = font.render(chr(word[i]), True, (R, G, B))  # int转字符串，字体为黑色
        scoreShow = font.render("分数:%s" % score, True, (255, 0, 0))
        failShow = font.render("遗漏个数:%s" % failCount, True, (0, 0, 255))
        gks = font.render("关卡：%s" % gk, True, (0, 255, 0))
        # 4.5 设置绘制内容的坐标
        screen.blit(fontRead, (xx[i], yy[i]))  # 将字符串绘制到该窗口上
        # 4.6 绘制分数
        screen.blit(scoreShow, (20, 20))  # 将字符串绘制到该窗口上
        screen.blit(failShow, (20, 60))  # 将字符串绘制到该窗口上
        screen.blit(gks, (20, 100))  # 将字符串绘制到该窗口上


"""
第五部分：初始化函数
"""


def init():
    for i in range(0, 10):
        # 字母 ===》A :65  a==>97
        word.append(random.randint(65, 90))
        # 坐标值
        xx.append(random.randint(10, 790))
        yy.append(random.randint(0, 400))


"""
第六部分：更改RGB颜色值
"""


def updateColor():
    global R, G, B
    R = random.randint(0, 0)
    G = random.randint(0, 0)
    B = random.randint(0, 0)


def blitlines(surf, text, renderer, color, x, y):
    h = renderer.get_height()
    lines = text.split('\n')
    for i, ll in enumerate(lines):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y + (i * h)))


# main函数
if __name__ == '__main__':
    tishi()
    # init()
    # menu()

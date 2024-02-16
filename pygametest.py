import pygame
import sys

textList = []


class Message:
    size = 28

    def __init__(self, text):
        self.text = text
        self.size = Message.size
        self.color = (100, 100, 100)
        self.bg = None
        self.font = pygame.font.SysFont('simhei', self.size)
        self.surface = self.font.render(self.text, True, self.color, self.bg)
        self.rect = self.surface.get_rect()

    def show_me(self, screen):
        screen.blit(self.surface, self.rect)


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def cut_text(text):
    global lineSpacing  # 行距
    lineSpacing = Message.size * 0.6
    for i in range(0, len(text) + 1):
        m = Message(text[0:i])
        if m.rect.width > 780:
            textList.append(text[0:i - 1])
            # if (Message.size + lineSpacing) * len(textList) > 580: textList.remove(textList[0])
            # 上边一行主要解决超过窗口高度
            text = text[i - 1:len(text)]
            cut_text(text)
            break
        if i == len(text) and m.rect.width <= 780:
            textList.append(text[0:i])
            # if (Message.size + lineSpacing) * len(textList) > 580: textList.remove(textList[0])
            print(m.rect.height, m.size)


def messageShow(screen):
    for i in range(0, len(textList)):
        m = Message(textList[i])
        m.rect.left = 10
        m.rect.top = 10 + i * (Message.size + lineSpacing)
        m.show_me(screen)


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    text = '    微软必应(英文名：Bing)是微软公司于2009年5月28日推出，用以取代Live Search的全新搜索引擎服务。为符合中国用户使用习惯，' \
           'Bing中文品牌名为“必应”。作为全球领先的搜索引擎之一，[1]截至2013年5月，必应已成为北美地区第二大搜索引擎，如加上为雅虎提' \
           '供的搜索技术支持，必应已占据29.3%的市场份额。2013年10月，微软在中国启用全新明黄色必应搜索标志并去除Beta标识，这使必应成为' \
           '继Windows、Office和Xbox后的微软品牌第四个重要产品线，也标志着必应已不仅仅是一个搜索引擎，更将深度融入微软几乎所有的服务' \
           '与产品中。在Windows Phone系统中，微软也深度整合了必应搜索，通过触摸搜索键引出，相比其他搜索引擎，界面也更加美观，整合信息' \
           '也更加全面。[2]'
    cut_text(text)

    while True:
        screen.fill((0, 0, 0))
        messageShow(screen)
        check_event()
        pygame.display.flip()
        pygame.time.Clock().tick(60)


run_game()

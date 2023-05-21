import random
import string
import sys

import easygui

mms = ['慢的', '绿色', '红色的', '骄傲的', '蓝色的', '湿的', '胖的', '勇敢的']
ns = ['苹果🍎', '球⚽️', '龙🐲', '熊猫🐼', '锤子🔨', '手机📱', '电视📺']
es =['树🌲','树叶🍂','树枝🌿','花🌹']
flavor = easygui.msgbox('欢迎到密码盒')

while True:
    mm = random.choice(mms)
    n = random.choice(ns)
    e =random.choice(es)
    number = random.randrange(0, 100)
    sprcial_char = random.choice(string.punctuation)

    password = mm + n + e+str(number) + sprcial_char
    easygui.msgbox('你的密码：%s' % password)

    response = easygui.buttonbox("你需要一个新密码么？", choices=['yes', 'no'])
    if response == 'no':
        break
sys.exit()
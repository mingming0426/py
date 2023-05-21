import random
import string
import sys
import easygui
import keyboard

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVIXYZ"
welcome = easygui.msgbox('欢迎来玩字母游戏')
len= 6
mm = random.sample(s,len)

easygui.msgbox('这些字母是: %s' % mm)


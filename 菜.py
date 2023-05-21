import sys

import easygui

flavor = easygui.buttonbox('你喜欢什么菜？',
                           choices=['咖哩牛肉', '四季豆', '清炒白菜'])  # List of choices
easygui.msgbox("喜欢 " + flavor)
sys.exit()
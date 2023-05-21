import sys

import easygui

flavor = easygui.buttonbox('你喜欢什么饭？',
                           choices=['米饭', '面条', '米线'])   # List of choices
easygui.msgbox("喜欢 " + flavor)
sys.exit()
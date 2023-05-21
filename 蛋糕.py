import sys

import easygui
import tkinter
flavor = easygui.buttonbox('你喜欢什么口味的蛋糕？',
                           choices=['巧克力', '水果', '冰其淋'])  # List of choices
easygui.msgbox("喜欢 " + flavor + '味蛋糕')
sys.exit()
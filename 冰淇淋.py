import sys

import easygui
import tkinter
flavor = easygui.buttonbox('你喜欢什么口味的冰其淋？',
                           choices=['巧克力', '香草','芒果' ,'草莓'])  # List of choices

easygui.msgbox("喜欢 " + flavor + '味冰淇淋')
sys.exit()
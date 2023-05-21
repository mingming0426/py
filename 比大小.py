# Listing_7-1_using_the_comparison_operators.py
# Copyright Warren & Carter Sande, 2009-2019
# Released under MIT license   https://opensource.org/licenses/mit-license.php
# ------------

num1 = float(input("输入第一个数字: "))
num2 = float(input("输入第二个数字: "))
if num1 < num2:
    print(num1, "小于", num2)
if num1 > num2:
    print(num1, "大于", num2)
if num1 == num2:  # Remember that this is a double equal sign
    print(num1, "相等", num2)
if num1 != num2:
    print(num1, "不相等", num2)

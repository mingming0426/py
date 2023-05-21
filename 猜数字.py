import random

n = eval(input('请随机输入一个1~100间的数:'))
r = random.randint (1,100)
# print(r)
for i in range(10,0,-1):
     if n > r :
          print('猜大了，您还有{}次机会，请再试试！'.format(i-1))
     elif n < r :
          print('猜小了，您还有{}次机会，请再试试！'.format(i-1))
     else :
          print("恭喜你，猜对了！✿✿ヽ')°▽°ノ✿")
          break
     if i == 1:
          print('很遗憾，你的机会已用完┭┮﹏┭┮')
          break
     n = eval(input('请随机输入一个1~100间的数:'))
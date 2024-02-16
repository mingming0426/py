# 井字棋游戏

# 初始化游戏棋盘
board = [' '] * 9
game_over = False
current_player = 'X'


# 打印游戏棋盘
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')


# 判断游戏是否结束
def check_game_over():
    # 判断行是否有胜者
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    # 判断列是否有胜者
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    # 判断对角线是否有胜者
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True

    # 判断是否平局
    if ' ' not in board:
        return True

    return False


# 电脑选择下棋位置
def computer_move():
    import random
    while True:
        position = random.randint(0, 8)
        if board[position] == ' ':
            return position


# 游戏循环
while not game_over:
    print_board()
    if current_player == 'X':
        # 人下棋
        while True:
            position = int(input("请输入下棋位置（0-8）："))
            if position >= 0 and position <= 8 and board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print("输入无效，请重新输入。")
    else:
        # 电脑下棋
        position = computer_move()
        board[position] = 'O'

    # 判断游戏是否结束
    game_over = check_game_over()

    # 切换下一个玩家
    current_player = 'O' if current_player == 'X' else 'X'

# 游戏结束，打印结果
print_board()
if ' ' not in board:
    print("平局！")
else:
    print("玩家", current_player, "获胜！")

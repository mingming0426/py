def count_digits(input_str):
    digit_count = {}  # 创建一个空字典来存储数字出现的次数

    for digit in input_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    return digit_count


input_str = input("请输入一串数字: ")
result = count_digits(input_str)

print("输出:", result)

# Converting binary numbers to decimal, performing addition, and converting back to binary

# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]  # [2:] is used to remove the '0b' prefix

# List of problems
problems = [
    ("11", "11"),  # 11 + 11
    ("101", "11"),  # 101 + 11
    ("1111", "11"),  # 1111 + 11
    ("1001", "110"),  # 1001 + 110
    ("10101", "1010")  # 10101 + 1010
]

# Calculate and compare
results = []
for problem in problems:
    binary_sum = decimal_to_binary(binary_to_decimal(problem[0]) + binary_to_decimal(problem[1]))
    results.append((problem[0] + " + " + problem[1], binary_sum))

results

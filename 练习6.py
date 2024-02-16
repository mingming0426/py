count = 0
lst = []
for i in range(150):
    lst.append(1)

lst = []
for i in range(150):
    lst.append(0)

for j in range(1, 151):
    for z in range(1, 151):
        if j % z == 0:
            if lst[j - 1] == 1:
                lst[j - 1] = 0
            else:
                lst[j - 1] += 1
for i in lst:
    if i % 2 == 0:
        count += 1

print(count)

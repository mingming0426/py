import time
start=time.process_time()
prime = []
for i in range(2,1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)


for A in prime:
    for B in prime:
        for C in prime:
            if A+B+C+A*B*C==999:
                print(A,B,C)
end=time.process_time()
print("密码破解程序共耗时{}秒".format(end-start))
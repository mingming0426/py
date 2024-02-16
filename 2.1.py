import time
start=time.process_time()
prime = []
for i in range(101):
    for j in range(2, i):
        if i % j == 0:
            prime.append(i)
            break
end=time.process_time()

print(prime)
print()
print(end-start)


sum = 0
for i in range(1, 2000001):
    sum += 1 / (i*i)
    if i % 5000 == 0:
        print(sum)
print(sum)
while 1:
    N = int(input())
    if 1 <= N <= 1000000000:
        break

count = 1

while N - 1 > 0:
    N -= 6 * count
    count += 1

print(count)
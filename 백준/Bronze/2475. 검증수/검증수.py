total = 0
uniqueNumber = list(map(int, input().split()))
for number in uniqueNumber:
    total += number ** 2
print(total % 10)
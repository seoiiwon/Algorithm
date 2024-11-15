totalNumbers = 1
for i in range(3):
    while(1):
        num = int(input())
        if 100 <= num < 1000:
            totalNumbers *= num
            break

numList = [0 for _ in range(10)]
for i in range(len(str(totalNumbers))):
    numList[totalNumbers % 10] += 1
    totalNumbers //= 10

for num in numList:
    print(num)
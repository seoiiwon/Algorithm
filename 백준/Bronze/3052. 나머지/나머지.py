restList = set()

for i in range(10):
    while(1):
        num = int(input())
        if 0 <= num <= 1000:
            restList.add(num % 42)
            break

print(len(restList))
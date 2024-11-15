while(1):
    N = int(input())
    if 1 <= N <= 1000000:
        break

while(1):
    numList = list(map(int, input().split()))
    count = 0
    for num in numList:
        if num < -1000000 or num > 1000000:
            count += 1
    if count == 0:
        break

print(min(numList), max(numList))
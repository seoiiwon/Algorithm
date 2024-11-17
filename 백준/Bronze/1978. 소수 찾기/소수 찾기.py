def checkPrime(num):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

while(1):
    N = int(input())
    if 1 <= N <= 100:
        break

while(1):
    numList = list(map(int, input().split()))
    if len(numList) == N and all(1 <= n <= 1000 for n in numList):
        break

if 1 in numList:
    numList.remove(1)

count = 0

for n in numList:
    if checkPrime(n):
        count += 1

print(count)
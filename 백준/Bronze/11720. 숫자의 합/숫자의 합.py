while(1):
    N = int(input())
    if 1 <= N <= 100:
        break

while(1):
    numList = list(map(int, input()))
    if len(numList) == N:
        break

print(sum(numList))
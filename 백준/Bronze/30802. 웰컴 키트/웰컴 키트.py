while(1):
    N = int(input())
    if 1 <= N <= 10 ** 9:
        break

while(1):
    size = list(map(int, input().split()))
    if  sum(size) == N and all(0 <= s <= N for s in size):
        break

while(1):
    T, P = map(int, input().split())
    if 2 <= T <= 10 ** 9 and 2 <= P <= 10 ** 9:
        break

amountT = 0
amountP = []

for s in size:
    if s % T == 0:
        amountT += s // T
    else:
        amountT += s // T + 1

amountP.append(N // P)
amountP.append(N % P)

print(amountT)
print(amountP[0], amountP[1])
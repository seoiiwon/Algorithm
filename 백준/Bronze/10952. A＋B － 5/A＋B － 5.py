sumList = []
while(1):
    A, B = map(int, input().split())
    count = 0
    if A > 0 and B < 10 and A + B != 0:
        sumList.append(A + B)
    else:
        break

for i in sumList:
    print(i)
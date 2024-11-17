while 1:
    N = int(input())
    if 1 <= N <= 1000:
        break

while 1:
    gradeList = list(map(int, input().split()))
    if len(gradeList) == N and max(gradeList) > 0:
        break

total = 0
maxGrade = max(gradeList)
for grade in gradeList:
    total += grade / maxGrade * 100

print(total / len(gradeList))
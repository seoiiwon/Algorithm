def oxQuizPoint(oxResult):
    beforeResult = 0
    point = 0
    for result in range(len(oxResult)):
        if oxResult[result] == 'O': 
            if beforeResult == 0:
                point += 1
                beforeResult = 1
            else:
                point += beforeResult + 1
                beforeResult += 1
        else:
            beforeResult = 0
    return point

N = int(input())
pointList = []
for n in range(N):
    oxResult = str(input())
    if 0 < len(oxResult) < 80:
        pointList.append(oxQuizPoint(oxResult))

for point in pointList:
    print(point)
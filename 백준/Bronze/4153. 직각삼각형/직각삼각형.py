def calcDiagonal(side1, side2, side3):
    triangleList = [side1, side2, side3]
    diagonal = max(triangleList)
    triangleList.remove(diagonal)
    if diagonal ** 2 == triangleList[0] ** 2 + triangleList[1] ** 2:
        return "right"
    else:
        return "wrong"

while(1):
    sideList = list(map(int, input().split()))
    if sideList == [0, 0, 0]:
        break
    print(calcDiagonal(sideList[0], sideList[1], sideList[2]))
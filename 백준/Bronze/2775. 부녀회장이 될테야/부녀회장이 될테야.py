def whatsInMyRoom(floor, room):
    aptList = [[r for r in range(1, room + 1)]]
    for f in range(1, floor + 1):
        floorList = []
        for r in range(room):
            floorList.append(sum(aptList[-1][:r+1]))
        aptList.append(floorList)

    return aptList

T = int(input())

for t in range(T):
    k = int(input())
    n = int(input())
    print(whatsInMyRoom(k, n)[-1][-1])
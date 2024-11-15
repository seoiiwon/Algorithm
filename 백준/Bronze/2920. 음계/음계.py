def checkType(code):
    codeType = ['ascending', 'descending', 'mixed']
    if code == [1, 2, 3, 4, 5, 6, 7, 8]:
        return codeType[0]
    elif code == [8, 7, 6, 5, 4, 3, 2, 1]:
        return codeType[1]
    else:
        return codeType[2]

while(1):
    code = list(map(int, input().split()))
    if len(set(code)) == 8 and max(set(code)) == 8 and min(set(code)) == 1:
        break

print(checkType(code))
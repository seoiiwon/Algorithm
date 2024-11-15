alphaList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

while(1):
    text = str(input())
    if text.islower() and 1 <= len(text) <= 100:
        break
for t in range(len(text)):
    if alphaList[ord(text[t]) - 97] == -1:
        alphaList[ord(text[t]) - 97] = t

for i in alphaList:
    print(i, end=' ')
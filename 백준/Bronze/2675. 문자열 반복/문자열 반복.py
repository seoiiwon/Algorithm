while(1):  
    T = int(input())
    if 1 <= T <= 1000:
        break

outputList = []

for t in range(T):
    while(1):
        inputValue = input().split()
        if 1 <= int(inputValue[0]) <= 8 and 1 <= len(inputValue[1]) <= 20:
            output = ''
            for repeat in range(len(inputValue[1])):
                output = output + inputValue[1][repeat] * int(inputValue[0])
            outputList.append(output)
            break

for output in outputList:
    print(output)
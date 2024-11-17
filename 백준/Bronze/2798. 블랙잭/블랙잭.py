# combination 함수 써서 블로그 올리기
def calcCardSum(cardNumList):
    currentSum = 0

    for _ in range(len(cardNumList)):
        card1 = cardNumList[0]
        cardNumList.remove(card1)
        for j in range(len(cardNumList)):
            card2 = cardNumList[j]
            for card3 in cardNumList[j+1:]:
                cardSum = card1 + card2 + card3 
                if cardSum == M:
                    return M
                elif cardSum < M and M - cardSum < M - currentSum:
                    currentSum = cardSum
    return currentSum

while 1:
    N, M = map(int, input().split())
    if 3 <= N <= 100 and 10 <= M <= 300000:
        break

while 1:
    cardNumList = list(map(int, input().split()))
    if len(cardNumList) == N and all(1 <= c < 100000 for c in cardNumList):
        break

print(calcCardSum(cardNumList))
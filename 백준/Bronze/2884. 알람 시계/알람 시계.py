while(1):
    H, M = map(int, input().split())
    if 0 <= H <=23 and 0 <= M <= 59:
        break

alarmTime = H * 60 + M - 45

if alarmTime // 60 < 0:
    alarmH = 23
else:
    alarmH = alarmTime // 60

print(alarmH, alarmTime % 60)
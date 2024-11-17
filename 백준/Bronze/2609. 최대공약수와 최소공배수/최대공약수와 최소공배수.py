while 1:
    num1, num2 = map(int, input().split())
    if 1 <= num1 <= 10000 and 1 <= num2 <= 10000:
        break

num1List = set()
num2List = set()

for num in range(1, num1 + 1):
    if num1 % num == 0:
        num1List.add(num)

for num in range(1, num2 + 1):
    if num2 % num == 0:
        num2List.add(num)

num1num2 = num1 * num2
for i in list(num1List.union(num2List))[::-1]:
    if (num1num2 // i) % num1 == 0 and (num1num2 // i) % num2 == 0:
        num1num2 //= i

print(max(num1List.intersection(num2List)))
print(num1num2)

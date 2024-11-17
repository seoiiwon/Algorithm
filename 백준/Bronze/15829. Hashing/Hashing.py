L = int(input())

while 1:
    text = str(input())
    if text.lower() == text and len(text) == L:
        break
    
hashTotal = 0
for i in range(len(text)):
    hashTotal += (ord(text[i]) - 96) * 31 ** i

print(hashTotal % 1234567891)
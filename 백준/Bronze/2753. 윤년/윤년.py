def checkLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0
    
while(1):
    year = int(input())
    if 1 <= year <= 4000:
        break

print(checkLeapYear(year))
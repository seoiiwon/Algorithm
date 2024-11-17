while 1:
    number = list(str(input()))
    if number == ['0']:
        break

    if number == number[::-1]:
        print('yes')
    else:
        print('no')
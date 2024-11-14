def returnOperator(result):
    if result == 0:
        return '=='
    elif result < 0:
        return '<'
    else:
        return '>'

numbers = list(map(int, input().split()))
print(returnOperator(numbers[0] - numbers[1]))
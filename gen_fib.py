def fibonacci(max_num):
    result = []
    number1 = 0
    number2 = 1
    for _ in range(max_num):
        result.append(number1)
        number1, number2 = number2, number1 + number2
    return result

for num in fibonacci(6):
    print(num)
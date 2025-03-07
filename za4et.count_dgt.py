def count_dgt(number):
    count = [0] * 10

    while number > 0:
        count[number % 10] += 1
        number //= 10

    for index in range (10):
        print(index, " - ", count[index])

count_dgt(1234567890)
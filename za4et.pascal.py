def factorial(number):
    result = 1
    for multiplier in range(1, number + 1):
        result *= multiplier
    return result

def pascal(row_index):
    row = [0] * (row_index + 1)
    for place in range (row_index + 1):
        row[place] = factorial(row_index) // (factorial(place) * factorial(row_index - place))
    print(row)

pascal(5)

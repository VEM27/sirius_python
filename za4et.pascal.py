def pascal(row_index):
    import math
    row = [0] * (row_index + 1)
    for place in range (row_index + 1):
        row[place] = math.factorial(row_index) // (math.factorial(place) * math.factorial(row_index - place))
    print(row)

pascal(5)
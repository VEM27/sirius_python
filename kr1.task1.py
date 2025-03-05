def multiplication_table (a, b, c, d):
    column = [1] * (d - c + 2)
    line = [1] * (b - a + 2) 
    for multiplier1 in range(1, d - c + 2):
        column[multiplier1] = c + multiplier1 - 1

    for multiplier2 in range(1, b - a + 2):
        line[multiplier2] = a + multiplier2 - 1

    for multiplier1 in range(b - a + 2):
        for multiplier2 in range(d - c + 2):
            if multiplier1 == 0 and multiplier2 == 0:
                print("  ", end=" ")
            elif multiplier2 == d - c + 1:
                print(line[multiplier1] * column[multiplier2])
            else:
                print(line[multiplier1] * column[multiplier2], end=" ")

multiplication_table(7, 10, 5, 6)
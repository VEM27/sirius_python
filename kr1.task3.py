def DNK(genom):
    check = ' '
    count = ''
    gnm=''
    for position in range(len(genom)):
        if check == genom[position]:
            count += 1
        else:
            gnm += check + str(count)
            check = genom[position]
            count = 1
    print(gnm)

    
DNK('aaaabbcaa')
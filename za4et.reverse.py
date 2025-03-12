def reverse(word, k):
    word = list(word)
    for index in range(0, len(word), 2 * k):

        if index == 0:
            word[index : index + k] = word[index + k - 1 :: -1]

        else:
           word[index : index + k] = word[index + k - 1 : index - 1 : -1] 

    return ''.join(word)

reverse('0123456789', 2)
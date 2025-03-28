def abbr(full_title):
    abbr_title = ''
    full_title = ' ' + full_title
    for letter in range (len(full_title) + 1):
        if full_title[letter - 1] == ' ' and full_title[letter].isalpha():
            abbr_title += full_title[letter].capitalize()
    print(abbr_title)

abbr('Кот обладает талантом')

def abbr(full_title):
    abbr_title = ''
    full_title = ' ' + full_title
    for letter in range (1, len(full_title) + 1):
        if full_title[letter - 1] == ' ' and ((ord(full_title[letter]) >= ord('A') and ord(full_title[letter]) <= ord('Z')) or \
            (ord(full_title[letter]) >= ord('А') and ord(full_title[letter]) <= ord('Я'))):
            abbr_title += full_title[letter]
    print(abbr_title)


abbr('English Русский 27')
def check_part(string, part):
    section = len(part) - 1
    count = 0
    for place in range (len(string) - section):
        if part == string[place : section + place + 1]:
            count += 1
    print(count)

check_part('abbaba', 'ab')
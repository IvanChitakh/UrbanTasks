counter = 0


def string_info(word):
    global counter
    counter += 1
    return len(word), word.upper(), word.lower()


def is_contains(word, list):
    global counter
    counter += 1
    list1 = ' '.join(list).lower()
    list1 = list1.split(' ')
    word = word.lower()
    if word in list1:
        return True
    else:
        return False


def calls():
    return counter


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls())
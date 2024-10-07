calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(word):
    count_calls()
    return len(word), word.upper(), word.lower()


def is_contains(word, list):
    count_calls()
    list1 = ' '.join(list).lower()
    list1 = list1.split(' ')
    word = word.lower()
    if word in list1:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
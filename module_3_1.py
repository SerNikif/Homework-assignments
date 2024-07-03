calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    global calls
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    global calls
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

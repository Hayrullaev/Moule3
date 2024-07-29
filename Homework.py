calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    upper_case = string.upper()
    lower_case = string.lower()
    return (len(string), upper_case, lower_case)

def is_contains(string, list_to_search):
    for item in list_to_search:
        if item.lower().strip() == string.lower().strip():
            return True
    return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic'])) 
print(calls)
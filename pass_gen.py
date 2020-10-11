import random
import string

# Generate lower and upper case letters
LETTERS = string.ascii_letters

NUMS = '012345678'

SPE = '!@#$%^&*()_+][/.,<>?'

SYMBOLS = LETTERS + NUMS + SPE

user_input = True

while True:
    try:
        len = int(input("Enter you desired password length: "))
        if type(len) == int:
            break
    except ValueError:
        print("Please input a valid number!\n")

# Generate password from the random sample based on len value
password = ''.join(random.sample(SYMBOLS, len))

print('\n' + password + '\n')

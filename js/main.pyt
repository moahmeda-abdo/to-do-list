import random

#Chosse Password strength
max_length = int

pass_strength= input('Choose your Password strength (strong / meduim / weak ) ')

if pass_strength.lower() == 'strong':
    max_length = 15

elif pass_strength.lower() == 'meduim':
    max_length = 10

else:
    max_length = 7


#Arrays to create password from its contents
CHARS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

UPCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']


# Concatenate all characters arrays  to  one array
FINAL_LIST = NUMBERS + UPCASE + LOWERCASE + CHARS
print(FINAL_LIST)

# randomly select one character from arrays
rand_digit = random.choice(NUMBERS)
rand_upper = random.choice(UPCASE)
rand_lower = random.choice(LOWERCASE)
rand_symbol = random.choice(CHARS)

rand_pass = rand_digit + rand_upper + rand_lower + rand_symbol



for x in range(max_length - 4):
	rand_pass = rand_pass + random.choice(FINAL_LIST)


# print  password

print( rand_pass)

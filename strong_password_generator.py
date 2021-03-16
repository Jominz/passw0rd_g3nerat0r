import random

# You can change here the password's elements; remember that for a strong password
# is recommend a good 'randomness'
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          '.', ',', ';', ':', '-', '_', '!', '|', '$', '%', '&', '(', ')', '=',
          '+', '[', ']', '{', '*', '}', '#', '@', '°', '^', '?', '<', '>', '€',
          'è', 'é', 'ì', 'ç', 'ò', 'ù', '§', 'à']

# You can change here the password length; remember that for a strong password
# is recommended a length of, at least, 16 characters.
length = 16

password = ''
while len(password) < length:
    random_element = random.randrange(0, len(values))
    password += str(values[random_element])
print("Here your password:\n")
print(password)
import random
def generate_password(length):
    passwordChars = []
    for i in range(length):
        randChar = chr(random.randint(33, 122))
        passwordChars.append(randChar)

    password = ''.join(passwordChars)
    print(password)

def prompt_length():
    random.seed()
    passLength = input("Enter length of desired password: ")
    generate_password(passLength)


prompt_length()
import random
def generate_password(length):
    password = []
    for i in range(length):
        randChar = chr(random.randint(33, 122))
        password.append(randChar)

    print(password)

def prompt_length():
    random.seed()
    passLength = input("Enter length of desired password: ")
    generate_password(passLength)


prompt_length()
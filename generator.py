import random

def generate_password(length, data):
    password = ''
    for i in range(length):
        index = random.randint(0, len(data) - 1)
        character = data[index]
        password += character
    return password

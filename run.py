from data import *
from generator import generate_password

password_length = int(input("How long should the password be? "))

data = alphabet + numbers + special_characters
password = generate_password(password_length, data)
print("Here is your password: {}".format(password))

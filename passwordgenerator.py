import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    # password = ''.join(random.choice(characters) for i in range(length))
    # print(characters)
    password=''
    for i in range(length):
        print("i",i)
        password +=random.choice(characters)
    return password

print("Generated Password:", generate_password(12))

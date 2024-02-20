import random
import string


def generate_random_email(char_num):
    char = ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
    email = char + "@gmail.com"
    return email


def generate_random_phone_number():
    random_number = int(''.join([str(random.randint(0, 9)) for _ in range(10)]))
    return random_number

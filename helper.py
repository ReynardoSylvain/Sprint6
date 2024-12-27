import random

def generate_phone_number():
    return "+79" + "".join([str(random.randint(0, 9)) for _ in range(9)])
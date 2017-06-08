import random


def generate_verification_code():
    return str(int(random.random() * 10000)).zfill(4)

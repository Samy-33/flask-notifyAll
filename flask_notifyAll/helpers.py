import random
from flask_notifyAll.constants import VERIFICATION_CODE_LENGTH


def generate_verification_code():
    """
    :return: Random generated code
    """
    multiplier = 10 ** VERIFICATION_CODE_LENGTH
    return str(int(random.random() * multiplier)).zfill(VERIFICATION_CODE_LENGTH)

import random
import string

ALPHA_NUMERIC_STRING = string.ascii_lowercase + string.digits
ALPHA_LENGTH = 6


def generate_random_text(chars=ALPHA_NUMERIC_STRING, length=ALPHA_LENGTH):
    random_text = ''.join([random.choice(chars) for _ in range(length)])
    return random_text

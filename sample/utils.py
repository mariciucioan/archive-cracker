from os.path import join
import string

from pathlib import Path

# Constants

ROOT_DIR = Path(__file__).parent.parent
RESOURCES_DIR = join(ROOT_DIR, 'resources')
IMAGES_DIR = join(RESOURCES_DIR, 'images')

MAX_PASS_LEN = 10
DEFAULT_CHARS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)


# Methods

def get_resource(name):
    return join(RESOURCES_DIR, name)


def get_image(name):
    return join(IMAGES_DIR, name)


def list_of_chars_to_string(comb):
    combined_chars = ''
    for character in comb:
        combined_chars += character

    return combined_chars


def fact(n):
    return 1 if n <= 1 else fact_help(n)


def fact_help(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def count_brute_passwords(k_pass, n_chars):
    counter = 0
    for i in range(1, k_pass + 1):
        counter += fact(n_chars) / fact(n_chars - i)

    return counter

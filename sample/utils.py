import os
import string
from pathlib import Path

import itertools

# Constants

ROOT_DIR = Path(__file__).parent.parent
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

MAX_PASS_LEN = 10
DEFAULT_CHARS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

# Methods

def get_resource(name):
    return os.path.join(RESOURCES_DIR, name)

def list_to_list_of_str(lst):
    list = lst.copy()
    arr = ['']
    for i in list:
        arr += i

    return arr

def combination_to_string(comb):
    str = ''
    for character in comb:
        str += character

    return str

def differentFlagPermutations(max_len=MAX_PASS_LEN, arr=None):
    if arr is None:
        arr = DEFAULT_CHARS

    vals = list_to_list_of_str(arr)

    return vals

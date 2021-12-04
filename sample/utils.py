import os
import string
from pathlib import Path

# Constants

ROOT_DIR = Path(__file__).parent.parent
RESOURCES_DIR = os.path.join(ROOT_DIR, 'resources')

MAX_PASS_LEN = 10
DEFAULT_CHARS = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)

# Methods

def get_resource(name):
    return os.path.join(RESOURCES_DIR, name)

def differentFlagPermutations(max_len=MAX_PASS_LEN, arr=None):
    if arr is None:
        arr = DEFAULT_CHARS

    ml = arr.copy()
    vals = ml

    count = len(ml)

    for z in range(max_len - 1):
        tmp = []

        for i in arr:
            for k in ml:
                if i not in k:
                    tmp.append(k + i)
                    count += 1

        vals += tmp

        ml = tmp

    return vals